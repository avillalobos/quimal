#ifndef TELESCOPE_H_
#define TELESCOPE_H_

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
#include "telescope/setAltitude.h"
#include "telescope/setAzimuth.h"
#include "telescope/setSlewRate.h"
#include "telescope/setEquatorialTarget.h"
#include "telescope/setAltAzimuthTarget.h"
#include "telescope/Park.h"
#include "telescope/StopSlewing.h"

using std::string;

class Telescope{
#define MAX32BIT 4294967296.0

	public:

		/**
		 * Coordinates section
		 * 1: Altitude/Azimuth section
		 */
		virtual string getAltitude() = 0;
		virtual bool setAltitude(telescope::setAltitude::Request &req, telescope::setAltitude::Response &res) = 0;
		virtual string getAzimuth() = 0;
		virtual bool setAzimuth(telescope::setAzimuth::Request &req, telescope::setAzimuth::Response &res) = 0;

		/**
		 * Coordinates section
		 * 2: RA/DEC section
		 */
		virtual string getRA() = 0;
		virtual bool setRA(telescope::setRA::Request &req, telescope::setRA::Response &res) = 0;
		virtual string getDEC() = 0;
		virtual bool setDEC(telescope::setDEC::Request &req, telescope::setDEC::Response &res) = 0;

		//#####################################################

		/**
		 * Targeting section
		 */
		virtual bool setEquatorialTarget(telescope::setEquatorialTarget::Request &req, telescope::setEquatorialTarget::Response &res) = 0;
		virtual bool setAltAzimuthTarget(telescope::setAltAzimuthTarget::Request &req, telescope::setAltAzimuthTarget::Response &res) = 0;
		virtual bool setSlewRate(telescope::setSlewRate::Request &req, telescope::setSlewRate::Response &res) = 0;
		virtual string getSlewRate() = 0;
		virtual bool stopSlewing(telescope::StopSlewing::Request &req, telescope::Park::Response &res) = 0;

		//#####################################################

		/*
		 * Info section
		 */
		virtual bool getInfo(telescope::getInfo::Request &req, telescope::getInfo::Response &res) = 0;
		virtual telescope::TelescopeInfo getTelescopeInfo() = 0;
		virtual string getSidereal() = 0;

		//#####################################################

		/*
		 * Parking section
		 */
		virtual bool Park(telescope::Park::Request &req, telescope::Park::Response &res) = 0;
		virtual bool isParking() = 0;
		virtual bool endPark() = 0;
		virtual void run() = 0;

	protected:
		serial::Serial* serial_device;
};
#endif
