/*
 * telescopeDriver.cpp
 *
 *  Created on: 20-05-2015
 *      Author: rosmgr
 */
//#include "Telescope.h"
#include "Celestron.h"
#include "LX200.h"

using namespace std;
int main(int argc, char **argv)
{
	if(argc < 2){
		cout << "You must indicate :\n"
				" * Driver to be used (LX200, Celestron)\n"
				" * the system device /dev/XXX\n"
				" * baud rate\n"
				" * timeout for usb, 1s by default" << endl;
	}else{
		if(string(argv[1]).compare(string("LX200")) == 0){
			ros::init(argc, argv, "LX200_telescope_controller");
			LX200 driver = LX200(argv[2], atoi(argv[3]), atoi(argv[4]));
			driver.run();
		}else if(string(argv[1]).compare(string("Celestron")) == 0){
			ros::init(argc, argv, "Celestron_telescope_controller");
			Celestron driver = Celestron(argv[2], atoi(argv[3]), 1000);
			driver.run();
		}
		//ros::spin();
	}
  return 0;
}



