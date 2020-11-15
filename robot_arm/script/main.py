#!/usr/bin/env python
#license removed for brevity
import math
import rospy
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('/rm/joint1_position_controller/command',Float64, queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" %rospy.get_time()
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass