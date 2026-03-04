#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist

def counter():

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rospy.init_node('turtle')

    rate = rospy.Rate(1)  # 1Hz = 1초에 1번

    move = Twist()
    move.linear.x =2.0
    move.angular.z = 1.0

    while not rospy.is_shutdown():


        pub.publish(move)

        rate.sleep()

if __name__ == '__main__':

    try:

        counter()

    except rospy.ROSInterruptException:

        pass
