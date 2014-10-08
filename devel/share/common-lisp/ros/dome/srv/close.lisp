; Auto-generated. Do not edit!


(cl:in-package dome-srv)


;//! \htmlinclude close-request.msg.html

(cl:defclass <close-request> (roslisp-msg-protocol:ros-message)
  ((speed
    :reader speed
    :initarg :speed
    :type cl:fixnum
    :initform 0))
)

(cl:defclass close-request (<close-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <close-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'close-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dome-srv:<close-request> is deprecated: use dome-srv:close-request instead.")))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <close-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-srv:speed-val is deprecated.  Use dome-srv:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <close-request>) ostream)
  "Serializes a message object of type '<close-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speed)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <close-request>) istream)
  "Deserializes a message object of type '<close-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speed)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<close-request>)))
  "Returns string type for a service object of type '<close-request>"
  "dome/closeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'close-request)))
  "Returns string type for a service object of type 'close-request"
  "dome/closeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<close-request>)))
  "Returns md5sum for a message object of type '<close-request>"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'close-request)))
  "Returns md5sum for a message object of type 'close-request"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<close-request>)))
  "Returns full string definition for message of type '<close-request>"
  (cl:format cl:nil "uint16 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'close-request)))
  "Returns full string definition for message of type 'close-request"
  (cl:format cl:nil "uint16 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <close-request>))
  (cl:+ 0
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <close-request>))
  "Converts a ROS message object to a list"
  (cl:list 'close-request
    (cl:cons ':speed (speed msg))
))
;//! \htmlinclude close-response.msg.html

(cl:defclass <close-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type dome-msg:roof
    :initform (cl:make-instance 'dome-msg:roof)))
)

(cl:defclass close-response (<close-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <close-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'close-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dome-srv:<close-response> is deprecated: use dome-srv:close-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <close-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-srv:status-val is deprecated.  Use dome-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <close-response>) ostream)
  "Serializes a message object of type '<close-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'status) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <close-response>) istream)
  "Deserializes a message object of type '<close-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'status) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<close-response>)))
  "Returns string type for a service object of type '<close-response>"
  "dome/closeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'close-response)))
  "Returns string type for a service object of type 'close-response"
  "dome/closeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<close-response>)))
  "Returns md5sum for a message object of type '<close-response>"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'close-response)))
  "Returns md5sum for a message object of type 'close-response"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<close-response>)))
  "Returns full string definition for message of type '<close-response>"
  (cl:format cl:nil "roof status~%~%~%================================================================================~%MSG: dome/roof~%float32 ubication~%bool sensor1~%bool sensor2~%bool sensor3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'close-response)))
  "Returns full string definition for message of type 'close-response"
  (cl:format cl:nil "roof status~%~%~%================================================================================~%MSG: dome/roof~%float32 ubication~%bool sensor1~%bool sensor2~%bool sensor3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <close-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'status))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <close-response>))
  "Converts a ROS message object to a list"
  (cl:list 'close-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'close)))
  'close-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'close)))
  'close-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'close)))
  "Returns string type for a service object of type '<close>"
  "dome/close")