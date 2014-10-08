; Auto-generated. Do not edit!


(cl:in-package dome-srv)


;//! \htmlinclude open-request.msg.html

(cl:defclass <open-request> (roslisp-msg-protocol:ros-message)
  ((speed
    :reader speed
    :initarg :speed
    :type cl:fixnum
    :initform 0))
)

(cl:defclass open-request (<open-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <open-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'open-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dome-srv:<open-request> is deprecated: use dome-srv:open-request instead.")))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <open-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-srv:speed-val is deprecated.  Use dome-srv:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <open-request>) ostream)
  "Serializes a message object of type '<open-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speed)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <open-request>) istream)
  "Deserializes a message object of type '<open-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speed)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<open-request>)))
  "Returns string type for a service object of type '<open-request>"
  "dome/openRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'open-request)))
  "Returns string type for a service object of type 'open-request"
  "dome/openRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<open-request>)))
  "Returns md5sum for a message object of type '<open-request>"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'open-request)))
  "Returns md5sum for a message object of type 'open-request"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<open-request>)))
  "Returns full string definition for message of type '<open-request>"
  (cl:format cl:nil "uint16 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'open-request)))
  "Returns full string definition for message of type 'open-request"
  (cl:format cl:nil "uint16 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <open-request>))
  (cl:+ 0
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <open-request>))
  "Converts a ROS message object to a list"
  (cl:list 'open-request
    (cl:cons ':speed (speed msg))
))
;//! \htmlinclude open-response.msg.html

(cl:defclass <open-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type dome-msg:roof
    :initform (cl:make-instance 'dome-msg:roof)))
)

(cl:defclass open-response (<open-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <open-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'open-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dome-srv:<open-response> is deprecated: use dome-srv:open-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <open-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-srv:status-val is deprecated.  Use dome-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <open-response>) ostream)
  "Serializes a message object of type '<open-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'status) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <open-response>) istream)
  "Deserializes a message object of type '<open-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'status) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<open-response>)))
  "Returns string type for a service object of type '<open-response>"
  "dome/openResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'open-response)))
  "Returns string type for a service object of type 'open-response"
  "dome/openResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<open-response>)))
  "Returns md5sum for a message object of type '<open-response>"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'open-response)))
  "Returns md5sum for a message object of type 'open-response"
  "6b2cf0726d295207cb0af1ee517cbebb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<open-response>)))
  "Returns full string definition for message of type '<open-response>"
  (cl:format cl:nil "roof status~%~%~%================================================================================~%MSG: dome/roof~%float32 ubication~%bool sensor1~%bool sensor2~%bool sensor3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'open-response)))
  "Returns full string definition for message of type 'open-response"
  (cl:format cl:nil "roof status~%~%~%================================================================================~%MSG: dome/roof~%float32 ubication~%bool sensor1~%bool sensor2~%bool sensor3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <open-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'status))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <open-response>))
  "Converts a ROS message object to a list"
  (cl:list 'open-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'open)))
  'open-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'open)))
  'open-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'open)))
  "Returns string type for a service object of type '<open>"
  "dome/open")