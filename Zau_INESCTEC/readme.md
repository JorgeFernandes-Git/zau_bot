# Zau eye on hand camera calibration

Summary:

Using ATOM framework to perform eye-on-hand calibration.
Eye-on-hand is a calibration problem that aims to determine the transformation between a camera and a end-effector.
The camera used was a intel realsense d415.
The calibration used a total of 18 collections.
The output is a URDF file with the optimized pose of the camera related to the end-effector.

________________________

## Launch optimized robot urdf

    roslaunch zau_eye_on_hand_optimized zau_eye_on_hand_optimized.launch

________________________

## Calibration tree

summary: https://github.com/JorgeFernandes-Git/zau_bot/blob/Zau_INESCTEC_eye_on_hand_calibration/Zau_INESCTEC/zau_eye_on_hand_calibration/calibration/summary.pdf

________________________

## Calibration results

evaluations: https://github.com/JorgeFernandes-Git/zau_bot/blob/Zau_INESCTEC_eye_on_hand_calibration/Zau_INESCTEC/results.md

________________________

## Record dataset

    roslaunch zau_eye_on_hand_calibration collect_data.launch output_folder:=$ATOM_DATASETS/zau_eye_on_hand_v2 overwrite:=true

________________________

## Dataset playback

    roslaunch zau_eye_on_hand_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/zau_eye_on_hand/dataset.json -ow

________________________

## Run calibration

    roslaunch zau_eye_on_hand_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/zau_eye_on_hand_v3/dataset.json -v -rv -si -vo -csf "lambda name: int(name) not in [0, 10, 16]"


| Collection | camera (px) |
|------------|-------------|
|    001     |    1.5224   |
|    002     |    1.4546   |
|    003     |    0.8906   |
|    004     |    1.4131   |
|    005     |    1.8743   |
|    006     |    1.7515   |
|    007     |    1.9140   |
|    008     |    1.4517   |
|    009     |    1.0305   |
|    011     |    1.9130   |
|    012     |    1.3474   |
|    013     |    1.3594   |
|    014     |    1.4301   |
|    015     |    1.2689   |
|    017     |    1.5659   |
|    018     |    1.3369   |
|    019     |    1.4187   |
|    020     |    1.6197   |
|  Averages  |    1.4757   |