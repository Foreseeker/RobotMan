#!/usr/bin/env python
from support_file import *
from state_reset import *

pos_2 = pi/3
pos_4 = pi/2
pos_5 = -pi/2
pos_wave_1 = -2.5
pos_wave_2 = -1.8

def test_run():
    rospy.init_node('PresentationRun_01',anonymous=True) 
    pub_04(pos_4,2.0)
    pub_05(pos_5,1.0) 
    pub_02(pos_2,2.0)
    for i in range(3):
        pub_05(pos_wave_1,2.0)
        pub_05(pos_wave_2,2.0)

if __name__ == '__main__':
    try: 
        test_run()
        sleep(1.0)
        relax() 
    except rospy.ROSInterruptException:
        pass