

class Publisher():
    def __init__(self):
        self.cam_topic = rospy.Publisher("/lab3_cam", Twist, size="10")
        self.pos_topic = rospy.Publisher("/lab3_pos", Twist, size="10")
        return

    def publish_cam(self, msg):
        msg = Twist()
        msg.
        pass

    def publish_pos(self, msg):
        pass

if __name__ == '__main__':

    rospy.init_node("publisher", disable_signals=True)
    data_publisher = Publisher()
    
    try:
        # Read bag file
        while not rospy.is_shutdown():
            # Publish data

            # Process Data

    except KeyboardInterrupt:

        # Display final results
        rospy.spin()
        
    rospy.spin()
    
    rospy.init.node('publisher')
    Publisher()
    rospy.spin()
