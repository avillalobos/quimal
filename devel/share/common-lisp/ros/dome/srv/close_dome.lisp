; Auto-generated. Do not edit!


(cl:in-package dome-srv)


;//! \htmlinclude close_dome-request.msg.html

(cl:defclass <close_dome-request> (roslisp-msg-protocol:ros-message)
  ((speed
    :reader speed
    :initarg :speed
    :type cl:fixnum
    :initform 0))
)

(cl:defclass close_dome-request (<close_dome-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <close_dome-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'close_dome-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dome-srv:<close_dome-request> is deprecated: use dome-srv:close_dome-request instead.")))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <close_dome-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-srv:speed-val is deprecated.  Use dome-srv:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <close_dome-request>) ostream)
  "Serializes a message object of type '<close_dome-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speed)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <close_dome-request>) istream)
  "Deserializes a message object of type '<close_dome-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speed)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speed)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<close_dome-request>)))
  "Returns string type for a service object of type '<close_dome-request>"
  "dome/close_domeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'close_dome-request)))
  "Returns string type for a service object of type 'close_dome-request"
  "dome/close_domeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<close_dome-request>)))
  "Returns md5sum for a message object of type '<close_dome-request>"
  "1982571d872b947abb761709b9b8b573")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'close_dome-request)))
  "Returns md5sum for a message object of type 'close_dome-request"
  "1982571d872b947abb761709b9b8b573")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<close_dome-request>)))
  "Returns full string definition for message of type '<close_dome-request>"
  (cl:format cl:nil "uint16 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'close_dome-request)))
  "Returns full string definition for message of type 'close_dome-request"
  (cl:format cl:nil "uint16 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <close_dome-request>))
  (cl:+ 0
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <close_dome-request>))
  "Converts a ROS message object to a list"
  (cl:list 'close_dome-request
    (cl:cons ':speed (speed msg))
))
;//! \htmlinclude close_dome-response.msg.html

(cl:defclass <close_dome-response> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type dome-msg:roof
    :initform (cl:make-instance 'dome-msg:roof)))
)

(cl:defclass close_dome-response (<close_dome-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <close_dome-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'close_dome-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dome-srv:<close_dome-response> is deprecated: use dome-srv:close_dome-response instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <close_dome-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-srv:status-val is deprecated.  Use dome-srv:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <close_dome-response>) ostream)
  "Serializes a message object of type '<close_dome-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'status) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <close_dome-response>) istream)
  "Deserializes a message object of type '<close_dome-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'status) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<close_dome-response>)))
  "Returns string type for a service object of type '<close_dome-response>"
  "dome/close_domeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'close_dome-response)))
  "Returns string type for a service object of type 'close_dome-response"
  "dome/close_domeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<close_dome-response>)))
  "Returns md5sum for a message object of type '<close_dome-response>"
  "1982571d872b947abb761709b9b8b573")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'close_dome-response)))
  "Returns md5sum for a message object of type 'close_dome-response"
  "1982571d872b947abb761709b9b8b573")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<close_dome-response>)))
  "Returns full string definition for message of type '<close_dome-response>"
  (cl:format cl:nil "roof status~%~%~%================================================================================~%MSG: dome/roof~%float32 ubication~%bool sensor1~%bool sensor2~%bool sensor3~%string state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'close_dome-response)))
  "Returns full string definition for message of type 'close_dome-response"
  (cl:format cl:nil "roof status~%~%~%================================================================================~%MSG: dome/roof~%float32 ubication~%bool sensor1~%bool sensor2~%bool sensor3~%string state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <close_dome-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'status))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <close_dome-response>))
  "Converts a ROS message object to a list"
  (cl:list 'close_dome-response
    (cl:cons ':status (status msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'close_dome)))
  'close_dome-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'close_dome)))
  'close_dome-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'close_dome)))
  "Returns string type for a service object of type '<close_dome>"
  "dome/close_dome")