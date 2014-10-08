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
 * Auto-generated by gensrv_cpp from file /home/rosmgr/quimal/src/dome/srv/open_dome.srv
 *
 */


#ifndef DOME_MESSAGE_OPEN_DOME_H
#define DOME_MESSAGE_OPEN_DOME_H

#include <ros/service_traits.h>


#include <dome/open_domeRequest.h>
#include <dome/open_domeResponse.h>


namespace dome
{

struct open_dome
{

typedef open_domeRequest Request;
typedef open_domeResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct open_dome
} // namespace dome


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::dome::open_dome > {
  static const char* value()
  {
    return "6b2cf0726d295207cb0af1ee517cbebb";
  }

  static const char* value(const ::dome::open_dome&) { return value(); }
};

template<>
struct DataType< ::dome::open_dome > {
  static const char* value()
  {
    return "dome/open_dome";
  }

  static const char* value(const ::dome::open_dome&) { return value(); }
};


// service_traits::MD5Sum< ::dome::open_domeRequest> should match 
// service_traits::MD5Sum< ::dome::open_dome > 
template<>
struct MD5Sum< ::dome::open_domeRequest>
{
  static const char* value()
  {
    return MD5Sum< ::dome::open_dome >::value();
  }
  static const char* value(const ::dome::open_domeRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::dome::open_domeRequest> should match 
// service_traits::DataType< ::dome::open_dome > 
template<>
struct DataType< ::dome::open_domeRequest>
{
  static const char* value()
  {
    return DataType< ::dome::open_dome >::value();
  }
  static const char* value(const ::dome::open_domeRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::dome::open_domeResponse> should match 
// service_traits::MD5Sum< ::dome::open_dome > 
template<>
struct MD5Sum< ::dome::open_domeResponse>
{
  static const char* value()
  {
    return MD5Sum< ::dome::open_dome >::value();
  }
  static const char* value(const ::dome::open_domeResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::dome::open_domeResponse> should match 
// service_traits::DataType< ::dome::open_dome > 
template<>
struct DataType< ::dome::open_domeResponse>
{
  static const char* value()
  {
    return DataType< ::dome::open_dome >::value();
  }
  static const char* value(const ::dome::open_domeResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // DOME_MESSAGE_OPEN_DOME_H
