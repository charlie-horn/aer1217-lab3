import roslib
import rospy
import numpy as np
import cv2

from geometry_msgs.msg import TransformStamped, Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler, quaternion_matrix

class TargetIdentifier():
    def __init__(self):
        self.pixels = []

        self.k_matrix = np.array([[698.86, 0, 306.91],
                                  [0, 699.13, 150.34],
                                  [0, 0, 1]])
        self.k_inv = np.linalg.inv(self.k_matrix)

        self.d = np.array([0.191887, -0.563680, -0.003676, -0.002037, 0])

        return

    def img_undist(self,img):

        img_undistort = cv2.undistort(img, self.k_matrix, self.d, None)

        return img_undistort

    def identify_targets(self, img_original):
        img = self.img_undist(img_original)

        img2 = cv2.inRange(img, (140, 140, 140), (160, 160, 160))

        _,contours,_ = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contour_list = []
        center_list = []
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
            area = cv2.contourArea(contour)
            if ((len(approx) > 8) & (area > 30)):
                contour_list.append(contour)
                M = cv2.moments(contour)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                center_list.append([cX, cY])



        # img2 = cv2.inRange(img, (140, 140, 140), (160, 160, 160))
        #
        # _, contours, _ = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #
        # center_list = []
        # rad_list = []
        # contour_list = []
        # dist_thresh = 2
        # rad_thresh = 10
        # for contour in contours:
        #     (x, y), radius = cv2.minEnclosingCircle(contour)
        #     sum_diff = 0
        #     for con in contour:
        #         dist = np.sqrt((con[0][0] - x) ** 2 + (con[0][1] - y) ** 2)
        #         diff = abs(dist - radius)
        #         sum_diff += diff
        #     sum_diff /= len(contour)
        #     # print(sum_diff)
        #     if sum_diff < dist_thresh and radius > rad_thresh:
        #         center_list.append((int(x), int(y)))
        #         rad_list.append(radius)
        #         contour_list.append(contour)

        return center_list
