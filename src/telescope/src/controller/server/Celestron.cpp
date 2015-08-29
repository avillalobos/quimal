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
	return degrees2alt_format(degrees);
}

string Celestron::degrees2alt_format(float alt_degrees){
	int degree = (int)alt_degrees;
	float minute_tmp = (alt_degrees - degree) * 60;
	int minute = (int) minute_tmp;
	float seconds = (minute_tmp - minute) * 60;
	std::ostringstream ss;
	// Asuming that we are working with the standard coordinated systems, then
	// we are in the south, and the parking position is pointing to the south, so
	// when the encoders start to modificate his data, then from 0 to 90 degrees
	// of movements we will be pointing to the south, just after moving 90 degrees
	// we will be at north.
	bool minus_sign = false;
	if(degree < 90){
		minus_sign = true;
	}else if(degree == 90){
		minus_sign = false;
		degree = 0;
	}else if(degree > 90){
		degree = 180 - degree;
		minus_sign = false;
	}

	if(minus_sign)
		ss << "-";
	else
		ss << "+";

	if(degree < 10)
		ss << "0" << degree << "º";
	else
		ss << degree << "º";
	if(minute < 10)
		ss << "0" << minute << "'";
	else
		ss << minute << "'";

	if(seconds < 10)
		ss << "0" << seconds << "\"";
	else
		ss << seconds << "\"";
	return ss.str();

}
//TODO improve the efficient, is not enough, we should get the raw hex value from the telescope
bool Celestron::setAltitude(telescope::setAltitude::Request &req, telescope::setAltitude::Response &res){
	telescope::TelescopeInfo msg;
	double alt = alt_format2degrees(req.ALTITUDE);
	double az = az_format2degrees(getAzimuth());
	msg = setAltAzimuthTarget(int_to_hex(alt),int_to_hex(az));
	res.status = msg;
	return true;
}

double Celestron::alt_format2degrees(string alt){
	char sign = alt[0];
	// this value will be always positive because we are removing the sign
	int degrees = atoi(alt.substr(1,alt.find("º")).c_str());
	// due we can have a positive or negative value, then we are adjusting it.
	if(sign == '+')
		degrees = 90 + degrees;
	alt.erase(0,alt.find("º")+1);
	int minutes = atoi(alt.substr(0,alt.find("'")).c_str());
	alt.erase(0,alt.find("'")+1);
	// the last character is removed because is a ' " ' character
	double seconds = atof(alt.substr(0,alt.length()-1).c_str());
	return degrees + (double)minutes*6 + (double)seconds*0.01;
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
	return degrees2az_format(degrees);
}

string Celestron::degrees2az_format(float az_degrees){
	bool sign = false;
	if(az_degrees < 0){
		sign= true;
		az_degrees = az_degrees * -1;
	}
	float minute_tmp = (az_degrees - (int)az_degrees) * 60;
	int minute = (int) minute_tmp;
	float seconds = (minute_tmp - minute) * 60;
	std::ostringstream ss;

	if(az_degrees < 10)
		if(sign)
			ss << "-0" << (int)az_degrees << "º";
		else
			ss << "+0" << (int)az_degrees << "º";
	else
		if(sign)
			ss << "-" << (int)az_degrees << "º";
		else
			ss << "+" << (int)az_degrees << "º";

	if(minute < 10)
		ss << "0" << (int)az_degrees << "'";
	else
		ss << minute << "'";

	if(seconds < 10)
		ss << "0" << seconds << "\"";
	else
		ss << seconds << "\"";

	return ss.str();

}

//TODO transform the coordinates into the corresponding form of the celestron protocol
bool Celestron::setAzimuth(telescope::setAzimuth::Request &req, telescope::setAzimuth::Response &res){
	telescope::TelescopeInfo msg;
	double alt = alt_format2degrees(getAltitude());
	double az = az_format2degrees(req.AZIMUTH);
	msg = setAltAzimuthTarget(int_to_hex(alt),int_to_hex(az));
	res.status = msg;
	return true;
}

double Celestron::az_format2degrees(string az){
	char sign = az[0];
	int degrees = atoi(az.substr(1,az.find("º")).c_str());
	if(sign == '+')
		degrees = 90 + degrees;
	az.erase(0,az.find("º")+1);
	int minutes = atoi(az.substr(0,az.find("'")).c_str());
	az.erase(0,az.find("'")+1);
	// the last character is removed because is a ' " ' character
	double seconds = atof(az.substr(0,az.length()-1).c_str());
	return degrees + (double)minutes*6 + (double)seconds*0.01;
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
	float* data = new float[2];
	if(result.length() == 0){
		ROS_ERROR("An empty string received");
		data[0] = -1;
		data[1] = -1;
	}

	cout << "getAltAz(): result: " << result << endl;
	// getting the Azimuth parameters from the string 'result', position 0 to 7
	//float raw_azimuth = (float) strtol(result.substr(0,8).c_str(), NULL, 16);
	int raw_azimuth = strtoul(result.substr(0,8).c_str(),0x0,16);
	float azimuth_percent = raw_azimuth / MAX32BIT;
	float azimuth_degrees = azimuth_percent * 360;
	// getting the Altitude parameters from the string 'result', position 9 to 16
	int raw_altitud = strtoul(result.substr(9,8).c_str(), NULL, 16);
	float altitude_percent = raw_altitud / MAX32BIT;
	float altitude_degrees = altitude_percent * 360;
	cout << "azimut: " << azimuth_degrees << " altitude: " << altitude_degrees << endl;
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
	ROS_INFO("Telescope said Right Ascension = %f", degrees);
	return degrees2ra_format(degrees);
}

string Celestron::degrees2ra_format(float ra_degrees){
	float hour_tmp = ra_degrees/15;
	int hour = (int) hour_tmp;
	float minute_tmp = (hour_tmp - hour) * 60;
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

// TODO Check, it is not possible send only Declination commands, but we could create it by retrieving first
// the DEC value and then send a goto with both commands, this will actually change only the RA parameter.
bool Celestron::setRA(telescope::setRA::Request &req, telescope::setRA::Response &res){
	// processing the string received into the corresponding format for celestron
	double data = ra_format2degrees(req.RA);
	int percent = data * MAX32BIT / 360;
	string final_hex = int_to_hex(percent);
	// once we send the command to the mount, we should return a telescope status
	telescope::TelescopeInfo msg;
	msg = setEquatorialTarget(final_hex, getDEC());
	res.status = msg;
	return true;
}

//TODO check if we could receive a string staring with a sign +-
// RA goes from 0 to 24 hours
double Celestron::ra_format2degrees(string ra){
	int hours = atoi(ra.substr(0,ra.find(":")).c_str());
	ra.erase(0,ra.find(":")+1);
	int minutes = atoi(ra.substr(0,ra.find(":")).c_str());
	ra.erase(0,ra.find(":")+1);
	double seconds = atof(ra.substr(0,ra.length()).c_str());
	cout << "seconds: " << seconds << endl;
	// hour, 360/24 = 15
	// minutes, 360/24*60 = 0.25, regla de 3 simples, 360 -> 24h ó 360 -> 24*60 minutos
	// seconds, 360/24*3600, regla de 3 simples, 360 -> 24*60*60 segundos.
	return hours*15 + (double)minutes/4 + (double)seconds/240;
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
	ROS_INFO("Telescope said Declination = %f", degrees);
	return degrees2dec_format(degrees);
}

string Celestron::degrees2dec_format(float dec_degrees){
	int degree = (int)dec_degrees;
	float minute_tmp = (dec_degrees - degree) * 60;
	int minute = (int) minute_tmp;
	float seconds = (minute_tmp - minute) * 60;
	std::ostringstream ss;

	bool minus_sign = false;
	if(degree < 90){
		minus_sign = true;
	}else if(degree == 90){
		minus_sign = false;
		degree = 0;
	}else if(degree > 90){
		degree = 180 - degree;
		minus_sign = false;
	}

	if(minus_sign)
		ss << "-";
	else
		ss << "+";


	if(degree < 10)
		ss << "0" << degree << ":";
	else
		ss << degree << ":";
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

// TODO Check, it is not possible send only Declination commands, but we could create it by retrieving first
// the RA value and then send a goto with both commands, this will actually change only the Declination parameter.
bool Celestron::setDEC(telescope::setDEC::Request &req, telescope::setDEC::Response &res){
	telescope::TelescopeInfo msg;
	// processing the string received into the corresponding format for celestron
	float data = dec_format2degrees(req.DEC);
	if(data == -1){
		msg.msg = "Wrong data received!";
	}
	int percent = data * MAX32BIT / 360;
	string final_hex = int_to_hex(percent);
	// once we send the command to the mount, we should return a telescope status
	msg = setEquatorialTarget(getRA(), final_hex);
	res.status = msg;
	return true;
}

// from -90 to +90, data must be validated before
double Celestron::dec_format2degrees(string dec){
	int degrees = atoi(dec.substr(0,dec.find(":")).c_str());
	if(degrees < -90 && degrees > 90)
		return -1;
	// If I receive a negative number, ie: -50, this means a rotation of 40º from
	// the 0º position, and if I receive a positive number, then this means a value
	// more than 90 degrees of rotation for the telescope axis, so we are always adding.
	degrees = 90 + degrees;
	dec.erase(0,dec.find(":")+1);
	int minutes = atoi(dec.substr(0,dec.find(":")).c_str());
	if(minutes < 0 && minutes >= 60)
		return -1;
	dec.erase(0,dec.find(":")+1);
	double seconds = atof(dec.substr(0,dec.length()).c_str());
	if(seconds < 0 and seconds >= 60)
		return -1;
	return degrees + (double)minutes/60 + (double)seconds/3600;
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
	telescope::TelescopeInfo msg;
	msg = setEquatorialTarget(req.RA, req.DEC);
	res.status = msg;
	return true;
}

telescope::TelescopeInfo Celestron::setEquatorialTarget(string RA, string DEC){
  	ROS_INFO("A new Target has been requested: RA=%s | DEC=%s", RA.c_str(), DEC.c_str());
	ROS_INFO("Sending command to telescope");
	int ra = ra_format2degrees(RA);
	int dec = dec_format2degrees(DEC);
	string cmd = "r" + int_to_hex(ra) + "," + int_to_hex(dec);
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
		ROS_INFO("moving to target position...");
		// telescope return 1 when the telescope is currently moving to the desired position and 0 when it finish
	}while(goto_progress.compare(string("1#")) != 0);
	ROS_INFO("Target position reached successfully");
	return getTelescopeInfo();
}

// TODO Check
bool Celestron::setAltAzimuthTarget(telescope::setAltAzimuthTarget::Request &req, telescope::setAltAzimuthTarget::Response &res){
	telescope::TelescopeInfo msg;
	msg = setAltAzimuthTarget(req.ALTITUDE, req.AZIMUTH);
	res.status = msg;
	return true;
}

telescope::TelescopeInfo Celestron::setAltAzimuthTarget(string Altitude, string Azimuth){
	ROS_INFO("A new Target has been requested: ALT=%s | AZ=%s", Altitude.c_str(), Azimuth.c_str());
	ROS_INFO("Sending command to telescope");
	int az = az_format2degrees(Azimuth);
	int alt = alt_format2degrees(Altitude);
	cout << "azimuth " << az << " - altitude: " << alt << endl;
	string cmd = "b" + int_to_hex(az) + "," + int_to_hex(alt);
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
		ROS_INFO("moving to target position...");
		// telescope return 1 when the telescope is currently moving to the desired position and 0 when it finish
	}while(goto_progress == "1#");
	ROS_INFO("Target position reached successfully");
	return getTelescopeInfo();
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
	info.azimuth = degrees2az_format(AltAz[0]);;
	info.altitud = degrees2alt_format(AltAz[1]);;
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
	/*
	ROS_INFO("Reading Sidereal from telescope");
	size_t bytes_wrote = this->serial_device->write(":GS#");
	string result = this->serial_device->read(10);
	ROS_INFO("Driver wrote %lu bytes", bytes_wrote);
	ROS_INFO("Telescope said Sidereal = %s", result.c_str());
	*/
	return "Not implemented";
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

string Celestron::int_to_hex(int degree_percent){
	std::stringstream stream;
	stream << std::setfill ('0') << std::setw(sizeof(int)*2)
		   << std::hex << degree_percent;
	return stream.str();
}

int Celestron::hex_to_int(string hex_value){

	return 0;
}

void Celestron::run(){
	ros::NodeHandle n;
	ros::ServiceServer get_info = n.advertiseService("getInfo", &Celestron::getInfo, this);
	ros::ServiceServer set_slewrate = n.advertiseService("setSlewRate", &Celestron::setSlewRate,this);
	ros::ServiceServer set_eqtarget = n.advertiseService("setEquatorialTarget", &Celestron::setEquatorialTarget,this);
	ros::ServiceServer set_altaztarget = n.advertiseService("setAltAzimuthTarget", &Celestron::setAltAzimuthTarget,this);
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
