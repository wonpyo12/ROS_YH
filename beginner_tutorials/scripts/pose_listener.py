#!/usr/bin/env python3

import rospy

from std_msgs.msg import Int32

def callback(msg):

    rospy.loginfo("위치: x=%.2f, y=%.2f, 방향=%.2f", msg.x, msg.y, msg.theta)

def listener():

    rospy.init_node('pose_listener')

    rospy.Subscriber('pose', Int32, callback)

    rospy.spin()

if __name__ == '__main__':

    listener()
