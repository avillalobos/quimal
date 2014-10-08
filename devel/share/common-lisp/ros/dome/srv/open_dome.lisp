; Auto-generated. Do not edit!


(cl:in-package dome-srv)


;//! \htmlinclude open_dome-request.msg.html

(cl:defclass <open_dome-request> (roslisp-msg-protocol:ros-message)
  ((speed
    :reader speed
    :initarg :speed
    :type cl:fixnum
    :initform 0))
)

(cl:defclass open_dome-request (<open_dome-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <open_dome-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'open_dome-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dome-srv:<open_dome-request> is deprecated: use dome-srv:open_dome-request instead.")))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <open_dome-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-srv:speed-val is deprecated.  Use dome-srv:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <open_dome-request>) ostream)
  "Serializes a message object of type '<open_dome-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speed)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <open_dome-request>) istream)
  "Deserializes a message object of type '<open_dome-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speed)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<open_dome-request>)))
  "Returns string type for a service object of type '<open_dome-request>"
  "dome/open_domeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'open_dome-request)))
  "Returns string type for a service object of type 'open_dome-request"
  "dome/open_domeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<open_dome-request>)))
  "Returns md5sum for a message object of type '<open_dome-request>"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'open_dome-request)))
  "Returns md5sum for a message object of type 'open_dome-request"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<open_dome-request>)))
  "Returns full string definition for message of type '<open_dome-request>"
  (cl:format cl:nil "uint16 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'open_dome-request)))
  "Returns full string definition for message of type 'open_dome-request"
  (cl:format cl:nil "uint16 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <open_dome-request>))
  (cl:+ 0
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <open_dome-request>))
  "Converts a ROS message object to a list"
  (cl:list 'open_dome-request
    (cl:cons ':speed (speed msg))
))
;//! \htmlinclude open_dome-response.msg.html

(cl:defclass <open_dome-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type dome-msg:roof
    :initform (cl:make-instance 'dome-msg:roof)))
)

(cl:defclass open_dome-response (<open_dome-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <open_dome-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'open_dome-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dome-srv:<open_dome-response> is deprecated: use dome-srv:open_dome-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <open_dome-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-srv:status-val is deprecated.  Use dome-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <open_dome-response>) ostream)
  "Serializes a message object of type '<open_dome-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'status) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <open_dome-response>) istream)
  "Deserializes a message object of type '<open_dome-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'status) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<open_dome-response>)))
  "Returns string type for a service object of type '<open_dome-response>"
  "dome/open_domeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'open_dome-response)))
  "Returns string type for a service object of type 'open_dome-response"
  "dome/open_domeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<open_dome-response>)))
  "Returns md5sum for a message object of type '<open_dome-response>"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'open_dome-response)))
  "Returns md5sum for a message object of type 'open_dome-response"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<open_dome-response>)))
  "Returns full string definition for message of type '<open_dome-response>"
  (cl:format cl:nil "roof status~%~%~%================================================================================~%MSG: dome/roof~%float32 ubication~%bool sensor1~%bool sensor2~%bool sensor3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'open_dome-response)))
  "Returns full string definition for message of type 'open_dome-response"
  (cl:format cl:nil "roof status~%~%~%================================================================================~%MSG: dome/roof~%float32 ubication~%bool sensor1~%bool sensor2~%bool sensor3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <open_dome-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'status))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <open_dome-response>))
  "Converts a ROS message object to a list"
  (cl:list 'open_dome-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'open_dome)))
  'open_dome-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'open_dome)))
  'open_dome-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'open_dome)))
  "Returns string type for a service object of type '<open_dome>"
  "dome/open_dome")