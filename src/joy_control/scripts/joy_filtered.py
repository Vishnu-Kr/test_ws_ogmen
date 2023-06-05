#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy

joy_filtered_pub = rospy.Publisher('joy_filtered', Joy, queue_size=10)

def joy_callback(data):
    
    # Extract axes and buttons data
    # axes = data.axes
    # buttons = data.buttons

    # # Apply changes to the axes and buttons data
    # # Example: Increase the first axis value by 0.1
    # # axes[0] = 0
    # # axes[1] = 0
    # # axes[2] = 0
    # # axes[3] = 0
    # # axes[4] = 30 + axes[4]*30
    # # axes[5] = 0
    # # axes[6] = 0
    # # axes[7] = 0


    # # Create a new Joy message with the modified data
    # joy_filtered = Joy()
    # joy_filtered.header = data.header
    # joy_filtered.axes=0
    # # joy_filtered.axes[0] = 0
    # # joy_filtered.axes[1] = 0
    # # joy_filtered.axes[2] = 0
    # # joy_filtered.axes[3] = 0
    # # joy_filtered.axes[4] = 0
    # # joy_filtered.axes[5] = 0
    # # joy_filtered.axes[6] = 0
    # # joy_filtered.axes[7] = 0
    # joy_filtered.buttons = buttons

    # # Publish the filtered joy message
    # joy_filtered_pub.publish(joy_filtered)

def joy_filter_node():
    rospy.init_node('joy_filter_node', anonymous=True)

    # Subscribe to the joy topic
    rospy.Subscriber('joy', Joy, joy_callback)

    # Create a publisher for the filtered joy topic
    # joy_filtered_pub = rospy.Publisher('joy_filtered', Joy, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    try:
        joy_filter_node()
    except rospy.ROSInterruptException:
        pass
