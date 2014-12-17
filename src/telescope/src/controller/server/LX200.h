#include "Telescope.h"

// TODO Arreglar el polimorfismo
//class LX200: public Telescope{
class LX200 : public Telescope{
	public:
		LX200(string device, int baud_rate, int timeout);
		telescope::TelescopeInfo getTelescopeInfo();

		// INFO Section
		bool getInfo(telescope::getInfo::Request &req, telescope::getInfo::Response &res);
		string getAzimut();
		string getAltitud();
		string getSidereal();

		// DEC Section
		string readDEC();
		bool writeDEC(string DEC);

		// RA Section
		string readRA();
		bool writeRA(string RA);
		bool setRA(telescope::setRA::Request &req, telescope::setRA::Response &res);

		//Targeting section
		bool setSlewRate(telescope::setSlewRate::Request &req, telescope::setSlewRate::Response &res);
		bool setTarget(telescope::setTarget::Request &req, telescope::setTarget::Response &res);
		bool stopSlewing(telescope::StopSlewing::Request &req, telescope::Park::Response &res);

		// Parking Section
		bool Park(telescope::Park::Request &req, telescope::Park::Response &res);
		bool isParking();
		bool endPark();

	protected:
		serial::Serial* serial_device;
};
