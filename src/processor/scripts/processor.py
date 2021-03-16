#!/usr/bin/env python2

from target_identifier import TargetIdentifier
from localization import Localizer
import roslib
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats

from geometry_msgs.msg import Twist, TransformStamped
from sensor_msgs.msg import Image

from cv_bridge import CvBridge
import numpy as np

class Processor():
    def __init__(self):
        self.target_identifier = TargetIdentifier()
        self.localizer = Localizer()
        self.sub_cam = rospy.Subscriber("/lab3_cam", Image, self.identify_targets)
        self.sub_pos = rospy.Subscriber("/lab3_pos", TransformStamped, self.store_pos)
        self.pub_locations = rospy.Publisher('/lab3_locations', numpy_msg(Floats), queue_size="0")
        self.bridge = CvBridge()
        self.locations = []
        return

    def identify_targets(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        pixels = self.target_identifier.identify_targets(img)
        if not pixels:
            return
        else:
            new_locations = self.localizer.localize(pixels, self.pos)
            self.locations += new_locations
            self.pub_locations.publish(new_locations)

            print new_locations
            f = open('/home/demi/aer1217/labs/src/processor/location.txt', 'a')
            for i in range(len(new_locations)):
                f.writelines('\n' + np.array2string(new_locations[i][0])+' '+ np.array2string(new_locations[i][1]))
            f.close()

        return

    def store_pos(self, msg):
        self.pos = msg
        return


if __name__ == '__main__':

    rospy.init_node("processor", disable_signals=True)
    data_processor = Processor()

    rospy.spin()
