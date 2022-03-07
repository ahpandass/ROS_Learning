#! /usr/bin/python
import rospy
from rospy.timer import Rate
from std_msgs.msg import String
from geometry_msgs.msg import Twist  

if __name__ == "__main__":
    rospy.init_node("motor_pub")
    pub = rospy.Publisher("motor_order",Twist,queue_size=10)

    msg = Twist()
    rate = rospy.Rate(0.5)
    msg.linear.x = 5
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()
        rospy.loginfo('send order info: '+str(msg.linear.x ))

    pass