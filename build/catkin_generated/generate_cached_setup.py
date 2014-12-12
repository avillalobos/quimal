from __future__ import print_function
import argparse
import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/home/rosmgr/ros_catkin_ws/install_isolated/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/home/rosmgr/ros_catkin_ws/install_isolated/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
<<<<<<< HEAD
    for workspace in "/home/rosmgr/quimal/devel;/home/rosmgr/ros_catkin_ws/devel_isolated/move_base;/home/rosmgr/ros_catkin_ws/install_isolated".split(';'):
=======
    for workspace in "/home/rosmgr/ros_catkin_ws/devel_isolated/image_transport;/home/rosmgr/ros_catkin_ws/devel_isolated/message_filters;/home/rosmgr/ros_catkin_ws/devel_isolated/diagnostic_updater;/home/rosmgr/ros_catkin_ws/devel_isolated/diagnostic_aggregator;/home/rosmgr/ros_catkin_ws/devel_isolated/rosout;/home/rosmgr/ros_catkin_ws/devel_isolated/nodelet;/home/rosmgr/ros_catkin_ws/devel_isolated/kobuki_keyop;/home/rosmgr/ros_catkin_ws/devel_isolated/dynamic_reconfigure;/home/rosmgr/ros_catkin_ws/devel_isolated/bondcpp;/home/rosmgr/ros_catkin_ws/devel_isolated/roscpp;/home/rosmgr/ros_catkin_ws/devel_isolated/xmlrpcpp;/home/rosmgr/ros_catkin_ws/devel_isolated/tf2;/home/rosmgr/ros_catkin_ws/devel_isolated/tf2_msgs;/home/rosmgr/ros_catkin_ws/devel_isolated/std_srvs;/home/rosmgr/ros_catkin_ws/devel_isolated/sensor_msgs;/home/rosmgr/ros_catkin_ws/devel_isolated/rosgraph_msgs;/home/rosmgr/ros_catkin_ws/devel_isolated/nav_msgs;/home/rosmgr/ros_catkin_ws/devel_isolated/kobuki_msgs;/home/rosmgr/ros_catkin_ws/devel_isolated/geometry_msgs;/home/rosmgr/ros_catkin_ws/devel_isolated/diagnostic_msgs;/home/rosmgr/ros_catkin_ws/devel_isolated/bond;/home/rosmgr/ros_catkin_ws/devel_isolated/actionlib_msgs;/home/rosmgr/ros_catkin_ws/devel_isolated/std_msgs;/home/rosmgr/ros_catkin_ws/devel_isolated/smclib;/home/rosmgr/ros_catkin_ws/devel_isolated/rostest;/home/rosmgr/ros_catkin_ws/devel_isolated/pluginlib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosconsole;/home/rosmgr/ros_catkin_ws/devel_isolated/rosunit;/home/rosmgr/ros_catkin_ws/devel_isolated/roslaunch;/home/rosmgr/ros_catkin_ws/devel_isolated/rosbag_storage;/home/rosmgr/ros_catkin_ws/devel_isolated/roscpp_serialization;/home/rosmgr/ros_catkin_ws/devel_isolated/rostime;/home/rosmgr/ros_catkin_ws/devel_isolated/rosservice;/home/rosmgr/ros_catkin_ws/devel_isolated/rospy;/home/rosmgr/ros_catkin_ws/devel_isolated/rosparam;/home/rosmgr/ros_catkin_ws/devel_isolated/roslib;/home/rosmgr/ros_catkin_ws/devel_isolated/rospack;/home/rosmgr/ros_catkin_ws/devel_isolated/rosmsg;/home/rosmgr/ros_catkin_ws/devel_isolated/rosmaster;/home/rosmgr/ros_catkin_ws/devel_isolated/rosmake;/home/rosmgr/ros_catkin_ws/devel_isolated/roslang;/home/rosmgr/ros_catkin_ws/devel_isolated/rosgraph;/home/rosmgr/ros_catkin_ws/devel_isolated/roscreate;/home/rosmgr/ros_catkin_ws/devel_isolated/roscpp_traits;/home/rosmgr/ros_catkin_ws/devel_isolated/rosclean;/home/rosmgr/ros_catkin_ws/devel_isolated/rosbuild;/home/rosmgr/ros_catkin_ws/devel_isolated/rosboost_cfg;/home/rosmgr/ros_catkin_ws/devel_isolated/rosbash;/home/rosmgr/ros_catkin_ws/devel_isolated/ros_comm;/home/rosmgr/ros_catkin_ws/devel_isolated/ros;/home/rosmgr/ros_catkin_ws/devel_isolated/mk;/home/rosmgr/ros_catkin_ws/devel_isolated/message_runtime;/home/rosmgr/ros_catkin_ws/devel_isolated/message_generation;/home/rosmgr/ros_catkin_ws/devel_isolated/kobuki_ftdi;/home/rosmgr/ros_catkin_ws/devel_isolated/kobuki_driver;/home/rosmgr/ros_catkin_ws/devel_isolated/image_publisher;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_streams;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_sigslots;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_devices;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_threads;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_mobile_robot;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_geometry;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_containers;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_utilities;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_math;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_linear_algebra;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_formatters;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_converters;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_concepts;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_type_traits;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_time;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_time_lite;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_mpl;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_exceptions;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_errors;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_eigen;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_config;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_command_line;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_build;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_license;/home/rosmgr/ros_catkin_ws/devel_isolated/cpp_common;/home/rosmgr/ros_catkin_ws/devel_isolated/class_loader;/home/rosmgr/ros_catkin_ws/devel_isolated/angles;/home/rosmgr/ros_catkin_ws/devel_isolated/genpy;/home/rosmgr/ros_catkin_ws/devel_isolated/genlisp;/home/rosmgr/ros_catkin_ws/devel_isolated/gencpp;/home/rosmgr/ros_catkin_ws/devel_isolated/genmsg;/home/rosmgr/ros_catkin_ws/devel_isolated/catkin;/home/rosmgr/quimal/devel;/home/rosmgr/ros_catkin_ws/install_isolated".split(';'):
>>>>>>> b316416f9c5a00b678fe48214420205e24e6a35d
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/rosmgr/quimal/devel/env.sh')

output_filename = '/home/rosmgr/quimal/build/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    #print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
