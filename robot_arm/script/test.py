#!/usr/bin/env python
from support_file import *

position_test = 1
time_test = 1

def test_run():
    rospy.init_node('TestRun',anonymous=True) 
    while not rospy.is_shutdown():
        pub_01(position_test, time_test)
        


if __name__ == '__main__':
    try: 
        test_run() 
    except rospy.ROSInterruptException:
        pass