#!/usr/bin/python3

def assign_joint_value(joints, group):
    # Assign values to joints
    # print(joint_0)
    group.set_max_velocity_scaling_factor(0.1)
    # create variable that stores joint values
    group_variable_values = group.get_current_joint_values()

    for i in range(len(joints)):
        group_variable_values[i] = joints[i]

    # set target joint values for 'manipulator' group
    group.set_joint_value_target(group_variable_values)

    plan1 = group.plan()  # call plan function to plan the path (visualize on rviz)
    group.go(wait=False)  # execute plan on real/simulation (gazebo) robot
    group.stop()
    group.clear_pose_targets()
    # rospy.sleep(5)  # sleep 5 seconds

def relative_pose_target(axis_world, distance, group):
    group.set_max_velocity_scaling_factor(0.1)
    # create a pose variable. The parameters can be seen from "$ rosmsg show Pose"
    pose_target = group.get_current_pose()
    
    axis_map = {'x': 'x', 'y': 'y', 'z': 'z'}
    if axis_world in axis_map:
        setattr(pose_target.pose.position, axis_map[axis_world], getattr(pose_target.pose.position, axis_map[axis_world]) + distance)
    
    # set pose_target as the goal pose of 'manipulator' group
    group.set_pose_target(pose_target)
    plan2 = group.plan()  # call plan function to plan the path
    group.go(wait=False)  # execute plan on real/simulation robot
    group.stop()
    group.clear_pose_targets()
    # rospy.sleep(2)  # sleep 5 seconds

def assign_pose_target(poses, group):
    group.set_max_velocity_scaling_factor(0.1)
    pose_target = group.get_current_pose()

    for key in poses:
        if key in pose_target.pose.position.__slots__:
            setattr(pose_target.pose.position, key, poses[key])
        elif key == "qx":
            setattr(pose_target.pose.orientation, "x", poses[key])
        elif key == "qy":
            setattr(pose_target.pose.orientation, "y", poses[key])
        elif key == "qz":
            setattr(pose_target.pose.orientation, "z", poses[key])
        elif key == "qw":
            setattr(pose_target.pose.orientation, "w", poses[key])
    
    group.set_pose_target(pose_target)
    plan = group.plan()
    group.go(wait=False)
