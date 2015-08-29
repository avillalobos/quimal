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
		string degrees2alt_format(float alt_degrees);
		bool setAltitude(telescope::setAltitude::Request &req, telescope::setAltitude::Response &res);
		double alt_format2degrees(string alt);
		string getAzimuth();
		string degrees2az_format(float az_degrees);
		bool setAzimuth(telescope::setAzimuth::Request &req, telescope::setAzimuth::Response &res);
		double az_format2degrees(string az);
		float* getAltAz();

		/**
		 * Coordinates section
		 * 2: RA/DEC section
		 */
		string getRA();
		string degrees2ra_format(float ra_degrees);
		bool setRA(telescope::setRA::Request &req, telescope::setRA::Response &res);
		double ra_format2degrees(string ra);
		string getDEC();
		string degrees2dec_format(float dec_degrees);
		bool setDEC(telescope::setDEC::Request &req, telescope::setDEC::Response &res);
		double dec_format2degrees(string dec);
		float* getRaDec();

		//#####################################################

		/**
		 * Targeting section
		 */
		bool setEquatorialTarget(telescope::setEquatorialTarget::Request &req, telescope::setEquatorialTarget::Response &res);
		telescope::TelescopeInfo setEquatorialTarget(string RA, string DEC);
		bool setAltAzimuthTarget(telescope::setAltAzimuthTarget::Request &req, telescope::setAltAzimuthTarget::Response &res);
		telescope::TelescopeInfo setAltAzimuthTarget(string Altitude, string Azimuth);
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
		string int_to_hex(int degree_percent);
		int hex_to_int(string hex_value);

	protected:
		serial::Serial* serial_device;
};

#endif /* CELESTRON_H_ */
