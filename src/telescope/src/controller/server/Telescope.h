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

class Telescope{
	public:

		virtual ~Telescope() = 0;
		virtual telescope::TelescopeInfo getTelescopeInfo() = 0;

		/**
		 * Gather all the necessary information related with the telescope
		 */
		virtual bool getInfo(telescope::getInfo::Request &req, telescope::getInfo::Response &res) = 0;
		virtual string getAzimut() = 0;
		virtual string getAltitud() = 0;
		virtual string getSidereal() = 0;

		// DEC Section
		virtual string readDEC() = 0;
		virtual bool writeDEC(string DEC) = 0;

		// RA Section
		virtual string readRA() = 0;
		virtual bool writeRA(string RA) = 0;

		//Targeting section
		virtual bool setSlewRate(telescope::setSlewRate::Request &req, telescope::setSlewRate::Response &res) = 0;
		virtual bool setTarget(telescope::setTarget::Request &req, telescope::setTarget::Response &res) = 0;
		virtual bool stopSlewing(telescope::StopSlewing::Request &req, telescope::Park::Response &res) = 0;

		// Parking Section
		virtual bool Park(telescope::Park::Request &req, telescope::Park::Response &res) = 0;
		virtual bool isParking() = 0;
		virtual bool endPark() = 0;
	protected:
		serial::Serial* serial_device;
};
