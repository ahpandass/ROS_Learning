#! /usr/bin/python

import rospy,os,sys
from std_msgs.msg import String
from geometry_msgs.msg import Twist  

path = os.path.abspath(".")
sys.path.insert(0,path+'/src/motorcontrol/scripts')

from  Motor import *

def dist2pwm(dist_m):
    dist = int(dist_m*2000)
    minus = dist/abs(dist)
    dist = abs(dist)
    if abs(dist) < 825:
        y = 0
    elif 825 <= abs(dist)<1220:
        y = 1.013*dist - 35.44
    elif 1220 <= abs(dist) < 1350:
        y = 1.538*dist - 676.9
    elif 1350<= abs(dist) <1465:
        y = 1.739 *dist -947.8
    elif 1465 <= abs(dist) <1550:
        y = 2.353 *dist -1847
    elif 1550<= abs(dist) <1625:
        y = 2.667 *dist -2333
    elif 1625<= abs(dist) <1680:
        y = 7.273 *dist - 9818
    elif 1680 <= abs(dist) < 1725:
        y = 4.444 *dist -5067
    elif 1725<= abs(dist) < 1770:
        y = 4.444 *dist -5067
    elif 1770 <= abs(dist) < 1800:
        y = 6.667 *dist -9000
    elif 1800<= abs(dist) < 1820:
        y = 10    *dist -15000
    elif 1820<= abs(dist) < 1865:
        y = 4.444 *dist -4889
    elif 1865<= abs(dist) < 1885:
        y = 10    *dist -15250
    elif 1885<= abs(dist) < 1900:
        y = 13.33 *dist -21530
    elif 1900 <= abs(dist) < 1930:
        y = 6.667 *dist -8867  
    else:
        y = 4096
    return y*minus

def calc_fact(left_wheel_v):
    return left_wheel_v * 0.99144

#def a_v_boot(robert_v):
#    delta = robert_v*2000 - 850
#    for i in range(5):
#        left_wheel_pwm = dist2pwm((850+ delta*(i+1)*0.2)/2000)
#        right_wheel_pwm = calc_fact(left_wheel_pwm)
#        rospy.loginfo("left_wheel_pwm: " + str(left_wheel_pwm) + "  right_wheel_pwm: " + str(right_wheel_pwm))
#        PWM.setMotorModel(int(left_wheel_pwm),int(left_wheel_pwm),int(right_wheel_pwm),int(right_wheel_pwm))
#        time.sleep(0.1)
#        
#def d_v_boot(robert_v):
#    delta = robert_v*2000 - 850
#    for i in range(5):
#        left_wheel_pwm = dist2pwm((robert_v*2000 - delta*(i+1)*0.2)/2000)
#        right_wheel_pwm = calc_fact(left_wheel_pwm)
#        rospy.loginfo("left_wheel_pwm: " + str(left_wheel_pwm) + "  right_wheel_pwm: " + str(right_wheel_pwm))
#        PWM.setMotorModel(int(left_wheel_pwm),int(left_wheel_pwm),int(right_wheel_pwm),int(right_wheel_pwm))
#        time.sleep(0.1)        
    
def doBack(msg):
    rospy.loginfo("I heared: x is " + str(msg.linear.x ) + ' z angular '+str(msg.angular.z))
    
    robert_v = float(msg.linear.x)
    robert_g = float(msg.angular.z)
    #a_v_boot(robert_v)
    left_wheel_pwm = dist2pwm(robert_v)
    right_wheel_pwm = calc_fact(left_wheel_pwm ) - 215*robert_g
    rospy.loginfo("left_wheel_pwm: " + str(left_wheel_pwm) + "  right_wheel_pwm: " + str(right_wheel_pwm))
    PWM.setMotorModel(int(left_wheel_pwm),int(left_wheel_pwm),int(right_wheel_pwm),int(right_wheel_pwm))
    time.sleep(int(msg.linear.z ))
    #d_v_boot(robert_v)
    PWM.setMotorModel(0,0,0,0)

if __name__ == "__main__":
    rospy.init_node("motor_sub")
    PWM = Motor()
    sub = rospy.Subscriber("motor_order",Twist,doBack,queue_size=10)
    
    rospy.spin()
