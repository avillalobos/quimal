/*
 * Copyright (C) 2008, Morgan Quigley and Willow Garage, Inc.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *   * Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   * Neither the names of Stanford University or Willow Garage, Inc. nor the names of its
 *     contributors may be used to endorse or promote products derived from
 *     this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#include "LX200.h"

using std::string;
using std::exception;
using std::cout;
using std::cerr;
using std::endl;
using std::vector;

LX200::LX200(string device, int baud_rate, int timeout){
	this->serial_device = new serial::Serial(device, baud_rate, serial::Timeout::simpleTimeout(timeout));
	ros::NodeHandle n;
	ros::ServiceServer get_info = n.advertiseService("getInfo", &LX200::getInfo, this);
	ros::ServiceServer set_slewrate = n.advertiseService("setSlewRate", &LX200::setSlewRate,this);
	ros::ServiceServer set_target = n.advertiseService("setTarget", &LX200::setTarget,this);
	ros::ServiceServer park = n.advertiseService("Park", &LX200::Park,this);
	ros::ServiceServer stop = n.advertiseService("StopSlewing", &LX200::stopSlewing,this);
}

Telescope::~Telescope(){
	delete this->serial_device;
}

// INFO Section

telescope::TelescopeInfo LX200::getTelescopeInfo(){
	ROS_INFO("Waiting for telescope status");
	telescope::TelescopeInfo info;
	info.RA = readRA();
	info.DEC = readDEC();
	info.Sidereal = "blablabla";
	info.azimut = 90.9;
	info.altitud = 1.2;
	info.slew_rate = "lentito";
	info.msg = "Atributo para enviar mensajes custom :D";
	ROS_INFO("Status retrieved successfully");
	return info;
}

bool LX200::getInfo(telescope::getInfo::Request &req, telescope::getInfo::Response &res){
	// here it must be implemented all the calls to the telescope with the corresponding response
	ROS_INFO("A request for INFO has been received, sending back the status of the telescope");
	res.info = getTelescopeInfo();
	return true;
}

string LX200::getAltitud(){
	ROS_INFO("Reading Altitud from telescope");
	size_t bytes_wrote = this->serial_device->write(":GA#");
	string result = this->serial_device->read(10);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	ROS_INFO("Telescope said Altitud = %s", result.c_str());
	return result;
}

string LX200::getAzimut(){
	ROS_INFO("Reading Azimut from telescope");
	size_t bytes_wrote= this->serial_device->write(":GZ#");
	string result = this->serial_device->read(10);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	ROS_INFO("Telescope said Azimut = %s", result.c_str());
	return result;
}

string LX200::getSidereal(){
	ROS_INFO("Reading Sidereal from telescope");
	size_t bytes_wrote = this->serial_device->write(":GS#");
	string result = this->serial_device->read(10);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	ROS_INFO("Telescope said Sidereal = %s", result.c_str());
	return result;
}

//
// DEC Section
//

string LX200::readDEC(){
	ROS_INFO("Reading DEC from telescope");
	size_t bytes_wrote = this->serial_device->write(":GD#");
	string result = this->serial_device->read(10);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	ROS_INFO("Telescope said DEC = %s", result.c_str());
	return result;
}

bool LX200::writeDEC(string DEC){
	string cmd = ":Sd" + DEC + "#";
	size_t bytes_wrote = this->serial_device->write(cmd.c_str());
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	string result = this->serial_device->read(1);
	cout << "DEC Accepted?: " << result << endl;
	if (result[0] == '1'){
		return true;
		ROS_INFO("DEC %s has been accepted",DEC.c_str());
	}else{
		ROS_INFO("DEC %s has been rejected",DEC.c_str());
		return false;
	}
}

//
// RA Section
//

string LX200::readRA(){
	size_t bytes_wrote = this->serial_device->write("#:GR#");
	string result = this->serial_device->read(9);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	ROS_INFO("Telescope said RA = %s", result.c_str());
	return result;
}

bool LX200::writeRA(string RA){
	string cmd = ":Sr " + RA +"#";
	cout << "cmd : " << cmd << endl;
	size_t bytes_wrote = this->serial_device->write(cmd.c_str());
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	string result = this->serial_device->read(1);
	cout << "resultado : " <<result << endl;
	if (result[0] == '1'){
		return true;
		ROS_INFO("DEC %s has been accepted",RA.c_str());
	}else{
		ROS_INFO("DEC %s has been rejected",RA.c_str());
		return false;
	}
}

bool LX200::setSlewRate(telescope::setSlewRate::Request &req, telescope::setSlewRate::Response &res){
  	ROS_INFO("A SlewRate set has been requested: %s", req.slew.c_str());
	ROS_INFO("Sending command to telescope");
	string cmd = ":R"+req.slew + "#";
	size_t bytes_wrote = this->serial_device->write(cmd);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	res.status = getTelescopeInfo();
	ROS_INFO("setSlewRate has been finished successfully");
	return true;
}

bool LX200::setTarget(telescope::setTarget::Request &req, telescope::setTarget::Response &res){
  	ROS_INFO("A new Target has been requested: RA=%s | DEC=%s", req.RA.c_str(), req.DEC.c_str());
	ROS_INFO("Sending command to telescope");
	writeRA(req.RA);
	writeDEC(req.DEC);
	ROS_INFO("Executing selected target");
	this->serial_device->write(":MS#");
	//TODO modify this to allow better understanding
	string asdf = this->serial_device->read(200);
	cout << "asdf: " << asdf << endl;
	res.status = getTelescopeInfo();
	ROS_INFO("The new target has sent successfully to the telescope");
	return true;
}

// Due parking can't be stopped, then it is not necessary an action function, just a Service wich wait until parking has been finished.
bool LX200::Park(telescope::Park::Request &req, telescope::Park::Response &res){
  	ROS_INFO("TCS Requested to Park the telescope!");
	ROS_INFO("Sending command to telescope");
	size_t bytes_wrote = this->serial_device->write("#:hP#");
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	while( isParking() ){
		usleep(10000);
	}
	// If telescope finish the parking ,then execute the endPark()
	endPark();
	res.status = getTelescopeInfo();
	ROS_INFO("Telescope has been parked successfully");
	return true;
}

// TODO: buscar una condición en la cual la montura puede fallar en el parking!
bool LX200::isParking(){
	ROS_INFO("Checking parking state");
	cout << "Si esto fuera serial, escribiria esto para saber si terminó de parkear" << ":D#" << endl;
	this->serial_device->write(":D#");
	return false;
}

bool LX200::endPark(){
	ROS_INFO("Parking finished, sending endParking to mount");
	cout << "Si esto fuera serial, escribiria esto para saber si terminó de parkear" << ":AL#" << endl;
	this->serial_device->write(":AL#");
	return true;
}

bool LX200::stopSlewing(telescope::StopSlewing::Request &req, telescope::Park::Response &res){
	ROS_INFO("Slewing of telescope has been requested to stop!");
	this->serial_device->write(":Q#");
	ROS_INFO("Stop command has been sent to Telescope");
	res.status = getTelescopeInfo();
	return true;
}

int main(int argc, char **argv)
{
	if(argc < 2){
		cout << "You must indicate the device and the baud rate, timeout for usb is 1s by default" << endl;
	}else{
		LX200 driver = LX200(argv[1], atoi(argv[2]), 1000);
		ros::init(argc, argv, "telescope_controller");
		ros::spin();
	}
  return 0;
}
