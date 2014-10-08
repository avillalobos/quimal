
(cl:in-package :asdf)

(defsystem "dome-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :dome-msg
)
  :components ((:file "_package")
    (:file "close_dome" :depends-on ("_package_close_dome"))
    (:file "_package_close_dome" :depends-on ("_package"))
    (:file "open_dome" :depends-on ("_package_open_dome"))
    (:file "_package_open_dome" :depends-on ("_package"))
  ))