# generated from catkin/cmake/template/pkgConfig.cmake.in

# append elements to a list and remove existing duplicates from the list
# copied from catkin/cmake/list_append_deduplicate.cmake to keep pkgConfig
# self contained
macro(_list_append_deduplicate listname)
  if(NOT "${ARGN}" STREQUAL "")
    if(${listname})
      list(REMOVE_ITEM ${listname} ${ARGN})
    endif()
    list(APPEND ${listname} ${ARGN})
  endif()
endmacro()

# append elements to a list if they are not already in the list
# copied from catkin/cmake/list_append_unique.cmake to keep pkgConfig
# self contained
macro(_list_append_unique listname)
  foreach(_item ${ARGN})
    list(FIND ${listname} ${_item} _index)
    if(_index EQUAL -1)
      list(APPEND ${listname} ${_item})
    endif()
  endforeach()
endmacro()

# pack a list of libraries with optional build configuration keywords
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_pack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  set(_argn ${ARGN})
  list(LENGTH _argn _count)
  set(_index 0)
  while(${_index} LESS ${_count})
    list(GET _argn ${_index} lib)
    if("${lib}" MATCHES "^debug|optimized|general$")
      math(EXPR _index "${_index} + 1")
      if(${_index} EQUAL ${_count})
        message(FATAL_ERROR "_pack_libraries_with_build_configuration() the list of libraries '${ARGN}' ends with '${lib}' which is a build configuration keyword and must be followed by a library")
      endif()
      list(GET _argn ${_index} library)
      list(APPEND ${VAR} "${lib}${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}${library}")
    else()
      list(APPEND ${VAR} "${lib}")
    endif()
    math(EXPR _index "${_index} + 1")
  endwhile()
endmacro()

# unpack a list of libraries with optional build configuration keyword prefixes
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_unpack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  foreach(lib ${ARGN})
    string(REGEX REPLACE "^(debug|optimized|general)${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}(.+)$" "\\1;\\2" lib "${lib}")
    list(APPEND ${VAR} "${lib}")
  endforeach()
endmacro()


if(dome_CONFIG_INCLUDED)
  return()
endif()
set(dome_CONFIG_INCLUDED TRUE)

# set variables for source/devel/install prefixes
if("TRUE" STREQUAL "TRUE")
  set(dome_SOURCE_PREFIX /home/rosmgr/quimal/src/dome)
  set(dome_DEVEL_PREFIX /home/rosmgr/quimal/devel)
  set(dome_INSTALL_PREFIX "")
  set(dome_PREFIX ${dome_DEVEL_PREFIX})
else()
  set(dome_SOURCE_PREFIX "")
  set(dome_DEVEL_PREFIX "")
  set(dome_INSTALL_PREFIX /home/rosmgr/quimal/install)
  set(dome_PREFIX ${dome_INSTALL_PREFIX})
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "WARNING: package 'dome' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  message("${_msg}")
endif()

# flag project as catkin-based to distinguish if a find_package()-ed project is a catkin project
set(dome_FOUND_CATKIN_PROJECT TRUE)

if(NOT "/home/rosmgr/quimal/devel/include" STREQUAL "")
  set(dome_INCLUDE_DIRS "")
  set(_include_dirs "/home/rosmgr/quimal/devel/include")
  foreach(idir ${_include_dirs})
    if(IS_ABSOLUTE ${idir} AND IS_DIRECTORY ${idir})
      set(include ${idir})
    elseif("${idir}" STREQUAL "include")
      get_filename_component(include "${dome_DIR}/../../../include" ABSOLUTE)
      if(NOT IS_DIRECTORY ${include})
        message(FATAL_ERROR "Project 'dome' specifies '${idir}' as an include dir, which is not found.  It does not exist in '${include}'.  Ask the maintainer 'rosmgr <rosmgr@todo.todo>' to fix it.")
      endif()
    else()
      message(FATAL_ERROR "Project 'dome' specifies '${idir}' as an include dir, which is not found.  It does neither exist as an absolute directory nor in '/home/rosmgr/quimal/src/dome/${idir}'.  Ask the maintainer 'rosmgr <rosmgr@todo.todo>' to fix it.")
    endif()
    _list_append_unique(dome_INCLUDE_DIRS ${include})
  endforeach()
endif()

set(libraries "")
foreach(library ${libraries})
  # keep build configuration keywords, target names and absolute libraries as-is
  if("${library}" MATCHES "^debug|optimized|general$")
    list(APPEND dome_LIBRARIES ${library})
  elseif(TARGET ${library})
    list(APPEND dome_LIBRARIES ${library})
  elseif(IS_ABSOLUTE ${library})
    list(APPEND dome_LIBRARIES ${library})
  else()
    set(lib_path "")
    set(lib "${library}-NOTFOUND")
    # since the path where the library is found is returned we have to iterate over the paths manually
<<<<<<< HEAD
    foreach(path /home/rosmgr/quimal/devel/lib;/home/rosmgr/quimal/devel/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/move_base/lib;/home/rosmgr/ros_catkin_ws/install_isolated/lib)
=======
    foreach(path /home/rosmgr/quimal/devel/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/image_transport/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/message_filters/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/diagnostic_updater/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/diagnostic_aggregator/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosout/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/nodelet/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/kobuki_keyop/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/dynamic_reconfigure/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/bondcpp/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/roscpp/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/xmlrpcpp/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/tf2/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/tf2_msgs/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/std_srvs/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/sensor_msgs/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosgraph_msgs/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/nav_msgs/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/kobuki_msgs/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/geometry_msgs/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/diagnostic_msgs/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/bond/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/actionlib_msgs/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/std_msgs/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/smclib/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rostest/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/pluginlib/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosconsole/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosunit/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/roslaunch/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosbag_storage/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/roscpp_serialization/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rostime/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosservice/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rospy/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosparam/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/roslib/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rospack/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosmsg/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosmaster/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosmake/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/roslang/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosgraph/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/roscreate/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/roscpp_traits/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosclean/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosbuild/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosboost_cfg/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/rosbash/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ros_comm/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ros/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/mk/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/message_runtime/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/message_generation/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/kobuki_ftdi/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/kobuki_driver/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/image_publisher/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_streams/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_sigslots/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_devices/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_threads/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_mobile_robot/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_geometry/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_containers/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_utilities/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_math/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_linear_algebra/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_formatters/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_converters/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_concepts/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_type_traits/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_time/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_time_lite/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_mpl/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_exceptions/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_errors/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_eigen/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_config/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_command_line/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_build/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/ecl_license/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/cpp_common/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/class_loader/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/angles/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/genpy/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/genlisp/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/gencpp/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/genmsg/lib;/home/rosmgr/ros_catkin_ws/devel_isolated/catkin/lib;/home/rosmgr/quimal/devel/lib;/home/rosmgr/ros_catkin_ws/install_isolated/lib)
>>>>>>> b316416f9c5a00b678fe48214420205e24e6a35d
      find_library(lib ${library}
        PATHS ${path}
        NO_DEFAULT_PATH NO_CMAKE_FIND_ROOT_PATH)
      if(lib)
        set(lib_path ${path})
        break()
      endif()
    endforeach()
    if(lib)
      _list_append_unique(dome_LIBRARY_DIRS ${lib_path})
      list(APPEND dome_LIBRARIES ${lib})
    else()
      # as a fall back for non-catkin libraries try to search globally
      find_library(lib ${library})
      if(NOT lib)
        message(FATAL_ERROR "Project '${PROJECT_NAME}' tried to find library '${library}'.  The library is neither a target nor built/installed properly.  Did you compile project 'dome'?  Did you find_package() it before the subdirectory containing its code is included?")
      endif()
      list(APPEND dome_LIBRARIES ${lib})
    endif()
  endif()
endforeach()

set(dome_EXPORTED_TARGETS "dome_generate_messages_cpp;dome_generate_messages_lisp;dome_generate_messages_py")
# create dummy targets for exported code generation targets to make life of users easier
foreach(t ${dome_EXPORTED_TARGETS})
  if(NOT TARGET ${t})
    add_custom_target(${t})
  endif()
endforeach()

set(depends "message_runtime")
foreach(depend ${depends})
  string(REPLACE " " ";" depend_list ${depend})
  # the package name of the dependency must be kept in a unique variable so that it is not overwritten in recursive calls
  list(GET depend_list 0 dome_dep)
  list(LENGTH depend_list count)
  if(${count} EQUAL 1)
    # simple dependencies must only be find_package()-ed once
    if(NOT ${dome_dep}_FOUND)
      find_package(${dome_dep} REQUIRED)
    endif()
  else()
    # dependencies with components must be find_package()-ed again
    list(REMOVE_AT depend_list 0)
    find_package(${dome_dep} REQUIRED ${depend_list})
  endif()
  _list_append_unique(dome_INCLUDE_DIRS ${${dome_dep}_INCLUDE_DIRS})

  # merge build configuration keywords with library names to correctly deduplicate
  _pack_libraries_with_build_configuration(dome_LIBRARIES ${dome_LIBRARIES})
  _pack_libraries_with_build_configuration(_libraries ${${dome_dep}_LIBRARIES})
  _list_append_deduplicate(dome_LIBRARIES ${_libraries})
  # undo build configuration keyword merging after deduplication
  _unpack_libraries_with_build_configuration(dome_LIBRARIES ${dome_LIBRARIES})

  _list_append_unique(dome_LIBRARY_DIRS ${${dome_dep}_LIBRARY_DIRS})
  list(APPEND dome_EXPORTED_TARGETS ${${dome_dep}_EXPORTED_TARGETS})
endforeach()

set(pkg_cfg_extras "dome-msg-extras.cmake")
foreach(extra ${pkg_cfg_extras})
  if(NOT IS_ABSOLUTE ${extra})
    set(extra ${dome_DIR}/${extra})
  endif()
  include(${extra})
endforeach()
