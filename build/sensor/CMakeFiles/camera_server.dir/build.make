# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/rosmgr/quimal/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/rosmgr/quimal/build

# Include any dependencies generated for this target.
include sensor/CMakeFiles/camera_server.dir/depend.make

# Include the progress variables for this target.
include sensor/CMakeFiles/camera_server.dir/progress.make

# Include the compile flags for this target's objects.
include sensor/CMakeFiles/camera_server.dir/flags.make

sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o: sensor/CMakeFiles/camera_server.dir/flags.make
sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o: /home/rosmgr/quimal/src/sensor/src/controller/camera_server.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/rosmgr/quimal/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o"
	cd /home/rosmgr/quimal/build/sensor && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o -c /home/rosmgr/quimal/src/sensor/src/controller/camera_server.cpp

sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.i"
	cd /home/rosmgr/quimal/build/sensor && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/rosmgr/quimal/src/sensor/src/controller/camera_server.cpp > CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.i

sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.s"
	cd /home/rosmgr/quimal/build/sensor && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/rosmgr/quimal/src/sensor/src/controller/camera_server.cpp -o CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.s

sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o.requires:
.PHONY : sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o.requires

sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o.provides: sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o.requires
	$(MAKE) -f sensor/CMakeFiles/camera_server.dir/build.make sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o.provides.build
.PHONY : sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o.provides

sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o.provides.build: sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o

# Object files for target camera_server
camera_server_OBJECTS = \
"CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o"

# External object files for target camera_server
camera_server_EXTERNAL_OBJECTS =

/home/rosmgr/quimal/devel/lib/sensor/camera_server: sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o
/home/rosmgr/quimal/devel/lib/sensor/camera_server: sensor/CMakeFiles/camera_server.dir/build.make
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libcv_bridge.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_calib3d.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_contrib.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_core.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_features2d.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_flann.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_gpu.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_highgui.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_imgproc.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_legacy.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_ml.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_nonfree.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_objdetect.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_photo.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_stitching.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_superres.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_video.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libopencv_videostab.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libimage_transport.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libmessage_filters.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/x86_64-linux-gnu/libtinyxml.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libclass_loader.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/libPocoFoundation.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/x86_64-linux-gnu/libdl.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libroslib.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libroscpp.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/librosconsole.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/librosconsole_log4cxx.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/librosconsole_backend_interface.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/liblog4cxx.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libxmlrpcpp.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libroscpp_serialization.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/librostime.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libcpp_common.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: /home/rosmgr/ros_catkin_ws/install_isolated/lib/libconsole_bridge.so
/home/rosmgr/quimal/devel/lib/sensor/camera_server: sensor/CMakeFiles/camera_server.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable /home/rosmgr/quimal/devel/lib/sensor/camera_server"
	cd /home/rosmgr/quimal/build/sensor && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/camera_server.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sensor/CMakeFiles/camera_server.dir/build: /home/rosmgr/quimal/devel/lib/sensor/camera_server
.PHONY : sensor/CMakeFiles/camera_server.dir/build

sensor/CMakeFiles/camera_server.dir/requires: sensor/CMakeFiles/camera_server.dir/src/controller/camera_server.cpp.o.requires
.PHONY : sensor/CMakeFiles/camera_server.dir/requires

sensor/CMakeFiles/camera_server.dir/clean:
	cd /home/rosmgr/quimal/build/sensor && $(CMAKE_COMMAND) -P CMakeFiles/camera_server.dir/cmake_clean.cmake
.PHONY : sensor/CMakeFiles/camera_server.dir/clean

sensor/CMakeFiles/camera_server.dir/depend:
	cd /home/rosmgr/quimal/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/rosmgr/quimal/src /home/rosmgr/quimal/src/sensor /home/rosmgr/quimal/build /home/rosmgr/quimal/build/sensor /home/rosmgr/quimal/build/sensor/CMakeFiles/camera_server.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sensor/CMakeFiles/camera_server.dir/depend

