#!/usr/bin/env python
#license removed for brevity
import math
import rospy
from time import sleep
from std_msgs.msg import Float64

def test_run():
    pub_1 = rospy.Publisher('/rm/joint1_position_controller/command',Float64, queue_size=10)
    pub_2 = rospy.Publisher('/rm/joint2_position_controller/command',Float64, queue_size=10)
    rospy.init_node('TestRun_01',anonymous=True)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        position_1 = 0
        position_2 = 0
        pub_1.publish(position_1)
        rate.sleep()
        sleep(3.0)
        pub_2.publish(position_2)
        rate.sleep()
        sleep(3.0)


if __name__ == '__main__':
    try: 
        test_run() 
    except rospy.ROSInterruptException:
        pass