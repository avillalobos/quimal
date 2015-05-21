#include "Telescope.h"
#include <stdlib.h>
/*
 * Celestron.h
 *
 *  Created on: 17-05-2015
 *      Author: Andrés Villalobos
 */

#ifndef CELESTRON_H_
#define CELESTRON_H_

class Celestron : public Telescope{
	public:
		Celestron(string device, int baud_rate, int timeout);
		~Celestron();
		/**
		 * Coordinates section
		 * 1: Altitude/Azimuth section
		 */
		string getAltitude();
		bool setAltitude(telescope::setAltitude::Request &req, telescope::setAltitude::Response &res);
		string getAzimuth();
		bool setAzimuth(telescope::setAzimuth::Request &req, telescope::setAzimuth::Response &res);
		float* getAltAz();

		/**
		 * Coordinates section
		 * 2: RA/DEC section
		 */
		string getRA();
		bool setRA(telescope::setRA::Request &req, telescope::setRA::Response &res);
		string getDEC();
		bool setDEC(telescope::setDEC::Request &req, telescope::setDEC::Response &res);
		float* getRaDec();
		string degrees2dec_format(float dec_degrees);
		string degrees2ra_format(float ra_degrees);
		float dec_format2degrees(string dec);
		float ra_format2degrees(string ra);

		//#####################################################

		/**
		 * Targeting section
		 */
		bool setEquatorialTarget(telescope::setEquatorialTarget::Request &req, telescope::setEquatorialTarget::Response &res);
		bool setEquatorialTarget(string RA, string DEC);
		bool setAltAzimuthTarget(telescope::setAltAzimuthTarget::Request &req, telescope::setAltAzimuthTarget::Response &res);
		bool setAltAzimuthTarget(string Altitude, string Azimuth);
		bool setSlewRate(telescope::setSlewRate::Request &req, telescope::setSlewRate::Response &res);
		string getSlewRate();
		bool stopSlewing(telescope::StopSlewing::Request &req, telescope::Park::Response &res);

		//#####################################################

		/*
		 * Info section
		 */
		bool getInfo(telescope::getInfo::Request &req, telescope::getInfo::Response &res);
		telescope::TelescopeInfo getTelescopeInfo();
		string getSidereal();

		//#####################################################

		/*
		 * Parking section
		 */
		bool Park(telescope::Park::Request &req, telescope::Park::Response &res);
		bool isParking();
		bool endPark();
		void run();

	protected:
		serial::Serial* serial_device;
};

#endif /* CELESTRON_H_ */
