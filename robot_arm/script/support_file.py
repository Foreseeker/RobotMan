#!/usr/bin/env python
import math
import rospy
from time import sleep
from std_msgs.msg import Float64

pub_1 = rospy.Publisher('/rm/joint1_position_controller/command',Float64, queue_size=10)
pub_2 = rospy.Publisher('/rm/joint2_position_controller/command',Float64, queue_size=10)
pub_3 = rospy.Publisher('/rm/joint3_position_controller/command',Float64, queue_size=10)
pub_4 = rospy.Publisher('/rm/joint4_position_controller/command',Float64, queue_size=10)
pub_5 = rospy.Publisher('/rm/joint5_position_controller/command',Float64, queue_size=10)
pub_6 = rospy.Publisher('/rm/joint6_position_controller/command',Float64, queue_size=10)
pub_7 = rospy.Publisher('/rm/joint7_position_controller/command',Float64, queue_size=10)
pub_8 = rospy.Publisher('/rm/joint8_position_controller/command',Float64, queue_size=10)
pub_9 = rospy.Publisher('/rm/joint9_position_controller/command',Float64, queue_size=10)
pub_10 = rospy.Publisher('/rm/joint10_position_controller/command',Float64, queue_size=10)
pub_11 = rospy.Publisher('/rm/joint11_position_controller/command',Float64, queue_size=10)
pub_12 = rospy.Publisher('/rm/joint12_position_controller/command',Float64, queue_size=10)
pub_13 = rospy.Publisher('/rm/joint13_position_controller/command',Float64, queue_size=10)

def pub_01(val,t):
    sleep(t)
    pub_1.publish(val)

def pub_02(val,t):
    sleep(t)
    pub_2.publish(val)

def pub_03(val,t):
    sleep(t)
    pub_3.publish(val)

def pub_04(val,t):
    sleep(t)
    pub_4.publish(val)

def pub_05(val,t):
    sleep(t)
    pub_5.publish(val)

def pub_06(val,t):
    sleep(t)
    pub_6.publish(val)

def pub_07(val,t):
    sleep(t)
    pub_7.publish(val)

def pub_08(val,t):
    sleep(t)
    pub_8.publish(val)

def pub_09(val,t):
    sleep(t)
    pub_9.publish(val)

def pub_010(val,t):
    sleep(t)
    pub_10.publish(val)

def pub_011(val,t):
    sleep(t)
    pub_11.publish(val)

def pub_012(val,t):
    sleep(t)
    pub_12.publish(val)

def pub_013(val,t):
    sleep(t)
    pub_13.publish(val)
