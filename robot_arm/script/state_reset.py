from support_file import *

pi = math.pi

def reset():
    rospy.init_node('ResetState',anonymous=True)
    pub_01(0.0,1.0)
    pub_02(0.0,1.0) 
    pub_03(0.0,1.0) 
    pub_04(0.0,1.0) 
    pub_05(0.0,1.0) 
    pub_06(0.0,1.0) 
    pub_07(0.0,1.0) 
    pub_08(0.0,1.0)
    pub_09(0.0,1.0) 
    pub_010(0.0,1.0) 
    pub_011(0.0,1.0)
    pub_012(0.0,1.0)
    pub_013(0.0,1.0)

def relax():
    pub_01(0.0,1.0)
    pub_02(0.0,1.0) 
    pub_03(0.0,1.0) 
    pub_04(0.0,1.0) 
    pub_05(0.0,1.0) 
    pub_06(0.0,1.0) 
    pub_07(0.0,1.0) 
    pub_08(0.0,1.0)
    pub_09(0.0,1.0) 
    pub_010(0.0,1.0) 
    pub_011(0.0,1.0)
    pub_012(0.0,1.0)
    pub_013(0.0,1.0)


if __name__ == '__main__':
    try: 
        reset() 
    except rospy.ROSInterruptException:
        pass
