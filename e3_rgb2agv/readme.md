## Calibration of an RGB astra camera mounted on the AGV (sensor in motion calibration). https://github.com/JorgeFernandes-Git/zau_bot/issues/6
_______________________________

Summary: 
* Using ATOM framework to perform RGB camera to AGV calibration. 
* Aims to determine the transformation of the camera w.r.t. the AGV.
* The camera used was a depth astra. 
* The calibration used a total of 35 collections.
* The output is a URDF file with the optimized pose of the camera related to the AGV. 
_______________________________

![summary tree](https://user-images.githubusercontent.com/80167550/219402639-d1685718-bc4e-4581-922e-daabb3d56d81.png)
![e3_rgb2agv](https://user-images.githubusercontent.com/80167550/219379619-d4686598-b031-4169-87ab-eb876562a648.png)
![e3_rgb2agv_2](https://user-images.githubusercontent.com/80167550/219379671-8de664b2-4733-48cf-a07e-b18378186642.png)
_______________________________

## Commands:
Launch AGV for calibration:

    roslaunch zau_bot_bringup moving_base_odom.launch calibration_pattern:=true

Launch teleop to control the AGV through the keyboard:

    roslaunch zau_bot_bringup my_teleop.launch 

Record bag file:

    roslaunch e3_rgb2agv_record_bag record_sensor_data.launch

## Calibration using the transformations in the bagfile instead of the ones produced by the xacro description:

    rosrun atom_calibration configure_calibration_pkg -n e3_rgb2agv_calibration -utf
_______________________________

## Videos:
Recording bag file: https://youtu.be/q7h5tL1suVE
