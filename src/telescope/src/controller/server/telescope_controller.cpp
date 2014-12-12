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

#include "ros/ros.h"
#include "std_msgs/String.h"
#include <string>
#include <iostream>
#include <cstdio>
#include <unistd.h>
#include "serial/serial.h"
#include "telescope/TelescopeInfo.h"
#include "telescope/getInfo.h"
#include "telescope/setDEC.h"
#include "telescope/setRA.h"
#include "telescope/setSlewRate.h"
#include "telescope/setTarget.h"
#include "telescope/Park.h"
#include "telescope/StopSlewing.h"

using std::string;
using std::exception;
using std::cout;
using std::cerr;
using std::endl;
using std::vector;

// Definición de funciones!
telescope::TelescopeInfo getTelescopeInfo();
bool getInfo(telescope::getInfo::Request &req, telescope::getInfo::Response &res);
string readDEC();
bool writeDEC(string DEC);
bool setDEC(telescope::setDEC::Request &req, telescope::setDEC::Response &res);
string readRA();
bool setRA(telescope::setRA::Request &req, telescope::setRA::Response &res);
bool setSlewRate(telescope::setSlewRate::Request &req, telescope::setSlewRate::Response &res);
bool setTarget(telescope::setTarget::Request &req, telescope::setTarget::Response &res);
bool Park(telescope::Park::Request &req, telescope::Park::Response &res);
bool isParking();
bool endPark();
string getAzimut();
string getAltitud();
string getSidereal();


static serial::Serial* my_serial;
//static serial::Serial my_serial("/dev/null", 9600, serial::Timeout::simpleTimeout(1000));


void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
  // idealmente debería escribir la RA y DEC recibida y esperar un mensaje
  size_t bytes_wrote = my_serial->write(msg->data.c_str());
  string result = my_serial->read(msg->data.length()+1);
  cout << "result: " <<  result << endl;
}

//
// Telescope Info Section
//

telescope::TelescopeInfo getTelescopeInfo(){
	ROS_INFO("Waiting for telescope status");
	telescope::TelescopeInfo info;
	info.RA = readRA();
	info.DEC = readDEC();
	info.Sidereal = getSidereal();
	info.azimut = getAltitud();
	info.altitud = getAzimut();
	info.slew_rate = "lentito";
	info.msg = "Atributo para enviar mensajes custom :D";
	ROS_INFO("Status retrieved successfully");
	return info;
}

bool getInfo(telescope::getInfo::Request &req, telescope::getInfo::Response &res){
	// here it must be implemented all the calls to the telescope with the corresponding response
	ROS_INFO("A request for INFO has been received, sending back the status of the telescope");
	res.info = getTelescopeInfo();
	return true;
}

string getAltitud(){
	cout << "Si esto fuera serial, para leer altitude escribiria" << ":GA#" << endl;
	size_t bytes_wrote = my_serial->write(":GA#");
	string result = my_serial->read(10);
	cout << "read from telescope: [" << bytes_wrote << "] "<< result << endl;
	return result;
}

string getAzimut(){
	cout << "Si esto fuera serial, para leer azimut escribiria" << ":GZ#" << endl;
	size_t bytes_wrote= my_serial->write(":GZ#");
	string result = my_serial->read(10);
	cout << "read from telescope: [" << bytes_wrote << "] "<< result << endl;
	return result;
}

string getSidereal(){
	cout << "Si esto fuera serial, para leer sidereal escribiria" << ":GS#" << endl;
	size_t bytes_wrote = my_serial->write(":GS#");
	string result = my_serial->read(10);
	cout << "read from telescope: [" << bytes_wrote << "] "<< result << endl;
	return result;
}

//
// DEC Section
//

string readDEC(){
	cout << "Si esto fuera el serial, para leer el DEC escribiría:" << ":GD#" << endl;
	size_t bytes_wrote = my_serial->write(":GD#");
	string result = my_serial->read(10);
	cout << "result: " << result << endl;
	return result;
}

bool writeDEC(string DEC){
	//cout << "Simulando escritura serial :Sd "<< DEC[0] << DEC[1] << DEC[2] << ":" <<DEC[4] << DEC[5] << ":" << DEC[7] << DEC[8] << "#" << endl;
	string cmd = ":Sd" + DEC + "#";
	cout << "Comando: "<< cmd << endl;
	size_t bytes_wrote = my_serial->write(cmd.c_str());
	cout << "bytes wrote" << bytes_wrote << endl;
	string result = my_serial->read(1);
	cout << "read: " << result << endl;
	if (result[0] == '1')
		return true;
	else
		return false;
}

bool setDEC(telescope::setDEC::Request &req, telescope::setDEC::Response &res){
  	ROS_INFO("A DEC set has been requested: %s", req.DEC.c_str());
	ROS_INFO("Sending command to telescope");
	writeDEC(req.DEC);
	res.status = getTelescopeInfo();
	ROS_INFO("setDEC has been finished successfully");
	return true;
}

// RA section

string readRA(){
	cout << "Si esto fuera el serial, para leer el RA escribiría:" << "#:GR#" << endl;
	my_serial->write("#:GR#");
	string result = my_serial->read(9);
	cout << "readed: " << result <<  endl;
	return result;
}

bool writeRA(string RA){
	string cmd = ":Sr " + RA +"#";
	cout << "cmd : " << cmd << endl;
	size_t bytes_wrote = my_serial->write(cmd.c_str());
	cout << "bytes wrote: " << bytes_wrote << endl;
	string result = my_serial->read(1);
	cout << "resultado : " <<result << endl;
	if (result[0] == '1')
		return true;
	else
		return false;
}

bool setRA(telescope::setRA::Request &req, telescope::setRA::Response &res){
  	ROS_INFO("A RA set has been requested: %s", req.RA.c_str());
	ROS_INFO("Sending command to telescope");
	writeRA(req.RA);
	res.status = getTelescopeInfo();
	ROS_INFO("setRA has been finished successfully");
	return true;
}

bool setSlewRate(telescope::setSlewRate::Request &req, telescope::setSlewRate::Response &res){
  	ROS_INFO("A SlewRate set has been requested: %s", req.slew.c_str());
	ROS_INFO("Sending command to telescope");
	string cmd = ":R"+req.slew + "#";
	size_t bytes_wrote = my_serial->write(cmd);
	cout << "bytes wrote: " << bytes_wrote << endl;
	res.status = getTelescopeInfo();
	ROS_INFO("setSlewRate has been finished successfully");
	return true;
}

bool setTarget(telescope::setTarget::Request &req, telescope::setTarget::Response &res){
  	ROS_INFO("A new Target has been requested: RA=%s | DEC=%s", req.RA.c_str(), req.DEC.c_str());
	ROS_INFO("Sending command to telescope");
	writeRA(req.RA);
	writeDEC(req.DEC);
	// i ghess move to selected
	my_serial->write(":MS#");
	string asdf = my_serial->read(200);
	cout << "asdf: " << asdf << endl;
	res.status = getTelescopeInfo();
	ROS_INFO("The new target has sent successfully to the telescope");
	return true;
}

// Due parking can't be stopped, then it is not necessary an action function, just a Service wich wait until parking has been finished.
bool Park(telescope::Park::Request &req, telescope::Park::Response &res){
  	ROS_INFO("TCS Requested to Park the telescope!");
	ROS_INFO("Sending command to telescope");
	cout << "Si esto fuera el serial, esto escribiria" << ":hP#" << endl;
	size_t bytes_wrote = my_serial->write("#:hP#");
	cout << "bytes wrote: " << bytes_wrote << endl;
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
bool isParking(){
	ROS_INFO("Checking parking state");
	cout << "Si esto fuera serial, escribiria esto para saber si terminó de parkear" << ":D#" << endl;
	my_serial->write(":D#");
	return false;
}

bool endPark(){
	ROS_INFO("Parking finished, sending endParking to mount");
	cout << "Si esto fuera serial, escribiria esto para saber si terminó de parkear" << ":AL#" << endl;
	my_serial->write(":AL#");
}

bool stopSlewing(telescope::StopSlewing::Request &req, telescope::Park::Response &res){
	ROS_INFO("Slewing of telescope has been requested to stop!");
	my_serial->write(":Q#");
	ROS_INFO("Stop command has been sent to Telescope");
	res.status = getTelescopeInfo();
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "telescope_controller");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("telescope_parameters", 1000, chatterCallback);

  ros::ServiceServer get_info = n.advertiseService("getInfo", getInfo);
  ros::ServiceServer set_dec = n.advertiseService("setDEC", setDEC);
  ros::ServiceServer set_ra = n.advertiseService("setRA", setRA);
  ros::ServiceServer set_slewrate = n.advertiseService("setSlewRate", setSlewRate);
  ros::ServiceServer set_target = n.advertiseService("setTarget", setTarget);
  ros::ServiceServer park = n.advertiseService("Park", Park);
  ros::ServiceServer stop = n.advertiseService("StopSlewing", stopSlewing);

  my_serial = new serial::Serial("/dev/ttyACM0", 9600, serial::Timeout::simpleTimeout(1000));
  cout << "Is the serial port open?";
  if(my_serial->isOpen())
    cout << " Yes." << endl;
  else{
    cout << " No." << endl;
    return 0;
  }

  ros::spin();
  return 0;
}
