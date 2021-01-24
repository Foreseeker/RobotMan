#!/usr/bin/env python
#license removed for brevity
import math
import rospy
from std_msgs.msg import Float64

def shoulder_1():
    pub = rospy.Publisher('/rm/joint1_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Shoulder_01',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = -(math.pi)/2
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def shoulder_2():
    pub = rospy.Publisher('/rm/joint2_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Shoulder_2',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = 1
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def arm_1():
    pub = rospy.Publisher('/rm/joint3_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Arm_01',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def arm_2():
    pub = rospy.Publisher('/rm/joint4_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Arm_02',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = -1
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def arm_3():
    pub = rospy.Publisher('/rm/joint5_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Arm_03',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def wrist():
    pub = rospy.Publisher('/rm/joint6_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Wrist',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def hand():
    pub = rospy.Publisher('/rm/joint7_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Hand',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_1_a():
    pub = rospy.Publisher('/rm/joint8_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Finger_01_A',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_1_b():
    pub = rospy.Publisher('/rm/joint9_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Finger_01_B',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_2_a():
    pub = rospy.Publisher('/rm/joint10_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Finger_02_A',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_2_b():
    pub = rospy.Publisher('/rm/joint11_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Finger_02_B',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_3_a():
    pub = rospy.Publisher('/rm/joint12_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Finger_03_A',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_3_b():
    pub = rospy.Publisher('/rm/joint13_position_controller/command',Float64, queue_size=10)
    rospy.init_node('Py_Finger_03_B',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

if __name__ == '__main__':
    try:
        shoulder_1()
    except rospy.ROSInterruptException:
        pass