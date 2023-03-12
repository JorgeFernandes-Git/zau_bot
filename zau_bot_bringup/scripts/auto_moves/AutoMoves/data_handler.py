#!/usr/bin/python3

import random
import cv2
import rospy
from cv_bridge import CvBridge, CvBridgeError
from pattern import detect_pattern, draw_keypoints
from moveit_commands_to_arm import assign_pose_target
from euler_to_quaternion import euler_to_quaternion

class DataHandler:
    def __init__(self, args, group) -> None:
        self.img_arm_data = None
        self.arm_state_data = 'state: "IDLE"'
        self.bridge = CvBridge()
        self.args = args
        self.group = group
    
    def moveit_feedback(self, data) -> None:
        self.arm_state_data = data.feedback

    def camera_arm_feedback(self, data):
        self.img_arm_data = data
        self.process_data()

    def process_data(self) -> None:
        if self.img_arm_data is not None:
            try:
                self.camera_arm_process()
            except CvBridgeError as e:
                print(e)

    def camera_arm_process(self) -> None:
        # print(self.img_arm_data)
        img = self.bridge.imgmsg_to_cv2(self.img_arm_data, desired_encoding='bgr8')
        result = detect_pattern(img, equalize_histogram=False)
        detected_point = draw_keypoints(img, result)

        # print(self.arm_state_data)

        if str(self.arm_state_data) == 'state: "IDLE"':
            if detected_point > 40:
                rospy.sleep(5)
            
            self.move_arm_to_new_pose()

        cv2.imshow("image", img)
        k = cv2.waitKey(1) & 0xFF

    def move_arm_to_new_pose(self) -> None:
        poses = self.arm_poses()
        assign_pose_target(poses, self.group)

    def arm_poses(self) -> dict:
        x = random.uniform(-0.1,0.3)
        y = random.uniform(-0.5,0.5)
        z = random.uniform(0.8,1.3)
        roll = random.uniform(-0.3,0.3)
        pitch = random.uniform(-0.3,0.3)
        yaw = self.args['yaw']
        qx, qy, qz, qw = euler_to_quaternion(roll, pitch, yaw)
        return {'x': x,
                'y': y,
                'z': z,
                'qx': qx,
                'qy': qy,
                'qz': qz,
                'qw': qw}