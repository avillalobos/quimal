# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "dome: 1 messages, 2 services")

set(MSG_I_FLAGS "-Idome:/home/rosmgr/quimal/src/dome/msg;-Istd_msgs:/home/rosmgr/ros_catkin_ws/install_isolated/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(dome_generate_messages ALL)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(dome
  "/home/rosmgr/quimal/src/dome/msg/roof.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dome
)

### Generating Services
_generate_srv_cpp(dome
  "/home/rosmgr/quimal/src/dome/srv/close_dome.srv"
  "${MSG_I_FLAGS}"
  "/home/rosmgr/quimal/src/dome/msg/roof.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dome
)
_generate_srv_cpp(dome
  "/home/rosmgr/quimal/src/dome/srv/open_dome.srv"
  "${MSG_I_FLAGS}"
  "/home/rosmgr/quimal/src/dome/msg/roof.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dome
)

### Generating Module File
_generate_module_cpp(dome
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dome
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(dome_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(dome_generate_messages dome_generate_messages_cpp)

# target for backward compatibility
add_custom_target(dome_gencpp)
add_dependencies(dome_gencpp dome_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dome_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(dome
  "/home/rosmgr/quimal/src/dome/msg/roof.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dome
)

### Generating Services
_generate_srv_lisp(dome
  "/home/rosmgr/quimal/src/dome/srv/close_dome.srv"
  "${MSG_I_FLAGS}"
  "/home/rosmgr/quimal/src/dome/msg/roof.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dome
)
_generate_srv_lisp(dome
  "/home/rosmgr/quimal/src/dome/srv/open_dome.srv"
  "${MSG_I_FLAGS}"
  "/home/rosmgr/quimal/src/dome/msg/roof.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dome
)

### Generating Module File
_generate_module_lisp(dome
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dome
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(dome_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(dome_generate_messages dome_generate_messages_lisp)

# target for backward compatibility
add_custom_target(dome_genlisp)
add_dependencies(dome_genlisp dome_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dome_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(dome
  "/home/rosmgr/quimal/src/dome/msg/roof.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dome
)

### Generating Services
_generate_srv_py(dome
  "/home/rosmgr/quimal/src/dome/srv/close_dome.srv"
  "${MSG_I_FLAGS}"
  "/home/rosmgr/quimal/src/dome/msg/roof.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dome
)
_generate_srv_py(dome
  "/home/rosmgr/quimal/src/dome/srv/open_dome.srv"
  "${MSG_I_FLAGS}"
  "/home/rosmgr/quimal/src/dome/msg/roof.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dome
)

### Generating Module File
_generate_module_py(dome
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dome
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(dome_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(dome_generate_messages dome_generate_messages_py)

# target for backward compatibility
add_custom_target(dome_genpy)
add_dependencies(dome_genpy dome_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS dome_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dome)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/dome
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(dome_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dome)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/dome
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(dome_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dome)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dome\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/dome
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(dome_generate_messages_py std_msgs_generate_messages_py)
