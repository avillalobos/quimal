"""autogenerated by genpy from dome/closeRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class closeRequest(genpy.Message):
  _md5sum = "0026b653807c4b3ac6672ca0fd38046c"
  _type = "dome/closeRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint16 speed

"""
  __slots__ = ['speed']
  _slot_types = ['uint16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       speed

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(closeRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.speed is None:
        self.speed = 0
    else:
      self.speed = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_H.pack(self.speed))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 2
      (self.speed,) = _struct_H.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_H.pack(self.speed))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 2
      (self.speed,) = _struct_H.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_H = struct.Struct("<H")
"""autogenerated by genpy from dome/closeResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import dome.msg

class closeResponse(genpy.Message):
  _md5sum = "cbbdd3f7c5382e7f2ae887052ce258c9"
  _type = "dome/closeResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """roof status


================================================================================
MSG: dome/roof
float32 ubication
bool sensor1
bool sensor2
bool sensor3

"""
  __slots__ = ['status']
  _slot_types = ['dome/roof']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       status

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(closeResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.status is None:
        self.status = dome.msg.roof()
    else:
      self.status = dome.msg.roof()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_f3B.pack(_x.status.ubication, _x.status.sensor1, _x.status.sensor2, _x.status.sensor3))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.status is None:
        self.status = dome.msg.roof()
      end = 0
      _x = self
      start = end
      end += 7
      (_x.status.ubication, _x.status.sensor1, _x.status.sensor2, _x.status.sensor3,) = _struct_f3B.unpack(str[start:end])
      self.status.sensor1 = bool(self.status.sensor1)
      self.status.sensor2 = bool(self.status.sensor2)
      self.status.sensor3 = bool(self.status.sensor3)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_f3B.pack(_x.status.ubication, _x.status.sensor1, _x.status.sensor2, _x.status.sensor3))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.status is None:
        self.status = dome.msg.roof()
      end = 0
      _x = self
      start = end
      end += 7
      (_x.status.ubication, _x.status.sensor1, _x.status.sensor2, _x.status.sensor3,) = _struct_f3B.unpack(str[start:end])
      self.status.sensor1 = bool(self.status.sensor1)
      self.status.sensor2 = bool(self.status.sensor2)
      self.status.sensor3 = bool(self.status.sensor3)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_f3B = struct.Struct("<f3B")
class close(object):
  _type          = 'dome/close'
  _md5sum = '6b2cf0726d295207cb0af1ee517cbebb'
  _request_class  = closeRequest
  _response_class = closeResponse