#include "Celestron.h"
using std::string;
using std::exception;
using std::cout;
using std::cerr;
using std::endl;
using std::vector;
/*
 * Celestron.cpp
 *
 *  Created on: 17-05-2015
 *      Author: Andrés Villalobos
 */

Celestron::Celestron(string device, int baud_rate, int timeout){
	this->serial_device = new serial::Serial(device, baud_rate, serial::Timeout::simpleTimeout(timeout));
	ROS_INFO("initialization complete");
}

Celestron::~Celestron(){
	delete this->serial_device;
}

/**
 * Coordinates section
 * 1: Altitude/Azimuth section
 */
// TODO Check in HW
string Celestron::getAltitude(){
	ROS_INFO("Reading Altitud from telescope");
	// from celestron protocol 1.2+, get precise AZM/ALT use the command 'z', to get regular AZM/ALT 'Z'
	// we are working only with the precise command function only
	size_t bytes_wrote = this->serial_device->write("z");
	// once we send the command, we are expecting 18 hex characters in the format: XXXXXXXX,YYYYYYYY#, where
	// X means data in hexagesimal form corresponding to Azimuth, and Y means Altitud
	string result = this->serial_device->read(18);
	// once we get the result, we need to interpret the data, so we need to translate Hex to Decimal value,
	// also we must get only the part corresponding to the Altitud (position 0 to 7) and discard the rest
	// of the message
	float number = (float)strtol(result.substr(0,8).c_str(), NULL, 16);
	// MAX32BIT = 2^32
	float percent = number / MAX32BIT;
	// the hex value returned corresponds to a fraction of the revolution around the axis
	float degrees = percent * 360;
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	ROS_INFO("Telescope said Altitud = %f", degrees);
	// transform float value into string
	std::ostringstream ss;
	ss << degrees;
	return string(ss.str());
}

bool Celestron::setAltitude(telescope::setAltitude::Request &req, telescope::setAltitude::Response &res){
	return setAltAzimuthTarget(req.ALTITUDE,getAzimuth());
}

// TODO Check in HW
string Celestron::getAzimuth(){
	ROS_INFO("Reading Azimuth from telescope");
	// from celestron protocol 1.2+, get precise AZM/ALT use the command 'z', to get regular AZM/ALT 'Z'
	// we are working only with the precise command function only
	size_t bytes_wrote = this->serial_device->write("z");
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	// once we send the command, we are expecting 18 hex characters in the format: XXXXXXXX,YYYYYYYY#, where
	// X means data in hexagesimal form corresponding to Azimuth, and Y means Altitud
	string result = this->serial_device->read(18);
	// once we get the result, we need to interpret the data, so we need to translate Hex to Decimal value,
	// also we must get only the part corresponding to the Azimuth (position 9 to 16) and discard the rest
	// of the message
	float number = (float)strtol(result.substr(9,8).c_str(), NULL, 16);
	// MAX32BIT = 2^32
	float percent = number / MAX32BIT;
	// the hex value returned corresponds to a fraction of the revolution around the axis
	float degrees = percent * 360;
	ROS_INFO("Telescope said Altitud = %f", degrees);
	// transform float value into string
	std::ostringstream ss;
	ss << degrees;
	return string(ss.str());
}

//TODO transform the coordinates into the corresponding form of the celestron protocol
bool Celestron::setAzimuth(telescope::setAzimuth::Request &req, telescope::setAzimuth::Response &res){
	return setAltAzimuthTarget(getAltitude(),req.AZIMUTH);
}

// TODO Check in HW
float* Celestron::getAltAz(){
	ROS_INFO("Reading Alt/Az from telescope");
	// from celestron protocol 1.2+, to get precise AZM/ALT use the command 'z', to get regular AZM/ALT use 'Z'
	// we are working only with the precise command function only
	size_t bytes_wrote = this->serial_device->write("z");
	// once we send the command, we are expecting 18 hex characters in the format: XXXXXXXX,YYYYYYYY#, where
	// X means data in hexagesimal form corresponding to Azimuth, and Y means Altitud
	string result = this->serial_device->read(18);
	// getting the Azimuth parameters from the string 'result', position 0 to 7
	float raw_azimuth = (float) strtol(result.substr(0,8).c_str(), NULL, 16);
	float azimuth_percent = raw_azimuth / MAX32BIT;
	float azimuth_degrees = azimuth_percent * 360;
	// getting the Altitude parameters from the string 'result', position 9 to 16
	float raw_altitud = (float)strtol(result.substr(9,8).c_str(), NULL, 16);
	float altitude_percent = raw_altitud / MAX32BIT;
	float altitude_degrees = altitude_percent * 360;
	float* data = new float[2];
	data[0] = azimuth_degrees;
	data[1] = altitude_degrees;
	return data;
}

/**
 * Coordinates section
 * 2: RA/DEC section
 */
// TODO Check with hw
string Celestron::getRA(){
	ROS_INFO("Reading RA from telescope");
	// from celestron protocol 1.2+, to get precise Declination use the command 'e', to get regular AZM/ALT use 'E'
	// we are working only with the precise command function only
	size_t bytes_wrote = this->serial_device->write("e");
	// once we send the command, we are expecting 18 hex characters in the format: XXXXXXXX,YYYYYYYY#, where
	// X means data in hexagesimal form corresponding to Right Ascension, and Y means Declination
	string result = this->serial_device->read(18);
	// once we get the result, we need to interpret the data, so we need to translate Hex to Decimal value,
	// also we must get only the part corresponding to the RA (position 0 to 7) and discard the rest
	// of the message
	int number = (int)strtol(result.substr(9,16).c_str(), NULL, 16);
	// MAX32BIT = 2^32
	float percent = number / MAX32BIT;
	// the hex value returned corresponds to a fraction of the revolution around the axis
	float degrees = percent * 360;
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	ROS_INFO("Telescope said Altitud = %f", degrees);
	// transform float value into string
	std::ostringstream ss;
	ss << degrees;
	return string(ss.str());
}

// TODO Check, it is not possible send only Declination commands, but we could create it by retrieving first
// the DEC value and then send a goto with both commands, this will actually change only the RA parameter.
bool Celestron::setRA(telescope::setRA::Request &req, telescope::setRA::Response &res){
	return setEquatorialTarget(req.RA, getDEC());
}

// TODO Check with HW
string Celestron::getDEC(){
	ROS_INFO("Reading DEC from telescope");
	// from celestron protocol 1.2+, to get precise Declination use the command 'e', to get regular AZM/ALT use 'E'
	// we are working only with the precise command function only
	size_t bytes_wrote = this->serial_device->write("e");
	// once we send the command, we are expecting 18 hex characters in the format: XXXXXXXX,YYYYYYYY#, where
	// X means data in hexagesimal form corresponding to Right Ascension, and Y means Declination
	string result = this->serial_device->read(18);
	// once we get the result, we need to interpret the data, so we need to translate Hex to Decimal value,
	// also we must get only the part corresponding to the RA (position 0 to 7) and discard the rest
	// of the message
	int number = (int)strtol(result.substr(0,7).c_str(), NULL, 16);
	// MAX32BIT = 2^32
	float percent = number / MAX32BIT;
	// the hex value returned corresponds to a fraction of the revolution around the axis
	float degrees = percent * 360;
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	ROS_INFO("Telescope said Altitud = %f", degrees);
	// transform float value into string
	std::ostringstream ss;
	ss << degrees;
	return string(ss.str());
}

// TODO Check, it is not possible send only Declination commands, but we could create it by retrieving first
// the RA value and then send a goto with both commands, this will actually change only the Declination parameter.
bool Celestron::setDEC(telescope::setDEC::Request &req, telescope::setDEC::Response &res){
	return setEquatorialTarget(getRA(), req.DEC);
}

float* Celestron::getRaDec(){
	ROS_INFO("Reading RA/DEC from telescope");
	// from celestron protocol 1.2+, to get precise AZM/ALT use the command 'e', to get regular AZM/ALT use 'E'
	// we are working only with the precise command function only
	size_t bytes_wrote = this->serial_device->write("e");
	// once we send the command, we are expecting 18 hex characters in the format: XXXXXXXX,YYYYYYYY#, where
	// X means data in hexagesimal form corresponding to RA, and Y means DEC
	string result = this->serial_device->read(18);
	// getting the Azimuth parameters from the string 'result', position 0 to 7
	float raw_ra = (float)strtol(result.substr(0,8).c_str(), NULL, 16);
	float ra_percent = raw_ra / MAX32BIT;
	float azmut_degrees = ra_percent * 360;
	// getting the DEC parameters from the string 'result', position 9 to 16
	float raw_altitud = (float)strtol(result.substr(9,8).c_str(), NULL, 16);
	float altitude_percent = raw_altitud / MAX32BIT;
	float altitude_degrees = altitude_percent * 360;
	float* data = new float[2];
	data[0] = azmut_degrees;
	data[1] = altitude_degrees;
	return data;
}

//#####################################################

/**
 * Targeting section
 */
// TODO Check
bool Celestron::setEquatorialTarget(telescope::setEquatorialTarget::Request &req, telescope::setEquatorialTarget::Response &res){
  	return setEquatorialTarget(req.RA, req.DEC);
}

bool Celestron::setEquatorialTarget(string RA, string DEC){
  	ROS_INFO("A new Target has been requested: RA=%s | DEC=%s", RA.c_str(), DEC.c_str());
	ROS_INFO("Sending command to telescope");
	string cmd = "r" + RA + "," + DEC;
	size_t bytes_wrote = this->serial_device->write(cmd);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	string answer = this->serial_device->read(1);
	ROS_INFO("Telescope is going to : RA=%s | DEC=%s", RA.c_str(), DEC.c_str());
	ROS_INFO("waiting until position is reached");
	string goto_progress = "";
	do{
		// every 5 seconds, we will check if the telescope reached the desired position
		sleep(5);
		this->serial_device->write("L");
		goto_progress = this->serial_device->read(2);
		// telescope return 1 when the telescope is currently moving to the desired position and 0 when it finish
	}while(goto_progress == "1#");
	return true;
}

// TODO Check
bool Celestron::setAltAzimuthTarget(telescope::setAltAzimuthTarget::Request &req, telescope::setAltAzimuthTarget::Response &res){
	return setAltAzimuthTarget(req.ALTITUDE, req.AZIMUTH);
}

bool Celestron::setAltAzimuthTarget(string Altitude, string Azimuth){
	ROS_INFO("A new Target has been requested: RA=%s | DEC=%s", Altitude.c_str(), Azimuth.c_str());
	ROS_INFO("Sending command to telescope");
	string cmd = "b" + Altitude + "," + Azimuth;
	size_t bytes_wrote = this->serial_device->write(cmd);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	string answer = this->serial_device->read(1);
	ROS_INFO("Telescope is going to : RA=%s | DEC=%s", Altitude.c_str(), Azimuth.c_str());
	ROS_INFO("waiting until position is reached");
	string goto_progress = "";
	do{
		// every 5 seconds, we will check if the telescope reached the desired position
		sleep(5);
		this->serial_device->write("L");
		goto_progress = this->serial_device->read(2);
		// telescope return 1 when the telescope is currently moving to the desired position and 0 when it finish
	}while(goto_progress == "1#");
	return true;
}

// TODO Check
bool Celestron::setSlewRate(telescope::setSlewRate::Request &req, telescope::setSlewRate::Response &res){
  	ROS_INFO("A SlewRate set has been requested: %s", req.slewRate.c_str());
	ROS_INFO("Sending command to telescope");
	// here we are going to use only the fixed velocity
	char slewCmd[] = { 'P', 0x02, 0x10, 0x24, 0x09, 0x00, 0x00, 0x00 };
	slewCmd[4] = atoi(req.slewRate.c_str());
	if(req.direction.compare("NORTH")){
		slewCmd[2] = 0x11; // declination
		slewCmd[3] = 0x24; // positive
	}else if(req.direction.compare("SOUTH")){
		slewCmd[2] = 0x11; // declination
		slewCmd[3] = 0x25; // negative
	} else if(req.direction.compare("EAST")){
		slewCmd[2] = 0x10; // right ascension
		slewCmd[3] = 0x25; // positive
	}else if (req.direction.compare("WEST")){
		slewCmd[2] = 0x10; // right ascension
		slewCmd[3] = 0x24; // negative
	}

	size_t bytes_wrote = this->serial_device->write(slewCmd);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	res.status = getTelescopeInfo();
	ROS_INFO("setSlewRate has been finished successfully");
	return true;
}

//TODO implement this function somehow
string Celestron::getSlewRate(){
	return "Not implemented yet";
}

// TODO not implemented yet
bool Celestron::stopSlewing(telescope::StopSlewing::Request &req, telescope::Park::Response &res){
	ROS_INFO("Slewing of telescope has been requested to stop!");
	//this->serial_device->write(":Q#");
	ROS_INFO("Stop command has been sent to Telescope");
	res.status = getTelescopeInfo();
	return true;
}

//#####################################################

/*
 * Info section
 */
bool Celestron::getInfo(telescope::getInfo::Request &req, telescope::getInfo::Response &res){
	// here it must be implemented all the calls to the telescope with the corresponding response
	ROS_INFO("A request for INFO has been received, sending back the status of the telescope");
	res.info = getTelescopeInfo();
	return true;
}

string Celestron::degrees2dec_format(float dec_degrees){
	int degree = (int)dec_degrees;
	int minute_tmp = (dec_degrees - degree) * 60;
	int minute = (int) minute_tmp;
	float seconds = (minute_tmp - minute) * 60;
	std::ostringstream ss;
	ss << degree << "º:";
	if(minute < 10)
		ss << "0" << minute << ":";
	else
		ss << minute << ":";

	if(seconds < 10)
		ss << "0" << seconds;
	else
		ss << seconds;
	return ss.str();

}

string Celestron::degrees2ra_format(float ra_degrees){
	float hour_tmp = ra_degrees/24;
	int hour = (int) hour_tmp;
	int minute_tmp = (hour_tmp - hour) * 60;
	int minute = (int) minute_tmp;
	float seconds = (minute_tmp - minute) * 60;
	std::ostringstream ss;

	if(hour < 10)
		ss << "0" << hour << ":";
	if(minute < 10)
		ss << "0" << minute << ":";
	else
		ss << minute << ":";

	if(seconds < 10)
		ss << "0" << seconds;
	else
		ss << seconds;

	return ss.str();

}

// TODO Check and improve messages
telescope::TelescopeInfo Celestron::getTelescopeInfo(){
	ROS_INFO("Waiting for telescope status");
	telescope::TelescopeInfo info;
	float* RaDec = getRaDec();
	info.RA = degrees2ra_format(RaDec[0]);
	info.DEC = degrees2dec_format(RaDec[1]);
	info.Sidereal = getSidereal();
	// Section related with the Altitude Azimuth parameter.
	float *AltAz = getAltAz();
	std::ostringstream ss;
	ss << AltAz[0];
	info.azimuth = ss.str();
	ss.str("");
	ss << AltAz[1];
	info.altitud = ss.str();
	//TODO implement the getSlewRate()
	info.slew_rate = getSlewRate();
	// Any error message or status should be here
	info.msg = "Atributo para enviar mensajes custom :D";
	ROS_INFO("Status retrieved successfully");
	delete AltAz;
	return info;
}

// TODO Check
string Celestron::getSidereal(){
	ROS_INFO("Reading Sidereal from telescope");
	size_t bytes_wrote = this->serial_device->write(":GS#");
	string result = this->serial_device->read(10);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	ROS_INFO("Telescope said Sidereal = %s", result.c_str());
	return result;
}

//#####################################################

/*
 * Parking section
 */
// TODO Check
// Due parking can't be stopped, then it is not necessary an action function, just a Service wich wait until parking has been finished.
bool Celestron::Park(telescope::Park::Request &req, telescope::Park::Response &res){
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

// TODO Check
// TODO: buscar una condición en la cual la montura puede fallar en el parking!
bool Celestron::isParking(){
	ROS_INFO("Checking parking state");
	cout << "Si esto fuera serial, escribiria esto para saber si terminó de parkear" << ":D#" << endl;
	this->serial_device->write(":D#");
	return false;
}

// TODO Check
bool Celestron::endPark(){
	ROS_INFO("Parking finished, sending endParking to mount");
	cout << "Si esto fuera serial, escribiria esto para saber si terminó de parkear" << ":AL#" << endl;
	this->serial_device->write(":AL#");
	return true;
}

void Celestron::run(){
	ros::NodeHandle n;
	ros::ServiceServer get_info = n.advertiseService("getInfo", &Celestron::getInfo, this);
	ros::ServiceServer set_slewrate = n.advertiseService("setSlewRate", &Celestron::setSlewRate,this);
	ros::ServiceServer set_target = n.advertiseService("setEquatorialTarget", &Celestron::setEquatorialTarget,this);
	ros::ServiceServer park = n.advertiseService("Park", &Celestron::Park,this);
	ros::ServiceServer stop = n.advertiseService("StopSlewing", &Celestron::stopSlewing,this);
	ros::ServiceServer setaltitude = n.advertiseService("setAltitude", &Celestron::setAltitude,this);
	ros::ServiceServer setazimuth = n.advertiseService("setAzimuth", &Celestron::setAzimuth,this);
	ros::ServiceServer setra = n.advertiseService("setRA", &Celestron::setRA,this);
	ros::ServiceServer setdec = n.advertiseService("setDEC", &Celestron::setDEC,this);
	ros::spin();
}

/*
int main(int argc, char **argv)
{
	if(argc < 2){
		cout << "You must indicate the device and the baud rate, timeout for usb is 1s by default" << endl;
	}else{
		Celestron driver = Celestron(argv[1], atoi(argv[2]), 1000);
		ros::init(argc, argv, "telescope_controller");
		ros::spin();
	}
  return 0;
}
*/
