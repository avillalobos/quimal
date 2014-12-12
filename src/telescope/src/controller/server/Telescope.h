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

using std::string;
/*
class Telescope{
	public:
		Telescope(string device, int baud_rate, int timeout);
		virtual telescope::TelescopeInfo getTelescopeInfo();
		
		virtual bool getInfo(telescope::getInfo::Request &req, telescope::getInfo::Response &res);
		// DEC Section
		virtual string readDEC();
		virtual bool writeDEC(string DEC);
		virtual bool setDEC(telescope::setDEC::Request &req, telescope::setDEC::Response &res);
		// RA Section
		virtual string readRA();
		virtual bool writeRA(string RA);
		virtual bool setRA(telescope::setRA::Request &req, telescope::setRA::Response &res);
		//Targeting section
		virtual bool setSlewRate(telescope::setSlewRate::Request &req, telescope::setSlewRate::Response &res);
		virtual bool setTarget(telescope::setTarget::Request &req, telescope::setTarget::Response &res);
		// Parking Section
		virtual bool Park(telescope::Park::Request &req, telescope::Park::Response &res);
		virtual bool isParking();
		virtual bool endPark();
	protected:
		serial::Serial* serial_device;
};
*/
