# Calibrate multi-modal Mobile Manipulator

![e6_multi_modal](https://user-images.githubusercontent.com/80167550/223143282-6aba8fe6-3a37-46c6-9d52-dcbfe30af1a1.png)

_______________________________

Summary: 
* Using ATOM framework to perform full calibration of a mobile manipulator with two cameras, one on the AGV and other on the end-effector of the manipulator and one 3D lidar on the AGV.
* Aims to determine the transformations: 
    * Manipulator arm base w.r.t. the AGV.
    * RGB1 w.r.t. the AGV. 
    * RGB2 w.r.t. the end-effector.
    * 3D Lidar w.r.t. the AGV
* The cameras used was a depth astra.
* The 3D lidar is a velodyne VLP 16.
* The calibration used a total of 30 collections.
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

| Collection | camera (px) | camera_mb (px) | velodyne (m) |
|------------|-------------|----------------|--------------|
|    000     |    1.1558   |     1.0690     |    0.0071    |
|    001     |    1.3319   |     1.0590     |    0.0073    |
|    002     |    1.2099   |     1.0633     |    0.0073    |
|    003     |    1.6119   |     1.0593     |    0.0068    |
|    004     |    1.5594   |     1.0563     |    0.0074    |
|    005     |    2.8226   |     1.0568     |    0.0070    |
|    006     |   21.1701   |    17.5368     |    0.0802    |
|    007     |    3.1967   |     1.1614     |    0.0071    |
|    008     |    2.6342   |     1.2181     |    0.0070    |
|    009     |    1.6312   |     1.2228     |    0.0071    |
|    010     |    1.7702   |     1.2297     |    0.0078    |
|    011     |    1.6932   |     1.2332     |    0.0073    |
|    012     |    2.3250   |     1.2391     |    0.0072    |
|    013     |    0.9602   |     0.7900     |    0.0074    |
|    014     |    0.8608   |     0.7799     |    0.0075    |
|    015     |    1.7500   |     1.2502     |    0.0071    |
|    016     |    5.2870   |     5.6779     |    0.0149    |
|    017     |    2.2777   |     2.0858     |    0.0072    |
|    018     |    1.9962   |     1.7309     |    0.0077    |
|    019     |    1.0274   |     0.6488     |    0.0076    |
|    020     |    0.9202   |     0.6315     |    0.0071    |
|    021     |    0.8286   |     0.6470     |    0.0070    |
|    022     |    1.0424   |     0.6309     |    0.0077    |
|    023     |    1.9838   |     1.4425     |    0.0069    |
|    024     |    1.8230   |     0.6651     |    0.0068    |
|    025     |    1.5983   |     1.4727     |    0.0112    |
|    026     |    1.3210   |     1.1720     |    0.0098    |
|    027     |    1.1986   |     1.1736     |    0.0100    |
|    028     |    1.3880   |     1.1377     |    0.0096    |
|    029     |    1.5159   |     1.1121     |    0.0099    |
|    030     |    2.0185   |     1.1501     |    0.0096    |
|  Averages  |    2.3842   |     1.7872     |    0.0104    |

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

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e6_mm/dataset_corrected.json 

Run calibration (2 terminals):

    roslaunch e6_mm_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e6_mm/dataset_corrected.json -v -rv -si -vo -nig 0.1 0.1 -oj atom_calibration_nig_0.1_0.1.json

_______________________________

Run evaluations:

**rgb to rgb**


**lidar to rgb**


**ground truth frame**