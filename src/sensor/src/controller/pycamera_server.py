#!/usr/bin/python
import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import picamera, io, time
import numpy as np

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("camera",Image)
    self.camera = picamera.PiCamera()
    self.camera.resolution = (640, 480)
    self.bridge = CvBridge()

  def publish(self):
    stream = io.BytesIO()
    self.camera.capture(stream,format='jpeg')
    stream.seek(0)
    try:
      data = np.fromstring(stream.getvalue(), dtype=np.uint8)
      cv_image = cv2.imdecode(data,1)
      # se da vuelta la imagen porque cv2 retorna imagen en bgr8 y la necesito en rgb8
      cv_image = cv_image[:, :, ::-1]
      #print cv_image
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "rgb8"))
    except CvBridgeError, e:
      print e

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  r = rospy.Rate(1)
  while not rospy.is_shutdown():
    ic.publish()
    print "image published"
    r.sleep()

if __name__ == '__main__':
    main(sys.argv)
