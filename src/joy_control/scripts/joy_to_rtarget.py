#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray 


# Create a publisher for the "rtarget" topic
rtarget_pub = rospy.Publisher('rTarget_value', Float32, queue_size=5)
# new_joy_pub = rospy.Publisher('joy_filtered', Joy, queue_size=10)
move_pub= rospy.Publisher('move_mode', Float32, queue_size=10)



def joy_callback(state):
    joy_values = Float32MultiArray()
    # Retrieve the value of the 5th axis
    if len(state.axes) >= 5:
        value = 30+ state.axes[4] * 40.0
        value2 =state.buttons[4]

        # Publish the multiplied value on the "rtarget" topic
        rtarget_pub.publish(value)
        move_pub.publish(value2)

        # value = 30.0 + state.axes[4] * 30.0
        
        # joy_values.data = [ state.buttons[4], state.buttons[3],state.buttons[0],state.buttons[2],state.buttons[1]]
        # # joy_values[1]= state.buttons[3]
        # # joy_values.buttons[2]= state.buttons[0]
        # # joy_values.buttons[3]= state.buttons[2]
        # # joy_values.buttons[4]= state.buttons[1]
        # new_joy_pub.publish(joy_values)
        rtarget_pub.publish(value)

def joy_to_rtarget():
    # Create a publisher for the "rtarget" topic
    # rtargetpub = rospy.Publisher('rTarget_value', Float32, queue_size=10)
    rospy.init_node('joy_to_rtarget', anonymous=True)
    
    # Subscribe to the joystick topic
    rospy.Subscriber('joy', Joy, joy_callback)



    rospy.spin()

if __name__ == '__main__':
    joy_to_rtarget()

