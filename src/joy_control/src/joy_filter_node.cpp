// #include <ros/ros.h>
// #include <sensor_msgs/Joy.h>
// #include <std_msgs/Float32.h>

// sensor_msgs::Joy joy_filtered_msg;
// ros::Publisher joy_filtered_pub("joy_filtered", &joy_filtered_msg);
// void joyCallback(const sensor_msgs::Joy::ConstPtr& joy_msg)
// {
//     // Extract desired values from joy message
//     float axis1 = joy_msg->axes[4];  // Example: Extracting the first axis value
//     float axis2 = joy_msg->axes[4];  // Example: Extracting the second axis value
//     bool forward= joy_msg->buttons[3];
//     bool backward= joy_msg->buttons[0];
//     bool clockwise= joy_msg->buttons[2];
//     bool anticlockwise= joy_msg->buttons[1];
//     // Perform any desired operations on the extracted values
//     float filtered_axis1 = 30+ axis1 * 30.0;
//     float filtered_axis2 = axis2 + 0.5;
    
//     // Create and publish a new joy message with the filtered values
    
//     joy_filtered_msg.header = joy_msg->header;
//     joy_filtered_msg.axes = {filtered_axis1, filtered_axis2};
//     joy_filtered_msg.buttons = { forward, backward, clockwise, anticlockwise};

//     joy_filtered_pub.publish(joy_filtered_msg);
// }

// int main(int argc, char** argv)
// {
//     // Initialize the ROS node
//     ros::init(argc, argv, "joy_filter_node");
//     ros::NodeHandle nh;

//     // Subscribe to the "joy" topic
//     ros::Subscriber joy_sub = nh.subscribe("joy", 10, joyCallback);

//     // Publish on the "joy_filtered" topic
//     joy_filtered_pub = nh.advertise<sensor_msgs::Joy>("joy_filtered", 10);

//     // Spin the node
//     ros::spin();

//     return 0;
// }
