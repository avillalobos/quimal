#ifndef LX200_H_
#define LX200_H_

#include "Telescope.h"

// TODO Arreglar el polimorfismo
//class LX200: public Telescope{
class LX200 : public Telescope{
	public:
		LX200(string device, int baud_rate, int timeout);
		~LX200();
		/**
		 * Coordinates section
		 * 1: Altitude/Azimuth section
		 */
		string getAltitude();
		bool setAltitude(telescope::setAltitude::Request &req, telescope::setAltitude::Response &res);
		string getAzimuth();
		bool setAzimuth(telescope::setAzimuth::Request &req, telescope::setAzimuth::Response &res);

		/**
		 * Coordinates section
		 * 2: RA/DEC section
		 */
		string getRA();
		bool setRA(telescope::setRA::Request &req, telescope::setRA::Response &res);
		bool setRA(string RA);
		string getDEC();
		bool setDEC(telescope::setDEC::Request &req, telescope::setDEC::Response &res);
		bool setDEC(string DEC);

		//#####################################################

		/**
		 * Targeting section
		 */
		bool setEquatorialTarget(telescope::setEquatorialTarget::Request &req, telescope::setEquatorialTarget::Response &res);
		bool setAltAzimuthTarget(telescope::setAltAzimuthTarget::Request &req, telescope::setAltAzimuthTarget::Response &res);
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
#endif
