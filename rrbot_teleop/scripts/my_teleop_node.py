#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import keyboard

def teleop():
    
    topic1 = '/rrbot/joint1_position_controller/command'
    topic2 = '/rrbot/joint2_position_controller/command'
        
    pub1 = rospy.Publisher(topic1, Float64, queue_size=10)
    pub2 = rospy.Publisher(topic2, Float64, queue_size=10)
    rospy.init_node('teleop', anonymous=True)
    rate = rospy.Rate(10)  # 10hz


    """
    while not rospy.is_shutdown():
        command = Float64()
        # Get command input from user
        command.data = float(input("Enter command: "))
        # Publish command to topic1 and topic2
        pub1.publish(command)
        pub2.publish(command)
        rate.sleep()
    """
    command = Float64()
    command.data = 0

    while not rospy.is_shutdown():
        
        # Get command input from user
        if keyboard.is_pressed("w"):
            command.data = command.data + 0.087
        if keyboard.is_pressed("s"):
            command.data = command.data - 0.087
        print("hello")
        # Publish command to topic1 and topic2
        pub1.publish(command)
        pub2.publish(command)
        rate.sleep()

if __name__ == '__main__':
    try:
        teleop()
    except rospy.ROSInterruptException:
        pass
