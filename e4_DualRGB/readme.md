## Simultaneous calibration of a Mobile Manipulator with two cameras. ()
_______________________________

Summary: 
* Using ATOM framework to perform simultaneous calibration of a mobile manipulator with two cameras. One on the AGV and other on the end-effector of the manipulator.
* Aims to determine the transformations RGB1 w.r.t. AGV and RGB2 w.r.t. end-effector.
* The cameras used was a depth astra. 
* The calibration used a total of xxxxxxx collections.
* The output is a URDF file with the optimized poses of the sensors.
_______________________________

Launch optimized URDF:

    roslaunch 

_______________________________

Evaluate two datasets: ...

_______________________________

## Calibration Results per collection:

_______________________________

## Videos:
* Recording bag file: 
* Playback dataset: 
* Run calibration: 
* Evaluation procedure:
_______________________________

## Calibration tree and Transformation RGB to AGV:

_______________________________

## Configure the calibration using the transformations in the bagfile instead of the ones produced by the xacro description:

    rosrun atom_calibration configure_calibration_pkg -n e4_dualrgb_calibration -utf

## Commands:
Launch AGV for calibration:

    roslaunch zau_bot_bringup zau_bot_bringup

Launch teleop to control the AGV through the keyboard:

    roslaunch zau_bot_bringup my_teleop.launch 

Record bag file:

    roslaunch e4_dualrgb_record_bag record_sensor_data.launch

Playback dataset for calibration (2 terminals):

Run calibration (2 terminals):
