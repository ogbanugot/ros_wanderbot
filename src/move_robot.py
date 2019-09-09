#!/usr/bin/env python
import roslib
import sys
import rospy
import cv2
import numpy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class move_robot:

  def __init__(self):
    self.velocity_publisher = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber('camera/rgb/image_raw',Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
    vel_msg = Twist()
    hsv	=	cv2.cvtColor(cv_image,	cv2.COLOR_BGR2HSV)
    lower_yellow	=	numpy.array([	29, 24, 85])
    upper_yellow	=	numpy.array([30, 255, 177]) 
    mask	=	cv2.inRange(hsv,	lower_yellow,	upper_yellow)
    masked	=	cv2.bitwise_and(cv_image,	cv_image,	mask=mask)
    res, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    valid_contours = []
    for contour in contours:            
            x, y, width, height = cv2.boundingRect(contour)
            print(height*width)              
            if(height*width < 650):
              valid_contours.append(contour)

    if valid_contours:    
      vel_msg.linear.x = 0.1
      vel_msg.linear.y = 0
      vel_msg.linear.z = 0
      self.velocity_publisher.publish(vel_msg)
    else:
      vel_msg.angular.x = 0
      vel_msg.angular.y = 0
      vel_msg.angular.z = 0.2
      self.velocity_publisher.publish(vel_msg)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

def main(args):
  ic = move_robot()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)