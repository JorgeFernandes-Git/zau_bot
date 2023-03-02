# Zau Mobile Manipulator

Summary:
* Zau is a mobile manipulator that comprises a UR5 manipulator arm installed on an AGV mobile platform. The system is equipped with multiple sensors (eye-on-hand camera and an AGV camera a.t.m.). The URDF file is a digital twin of the physical robotic system, which can be employed for both research and development purposes.
* This repository conduct several experiments (e0 to e5 a.t.m.) to develop methodologies to calibrate the sensors and the base of the UR5 w.r.t. the AGV. The objective is to enhance the precision and accuracy of tasks like grasping and navigation.
* This calibration process uses ATOM framework (https://github.com/lardemua/atom), a multi-sensor, multi-model calibration tool. As the framework is open-source, a fork of the repository was generated to accommodate alterations in the source code. (https://github.com/lardemua/atom/tree/JorgeFernandes-Git/issue543).

Experiment (more information inside each folder and on issues):
* e0 -  Calibration of an RGB astra camera mounted on the end-effector of the manipulator (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e0_rgb2ee)
* e1 - Single Calibrate a Manipulator with RGB astra camera on the end-effector, mounted on top of an AGV (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e1_arm2agv)
* e2 - Simultaneously calibrate a Manipulator with RGB astra camera on the end-effector, mounted on top of an AGV (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e2_arm2agv_rgb2ee)
* e3 - Calibration of an RGB astra camera mounted on the AGV (sensor in motion calibration) (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e3_rgb2agv)
* e4 - Simultaneous calibration of a Mobile Manipulator with two cameras (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e4_DualRGB)
* e5 - Full calibration of Mobile Manipulator - 3 transformations with 2 sensors (https://github.com/JorgeFernandes-Git/zau_bot/tree/main/e5_DualRGB_arm2agv)

___________________________
Zau digital twin:

![main_1](https://user-images.githubusercontent.com/80167550/222421512-7630ad23-9ee7-4366-8ae4-6e76ee4b4dad.png)

___________________________
WORK IN PROGRESS:

## Launching zau_bot

Rviz:

    roslaunch zau_bot_bringup zau_bot_bringup.launch

Rviz with Gazebo:

    roslaunch zau_bot_bringup zau_bot_bringup.launch gui:=true

Teleop:

    roslaunch zau_bot_bringup my_teleop.launch 

![Screenshot](https://github.com/JorgeFernandes-Git/zau_bot/blob/main/zau.png?raw=true)

## Tf Tree

![Screenshot](https://github.com/JorgeFernandes-Git/zau_bot/blob/main/imgs/tf_tree/zau_bot_tf_tree.png?raw=true)

## Simulation:

Teleop movement:

https://user-images.githubusercontent.com/93128909/198751405-d87c7601-d116-4c14-8328-ffaed76ca632.mp4

Motion planning (MoveIt):

https://user-images.githubusercontent.com/93128909/198751449-e8f088d5-c962-43c5-984a-b119a0b9828a.mp4
