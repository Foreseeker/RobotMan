#!/usr/bin/env python
#license removed for brevity
import math
import rospy
from std_msgs.msg import Float64

def shoulder_1():
    pub = rospy.Publisher('/rm/joint1_position_controller/command',Float64, queue_size=10)
    rospy.init_node('shoulder_1',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def shoulder_2():
    pub = rospy.Publisher('/rm/joint2_position_controller/command',Float64, queue_size=10)
    rospy.init_node('shoulder_2',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def arm_1():
    pub = rospy.Publisher('/rm/joint3_position_controller/command',Float64, queue_size=10)
    rospy.init_node('arm_1',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def arm_2():
    pub = rospy.Publisher('/rm/joint4_position_controller/command',Float64, queue_size=10)
    rospy.init_node('arm_2',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()


def arm_3():
    pub = rospy.Publisher('/rm/joint5_position_controller/command',Float64, queue_size=10)
    rospy.init_node('arm_3',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def wrist():
    pub = rospy.Publisher('/rm/joint6_position_controller/command',Float64, queue_size=10)
    rospy.init_node('wrist',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def hand():
    pub = rospy.Publisher('/rm/joint7_position_controller/command',Float64, queue_size=10)
    rospy.init_node('hand',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_1_a():
    pub = rospy.Publisher('/rm/joint8_position_controller/command',Float64, queue_size=10)
    rospy.init_node('finger_1_a',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_1_b():
    pub = rospy.Publisher('/rm/joint9_position_controller/command',Float64, queue_size=10)
    rospy.init_node('finger_1_b',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_2_a():
    pub = rospy.Publisher('/rm/joint10_position_controller/command',Float64, queue_size=10)
    rospy.init_node('finger_2_a',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_2_b():
    pub = rospy.Publisher('/rm/joint11_position_controller/command',Float64, queue_size=10)
    rospy.init_node('finger_2_b',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_3_a():
    pub = rospy.Publisher('/rm/joint12_position_controller/command',Float64, queue_size=10)
    rospy.init_node('finger_3_a',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        position = math.pi
        rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()

def finger_3_b():
    pub = rospy.Publisher('/rm/joint13_position_controller/command',Float64, queue_size=10)
    rospy.init_node('finger_3_b',anonymous=True)
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