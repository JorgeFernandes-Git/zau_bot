# Zau Mobile Manipulator

Summary:
* Zau is a mobile manipulator that comprises a UR5 manipulator arm installed on an AGV mobile platform. The system is equipped with multiple sensors (eye-on-hand camera and an AGV camera a.t.m.). The URDF file is a digital twin of the physical robotic system, which can be employed for both research and development purposes.
* This repository conduct several experiments (e0 to e5 a.t.m.) to develop methodologies to calibrate the sensors and the base of the UR5 w.r.t. the AGV. The objective is to enhance the precision and accuracy of tasks like grasping and navigation.
* This calibration process uses ATOM framework (https://github.com/lardemua/atom), a multi-sensor, multi-model calibration tool. As the framework is open-source, a fork of the repository was generated to accommodate alterations in the source code. (https://github.com/lardemua/atom/tree/JorgeFernandes-Git/issue543).

Experiments (more information inside each folder and on issues):
* e0 -  Calibration of an RGB astra camera mounted on the end-effector of the manipulator (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e0_rgb2ee)
* e1 - Single Calibrate a Manipulator with RGB astra camera on the end-effector, mounted on top of an AGV (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e1_arm2agv)
* e2 - Simultaneously calibrate a Manipulator with RGB astra camera on the end-effector, mounted on top of an AGV (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e2_arm2agv_rgb2ee)
* e3 - Calibration of an RGB astra camera mounted on the AGV (sensor in motion calibration) (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e3_rgb2agv)
* e4 - Simultaneous calibration of a Mobile Manipulator with two cameras (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e4_DualRGB)
* e5 - Full calibration of Mobile Manipulator - 3 transformations with 2 sensors (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e5_DualRGB_arm2agv)

___________________________ 
Zau digital twin (eye-on-hand camera and AGV camera):

![main_1_1](https://user-images.githubusercontent.com/80167550/222421938-7b4aa6b8-9f18-4553-bdb7-2e682504edb9.png)
![main_2_1](https://user-images.githubusercontent.com/80167550/222424085-79951101-608f-498c-85dc-ee28ccb2d898.png)
![main_3_1](https://user-images.githubusercontent.com/80167550/222424124-0a9370b2-8790-488b-8561-840a8dbe0ffb.png)
![main_gazebo_1](https://user-images.githubusercontent.com/80167550/222975895-05caedc7-14b8-49a1-9ab3-52771f0c6194.png)

___________________________

## Installation:

Clone repository:

    cd <path_to_catkin_ws>/src
    git clone https://github.com/JorgeFernandes-Git/zau_bot.git

Install packages:

    sudo apt install ros-<version>-moveit*
    sudo apt install ros-<version>-warehouse-ros*
    sudo apt install ros-<version>-joint-trajectory-controller

Add to .bashrc:

    export ROS_BAGS="/home/<username>/bagfiles"
    export ATOM_DATASETS="/home/<username>/datasets"

___________________________
## Commands:

Launch Zau on calibration studio to calibrate (default world):

    roslaunch zau_bot_bringup zau_bot_bringup.launch calibration_pattern:=true

Launch teleop:

    roslaunch zau_bot_bringup my_teleop.launch

Launch manipulator autonomous movements (default pattern position):

    rosrun zau_bot_bringup auto_moves -yaw 3.1

Launch record data for full calibration (two cameras and odometry):

    roslaunch e4_dualrgb_record_bag record_sensor_data.launch 

___________________________

Launch only the calibration studio (to calibrate a different robot):

    roslaunch zau_bot_bringup calibration_studio.launch

## Simulation:

Teleop movement:

https://user-images.githubusercontent.com/93128909/198751405-d87c7601-d116-4c14-8328-ffaed76ca632.mp4

Motion planning (MoveIt):

https://user-images.githubusercontent.com/93128909/198751449-e8f088d5-c962-43c5-984a-b119a0b9828a.mp4
