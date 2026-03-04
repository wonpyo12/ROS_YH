#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Float32

def counter():

    pub = rospy.Publisher('counter', Float32, queue_size=10)

    rospy.init_node('counter_pub')

    rate = rospy.Rate(1)  # 1Hz = 1초에 1번

    temp = 0

    while not rospy.is_shutdown():

        temp = random.uniform(20.0,40.0)
        

        if temp > 35.0 :
            rospy.loginfo("35도 보다 높습니다. 현재온도 : %d",temp)
        else :
            rospy.loginfo("현재온도: %d", temp)

        pub.publish(temp)
        rate.sleep()

if __name__ == '__main__':

    try:

        counter()

    except rospy.ROSInterruptException:

        pass
