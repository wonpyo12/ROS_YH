#!/usr/bin/env python3

import rospy

from turtlesim.msg import Pose

def callback(data):
    if data.x<=1.0 or data.x>=10.0 or data.y<=1.0 or data.y>=10.0:
        rospy.loginfo("x: %.1f, y:%.1f 경고 벽이랑 너무 가깝습니다.", data.x,data.y)
    else :
        rospy.loginfo("x: %.1f, y:%.1f", data.x,data.y)

def listener():

    rospy.Subscriber('/turtle1/pose', Pose, callback)

    rospy.init_node('turtle')

    rospy.spin()

if __name__ == '__main__':

    listener()
