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

//static serial::Serial* my_serial;
//static serial::Serial my_serial("/dev/null", 9600, serial::Timeout::simpleTimeout(1000));

/*
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
  // idealmente debería escribir la RA y DEC recibida y esperar un mensaje
  size_t bytes_wrote = my_serial->write(msg->data.c_str());
  string result = my_serial->read(msg->data.length()+1);
  cout << "result: " <<  result << endl;
}
*/

//
// Telescope Info Section
//

//LX200::LX200(string device, int baud_rate, int timeout) : Telescope::Telescope(device, baud_rate, timeout){
LX200::LX200(string device, int baud_rate, int timeout){
	this->serial_device = new serial::Serial(device, baud_rate, serial::Timeout::simpleTimeout(timeout));
/*
	ros::NodeHandle n;
        ros::ServiceServer get_info = n.advertiseService("getInfo", LX200::getInfo);
        ros::ServiceServer set_dec = n.advertiseService("setDEC", setDEC);
        ros::ServiceServer set_ra = n.advertiseService("setRA", setRA);
        ros::ServiceServer set_slewrate = n.advertiseService("setSlewRate", setSlewRate);
        ros::ServiceServer set_target = n.advertiseService("setTarget", setTarget);
        ros::ServiceServer park = n.advertiseService("Park", Park);
*/
}


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

//
// DEC Section
//

string LX200::readDEC(){
	cout << "Si esto fuera el serial, para leer el RA escribiría:" << "#:GD#" << endl;
	//my_serial->write("#:GD#")
	//string result = my_serial->read(200)
	return "+90:12:23";
}

bool LX200::writeDEC(string DEC){

}

bool LX200::setDEC(telescope::setDEC::Request &req, telescope::setDEC::Response &res){
  	ROS_INFO("A DEC set has been requested: %s", req.DEC.c_str());
	ROS_INFO("Sending command to telescope");
	res.status = getTelescopeInfo();
	ROS_INFO("setDEC has been finished successfully");
	return true;
}


string LX200::readRA(){
	cout << "Si esto fuera el serial, para leer el RA escribiría:" << "#:GR#" << endl;
        //my_serial->write("#:GR#")
        //string result = my_serial->read(200)
	return "12:23:34";
}

bool LX200::setRA(telescope::setRA::Request &req, telescope::setRA::Response &res){
  	ROS_INFO("A RA set has been requested: %s", req.RA.c_str());
	ROS_INFO("Sending command to telescope");
	res.status = getTelescopeInfo();
	ROS_INFO("setRA has been finished successfully");
	return true;
}

bool LX200::setSlewRate(telescope::setSlewRate::Request &req, telescope::setSlewRate::Response &res){
  	ROS_INFO("A SlewRate set has been requested: %s", req.slew.c_str());
	ROS_INFO("Sending command to telescope");
	res.status = getTelescopeInfo();
	ROS_INFO("setSlewRate has been finished successfully");
	return true;
}

bool LX200::setTarget(telescope::setTarget::Request &req, telescope::setTarget::Response &res){
  	ROS_INFO("A new Target has been requested: RA=%s | DEC=%s", req.RA.c_str(), req.DEC.c_str());
	ROS_INFO("Sending command to telescope");
	res.status = getTelescopeInfo();
	ROS_INFO("The new target has sent successfully to the telescope");
	return true;
}

// Due parking can't be stopped, then it is not necessary an action function, just a Service wich wait until parking has been finished.
bool LX200::Park(telescope::Park::Request &req, telescope::Park::Response &res){
  	ROS_INFO("TCS Requested to Park the telescope!");
	ROS_INFO("Sending command to telescope");
	cout << "Si esto fuera el serial, esto escribiria" << ":KA#" << endl;
	while( isParking()){
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
	return false;
}

bool LX200::endPark(){
	ROS_INFO("Parking finished, sending endParking to mount");
	cout << "Si esto fuera serial, escribiria esto para saber si terminó de parkear" << ":AL#" << endl;
}

int main(int argc, char **argv)
{

	LX200 driver = LX200("/dev/null", 9600, 1000);
	ros::init(argc, argv, "telescope_controller");
	//ros::Subscriber sub = n.subscribe("telescope_parameters", 1000, chatterCallback);
	ros::NodeHandle n;
	ros::ServiceServer get_info = n.advertiseService("getInfo", &driver.getInfo);
	ros::ServiceServer set_dec = n.advertiseService("setDEC", driver.setDEC);
	ros::ServiceServer set_ra = n.advertiseService("setRA", driver.setRA);
	ros::ServiceServer set_slewrate = n.advertiseService("setSlewRate", driver.setSlewRate);
	ros::ServiceServer set_target = n.advertiseService("setTarget", driver.setTarget);
	ros::ServiceServer park = n.advertiseService("Park", driver.Park);
/*
  my_serial = new serial::Serial("/dev/null", 9600, serial::Timeout::simpleTimeout(1000));
  cout << "Is the serial port open?";
  if(my_serial->isOpen())
    cout << " Yes." << endl;
  else{
    cout << " No." << endl;
    return 0;
  }
*/
  ros::spin();
  return 0;
}
