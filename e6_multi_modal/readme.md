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
|    000     |    0.5561   |     0.5320     |    0.0064    |
|    001     |    0.5263   |     0.5386     |    0.0064    |
|    002     |    0.5308   |     0.5346     |    0.0065    |
|    003     |    0.4642   |     0.5373     |    0.0060    |
|    004     |    0.6165   |     0.5390     |    0.0066    |
|    005     |    0.4792   |     0.5398     |    0.0062    |
|    007     |    0.5577   |     0.7607     |    0.0064    |
|    008     |    0.5560   |     0.6584     |    0.0062    |
|    009     |    1.0303   |     0.6434     |    0.0062    |
|    010     |    0.7677   |     0.6300     |    0.0067    |
|    011     |    0.5588   |     0.6184     |    0.0064    |
|    012     |    0.4670   |     0.6080     |    0.0064    |
|    013     |    0.2949   |     0.4613     |    0.0064    |
|    014     |    0.3067   |     0.4478     |    0.0067    |
|    015     |    0.2968   |     0.2064     |    0.0063    |
|    016     |    4.0170   |     3.8441     |    0.0088    |
|    017     |    3.0238   |     3.0225     |    0.0086    |
|    018     |    0.4867   |     0.5048     |    0.0064    |
|    019     |    0.4108   |     0.6225     |    0.0069    |
|    020     |    0.3086   |     0.4979     |    0.0064    |
|    021     |    0.3161   |     0.4620     |    0.0062    |
|    022     |    0.3217   |     0.4307     |    0.0069    |
|    023     |    0.8256   |     0.4673     |    0.0062    |
|    024     |    0.4339   |     0.4116     |    0.0061    |
|    025     |    0.7071   |     0.6554     |    0.0065    |
|    026     |    0.5492   |     0.9245     |    0.0063    |
|    027     |    0.6525   |     1.0532     |    0.0062    |
|    028     |    0.9089   |     1.1664     |    0.0061    |
|    029     |    0.7902   |     1.1462     |    0.0063    |
|    030     |    0.7275   |     1.0891     |    0.0065    |
|  **Averages**  |    **0.7496**   |     **0.8185**     |    **0.0065**    |

_______________________________

## Calibration tree and Transformations:

![summary](https://user-images.githubusercontent.com/80167550/223447591-e07abebf-9583-4fc2-937f-a91a2f06a977.png)

![e6_mm_calibration](https://user-images.githubusercontent.com/80167550/223447764-ef7f8521-8503-4577-a358-ad14ccffb4d5.png)


_______________________________

## Videos:
* Run calibration: https://youtu.be/VhpOOK9JeKo
* Correct Lidar data: https://youtu.be/OVAJ7TNBcyc
* Annotate pattern borders: https://youtu.be/qSARjm1FXBg
* Evaluation procedure:
    * Lidar to AGV camera: https://youtu.be/BIjOIW_AI8I
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

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e6_mm/dataset_corrected.json -v -rv -si -vo -nig 0.1 0.1 -oj atom_calibration_nig_0.1_0.1.json -csf "lambda name: int(name) not in [6, 6]"

_______________________________

Run evaluations:

Annotate images:

    rosrun atom_evaluation annotate_pattern_borders_in_rgb -d ~/datasets/e6_mm/dataset_corrected.json -si -cs camera_mb

**rgb to rgb**

    rosrun atom_evaluation rgb_to_rgb_evaluation -train_json ~/datasets/e6_mm/atom_calibration_nig_0.1_0.1.json -test_json ~/datasets/e6_mm/dataset_corrected.json -ss camera -st camera_mb -si

**lidar to rgb**

    rosrun atom_evaluation lidar_to_rgb_evaluation -train_json /home/jorge/datasets/e6_mm/atom_calibration_nig_0.1_0.1.json -test_json /home/jorge/datasets/e6_mm/dataset_corrected.json -cs camera_mb -rs velodyne -si

**ground truth frame**

    rosrun atom_evaluation ground_truth_frame_evaluation -train_json  /home/jorge/datasets/e6_mm/atom_calibration_nig_0.1_0.1.json -test_json /home/jorge/datasets/e6_mm/dataset_corrected.json