#!/usr/bin/env python3

import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import message_filters
import cv2
from pattern import detect_pattern, draw_keypoints

def read_cameras(init_params):
    img_arm = message_filters.Subscriber(init_params['camera_arm'], Image)
    img_agv = message_filters.Subscriber(init_params['camera_AGV'], Image)

    # Synchronize images
    ts = message_filters.ApproximateTimeSynchronizer([img_arm, img_agv], queue_size=10, slop=0.5)
    ts.registerCallback(image_callback)
    rospy.spin()

def image_callback(img_arm, img_agv):
    br = CvBridge()
    rospy.loginfo("receiving frame")
    image_arm = br.imgmsg_to_cv2(img_arm)
    image_agv = br.imgmsg_to_cv2(img_agv)

    result_arm = detect_pattern(image_arm, equalize_histogram=False)
    detected_point_arm = draw_keypoints(image_arm, result_arm)

    result_agv = detect_pattern(image_agv, equalize_histogram=False)
    detected_point_agv = draw_keypoints(image_agv, result_agv)

    cv2.namedWindow('image_arm')
    cv2.namedWindow('image_agv')

    cv2.imshow('image_arm', image_arm)
    cv2.imshow('image_agv', image_agv)

    k = cv2.waitKey(50) & 0xFF # if the script get stalled, adjust this rate

def initialize():
    camera_arm = rospy.get_param('/camera_arm')
    camera_AGV = rospy.get_param('/camera_AGV')
    rospy.init_node('dual_cam', anonymous=True)

    return {'camera_arm': camera_arm,
            'camera_AGV': camera_AGV}

if __name__ == '__main__':
    init_params = initialize()
    read_cameras(init_params)
