# Calibrate multi-modal Mobile Manipulator

![e6_multi_modal](https://user-images.githubusercontent.com/80167550/223143282-6aba8fe6-3a37-46c6-9d52-dcbfe30af1a1.png)

_______________________________

Summary: 
* Using ATOM framework to perform full calibration of a mobile manipulator with two cameras, one on the AGV and other on the end-effector of the manipulator.
* Aims to determine the transformations: 
    * Manipulator arm base w.r.t. the AGV.
    * RGB1 w.r.t. AGV. 
    * RGB2 w.r.t. end-effector.
* The cameras used was a depth astra. 
* The calibration used a total of 79 collections.
* The output is a URDF file with the optimized poses of the sensors.
_______________________________

Launch optimized URDF:

_______________________________

Evaluate two datasets:

Summary:

**Eye-on-hand camera to AGV camera evaluation**:


**AGV camera to Eye-on-hand camera evaluation**:


**Output with noise initial guess `nig` 0.1 0.1:**



**Output without noise initial guess `nig`:**


_______________________________

## Calibration Results per collection:


_______________________________

## Calibration tree and Transformations:


_______________________________

## Videos:
* Set initial estimate: 
* Run calibration: 
* Evaluation procedure: 
_______________________________

## Configure the calibration using the transformations in the bagfile instead of the ones produced by the xacro description:

    rosrun atom_calibration configure_calibration_pkg -n e6_mm_calibration -utf

## Commands:
Launch AGV for calibration:

    roslaunch zau_bot_bringup zau_bot_bringup

Launch teleop to control the AGV through the keyboard:

    roslaunch zau_bot_bringup my_teleop.launch 

Record bag file:

    roslaunch e6_mm_record_bag record_sensor_data.launch

Collect dataset for calibration:

    roslaunch e6_mm_calibration collect_data.launch output_folder:=$ATOM_DATASETS/e6_mm overwrite:=true

Playback dataset for calibration (2 terminals):

    roslaunch e6_mm_calibration dataset_playback.launch 

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e6_mm/dataset.json 

Run calibration (2 terminals):

    roslaunch e6_mm_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e6_mm/dataset_corrected.json -v -rv -si -vo -nig 0.1 0.1 -oj atom_calibration_nig_0.1_0.1.json

_______________________________

Run evaluations:

**rgb to rgb**



**sensor to frame**



**link to ground truth**



**lidar to rgb**


