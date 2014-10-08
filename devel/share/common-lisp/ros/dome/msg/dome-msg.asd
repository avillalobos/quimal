
(cl:in-package :asdf)

(defsystem "dome-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "roof" :depends-on ("_package_roof"))
    (:file "_package_roof" :depends-on ("_package"))
  ))