#!/usr/bin/env python
import keyboard
import os
from support_file import *

joint_state = [0,0,0,0,0,0,0,0,0,0]
pub_num = 1
t = 0.1
clc = lambda: os.system('clear')

def execute_order(pub_num, state, t):
    if pub_num == 1:
        return pub_01(state, t)
    if pub_num == 2:
        return pub_02(state, t)
    if pub_num == 3:
        return pub_03(state, t)
    if pub_num == 4:
        return pub_04(state, t)
    if pub_num == 5:
        return pub_05(state, t)
    if pub_num == 6:
        return pub_06(state, t)
    if pub_num == 7:
        return pub_07(state, t)
    if pub_num == 8:
        return pub_08(state, t)
    if pub_num == 9:
        return pub_09(state, t)
    if pub_num == 10:
        return pub_010(state, t)
    if pub_num == 11:
        return pub_011(state, t)
    if pub_num == 12:
        return pub_012(state, t)
    if pub_num == 13:
        return pub_013(state, t)
                
def move_joint(joint_state,pub_num):
    state = joint_state[pub_num]
    while keyboard.read_key() != 'q':
        if keyboard.read_key() == 'j':
            clc()
            if (pub_num == 1):
                pub_num = 1
            else:
                pub_num -= 1
                print("Obecny joint - ",pub_num)
                move_joint(joint_state,pub_num)
                
        if keyboard.read_key() == 'l':
            clc() 
            if (pub_num == 13):
                pub_num = 13 
            else:
                pub_num += 1
                print("Obecny joint - ",pub_num)
                move_joint(joint_state,pub_num)

        if keyboard.read_key() == 'i':
            clc()
            if (state == joint_up[pub_num]):
                state = joint_up[pub_num]
                print("Error: Max range\n")
            else:
                state += 0.05
                joint_state[pub_num] = state
                print('Obecny stan - ', state)
                execute_order(pub_num,joint_state[pub_num],t)              

        if keyboard.read_key() == 'k':
            clc()
            if (state == joint_low[pub_num]):
                state = joint_low[pub_num]
                print("Error: Max range\n")
            else:
                state -= 0.05
                joint_state[pub_num] = state
                print('Obecny stan - ', state)
                execute_order(pub_num,joint_state[pub_num],t)            

if __name__ == '__main__':
    try: 
        if keyboard.read_key() == 'a':
            rospy.init_node('KeyboardRun',anonymous=True)
            print("Aktywowano sterownie")
            move_joint(joint_state,pub_num)
    except rospy.ROSInterruptException:
        pass