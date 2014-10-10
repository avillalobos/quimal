/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/rosmgr/quimal/src/dome/srv/close_dome.srv
 *
 */


#ifndef DOME_MESSAGE_CLOSE_DOMERESPONSE_H
#define DOME_MESSAGE_CLOSE_DOMERESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <dome/roof.h>

namespace dome
{
template <class ContainerAllocator>
struct close_domeResponse_
{
  typedef close_domeResponse_<ContainerAllocator> Type;

  close_domeResponse_()
    : status()  {
    }
  close_domeResponse_(const ContainerAllocator& _alloc)
    : status(_alloc)  {
    }



   typedef  ::dome::roof_<ContainerAllocator>  _status_type;
  _status_type status;




  typedef boost::shared_ptr< ::dome::close_domeResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dome::close_domeResponse_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct close_domeResponse_

typedef ::dome::close_domeResponse_<std::allocator<void> > close_domeResponse;

typedef boost::shared_ptr< ::dome::close_domeResponse > close_domeResponsePtr;
typedef boost::shared_ptr< ::dome::close_domeResponse const> close_domeResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dome::close_domeResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dome::close_domeResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace dome

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/home/rosmgr/ros_catkin_ws/install_isolated/share/std_msgs/cmake/../msg'], 'dome': ['/home/rosmgr/quimal/src/dome/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::dome::close_domeResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dome::close_domeResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dome::close_domeResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dome::close_domeResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dome::close_domeResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dome::close_domeResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dome::close_domeResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cbbdd3f7c5382e7f2ae887052ce258c9";
  }

  static const char* value(const ::dome::close_domeResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xcbbdd3f7c5382e7fULL;
  static const uint64_t static_value2 = 0x2ae887052ce258c9ULL;
};

template<class ContainerAllocator>
struct DataType< ::dome::close_domeResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dome/close_domeResponse";
  }

  static const char* value(const ::dome::close_domeResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dome::close_domeResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "roof status\n\
\n\
\n\
================================================================================\n\
MSG: dome/roof\n\
float32 ubication\n\
bool sensor1\n\
bool sensor2\n\
bool sensor3\n\
";
  }

  static const char* value(const ::dome::close_domeResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dome::close_domeResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.status);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct close_domeResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dome::close_domeResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dome::close_domeResponse_<ContainerAllocator>& v)
  {
    s << indent << "status: ";
    s << std::endl;
    Printer< ::dome::roof_<ContainerAllocator> >::stream(s, indent + "  ", v.status);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DOME_MESSAGE_CLOSE_DOMERESPONSE_H