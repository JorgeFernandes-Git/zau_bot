## Calibration of an RGB astra camera mounted on the AGV (sensor in motion calibration). https://github.com/JorgeFernandes-Git/zau_bot/issues/6
_______________________________

Summary: 
* Using ATOM framework to perform RGB camera to AGV calibration. 
* Aims to determine the transformation of the camera w.r.t. the AGV.
* The camera used was a depth astra. 
* The calibration used a total of 27 collections.
* The output is a URDF file with the optimized pose of the camera related to the AGV. 
_______________________________

Launch optimized ...

_______________________________

Evaluate two datasets: ...

_______________________________

## Calibration Results per collection:
| Collection | Camera (px) |
| :-------------: | :-------------: |
|    000     |     1.3215     |
|    001     |     0.5251     |
|    002     |     2.0025     |
|    003     |     1.4960     |
|    004     |     5.3229     |
|    005     |     1.0206     |
|    006     |     1.1486     |
|    007     |     1.9128     |
|    008     |     0.9098     |
|    009     |     0.7199     |
|    010     |     1.1669     |
|    011     |     0.5040     |
|    012     |     2.3567     |
|    013     |     0.3553     |
|    014     |     1.1806     |
|    015     |     1.5711     |
|    016     |     1.2563     |
|    017     |     0.9612     |
|    018     |     1.8731     |
|    019     |     1.0544     |
|    020     |     1.7724     |
|    021     |     2.5432     |
|    022     |     2.3654     |
|    023     |     2.2581     |
|    025     |     7.7681     |
|    026     |    15.2750     |
|    027     |     3.4709     |
|  **Averages**  |     **2.3745**     |
_______________________________

## Calibration tree and Transformation RGB to AGV:
![summary tree](https://user-images.githubusercontent.com/80167550/219402639-d1685718-bc4e-4581-922e-daabb3d56d81.png)
![e3_rgb2agv](https://user-images.githubusercontent.com/80167550/219379619-d4686598-b031-4169-87ab-eb876562a648.png)
![e3_rgb2agv_2](https://user-images.githubusercontent.com/80167550/219379671-8de664b2-4733-48cf-a07e-b18378186642.png)
_______________________________

## Videos:
Recording bag file: https://youtu.be/q7h5tL1suVE
Playback dataset: https://youtu.be/sh7AZn0dUgA
_______________________________

## Configure the calibration using the transformations in the bagfile instead of the ones produced by the xacro description:

    rosrun atom_calibration configure_calibration_pkg -n e3_rgb2agv_calibration -utf

## Commands:
Launch AGV for calibration:

    roslaunch zau_bot_bringup moving_base_odom.launch calibration_pattern:=true

Launch teleop to control the AGV through the keyboard:

    roslaunch zau_bot_bringup my_teleop.launch 

Record bag file:

    roslaunch e3_rgb2agv_record_bag record_sensor_data.launch

Playback dataset for calibration (2 terminals):

    roslaunch e3_rgb2agv_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e3_rgb2agv/dataset.json -ow

Run calibration (2 terminals):

    roslaunch e0_rgb2ee_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e3_rgb2agv/dataset.json -v -rv -si -vo


