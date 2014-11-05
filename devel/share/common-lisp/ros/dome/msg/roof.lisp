; Auto-generated. Do not edit!


(cl:in-package dome-msg)


;//! \htmlinclude roof.msg.html

(cl:defclass <roof> (roslisp-msg-protocol:ros-message)
  ((ubication
    :reader ubication
    :initarg :ubication
    :type cl:float
    :initform 0.0)
   (sensor1
    :reader sensor1
    :initarg :sensor1
    :type cl:boolean
    :initform cl:nil)
   (sensor2
    :reader sensor2
    :initarg :sensor2
    :type cl:boolean
    :initform cl:nil)
   (sensor3
    :reader sensor3
    :initarg :sensor3
    :type cl:boolean
    :initform cl:nil)
   (state
    :reader state
    :initarg :state
    :type cl:string
    :initform ""))
)

(cl:defclass roof (<roof>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <roof>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'roof)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dome-msg:<roof> is deprecated: use dome-msg:roof instead.")))

(cl:ensure-generic-function 'ubication-val :lambda-list '(m))
(cl:defmethod ubication-val ((m <roof>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-msg:ubication-val is deprecated.  Use dome-msg:ubication instead.")
  (ubication m))

(cl:ensure-generic-function 'sensor1-val :lambda-list '(m))
(cl:defmethod sensor1-val ((m <roof>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-msg:sensor1-val is deprecated.  Use dome-msg:sensor1 instead.")
  (sensor1 m))

(cl:ensure-generic-function 'sensor2-val :lambda-list '(m))
(cl:defmethod sensor2-val ((m <roof>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-msg:sensor2-val is deprecated.  Use dome-msg:sensor2 instead.")
  (sensor2 m))

(cl:ensure-generic-function 'sensor3-val :lambda-list '(m))
(cl:defmethod sensor3-val ((m <roof>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-msg:sensor3-val is deprecated.  Use dome-msg:sensor3 instead.")
  (sensor3 m))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <roof>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dome-msg:state-val is deprecated.  Use dome-msg:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <roof>) ostream)
  "Serializes a message object of type '<roof>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'ubication))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'sensor1) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'sensor2) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'sensor3) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <roof>) istream)
  "Deserializes a message object of type '<roof>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ubication) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'sensor1) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'sensor2) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'sensor3) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<roof>)))
  "Returns string type for a message object of type '<roof>"
  "dome/roof")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'roof)))
  "Returns string type for a message object of type 'roof"
  "dome/roof")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<roof>)))
  "Returns md5sum for a message object of type '<roof>"
  "904d6c5ea52702f7baaa63d7589e3626")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'roof)))
  "Returns md5sum for a message object of type 'roof"
  "904d6c5ea52702f7baaa63d7589e3626")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<roof>)))
  "Returns full string definition for message of type '<roof>"
  (cl:format cl:nil "float32 ubication~%bool sensor1~%bool sensor2~%bool sensor3~%string state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'roof)))
  "Returns full string definition for message of type 'roof"
  (cl:format cl:nil "float32 ubication~%bool sensor1~%bool sensor2~%bool sensor3~%string state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <roof>))
  (cl:+ 0
     4
     1
     1
     1
     4 (cl:length (cl:slot-value msg 'state))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <roof>))
  "Converts a ROS message object to a list"
  (cl:list 'roof
    (cl:cons ':ubication (ubication msg))
    (cl:cons ':sensor1 (sensor1 msg))
    (cl:cons ':sensor2 (sensor2 msg))
    (cl:cons ':sensor3 (sensor3 msg))
    (cl:cons ':state (state msg))
))
