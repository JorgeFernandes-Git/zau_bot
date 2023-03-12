#!/usr/bin/python3

import rospy
import sys
import moveit_commander
import moveit_msgs.msg
import tf
from geometry_msgs.msg import Twist

def get_camera_nodes():
    camera_arm = rospy.remap_name('camera/rgb/image_raw')
    camera_AGV = rospy.remap_name('camera_mb/rgb/image_raw')
    return camera_arm, camera_AGV

def get_cmd_vel_node():
    cmd_vel_node = rospy.remap_name('cmd_vel')
    return cmd_vel_node

def cmd_vel_publisher():
    cmd_vel_node = get_cmd_vel_node()
    cmd_vel_pub = rospy.Publisher(cmd_vel_node, Twist, queue_size=10)
    return cmd_vel_node, cmd_vel_pub

def moveit_init(robot_name):
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group = moveit_commander.MoveGroupCommander(robot_name)
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=10)
    return robot, scene, group, display_trajectory_publisher

def get_tfs():
    tf_listener = tf.TransformListener()
    tf_broadcaster = tf.TransformBroadcaster()
    return tf_listener, tf_broadcaster

def start_main_node():
    rospy.init_node('autonomous_movements', anonymous=True)

def move_group_nodes():
    move_group_feedback_node = rospy.remap_name('move_group/feedback')
    return move_group_feedback_node