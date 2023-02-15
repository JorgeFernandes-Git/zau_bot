## Calibration of an RGB astra camera mounted on the end-effector of the manipulator. https://github.com/JorgeFernandes-Git/zau_bot/issues/3
_______________________________

Summary: 
* Using ATOM framework to perform eye-on-hand calibration. 
* Eye-on-hand is a calibration problem that aims to determine the transformastion between a camera and a end-effetor.
* The camera used was a depth astra. 
* The calibration used a total of 15 collections.
* The output is a URDF file with the optimized pose of the camera related to the end-effector. 

_______________________________
Launch optimized URDF mobile manipulator (AGV connected to world, it will not move):

    roslaunch e0_rgb2ee_optimized e0_rgb2ee_optimized.launch 

_______________________________

Evaluate two datasets:

    rosrun atom_evaluation cross_collection_rgb_to_rgb_evaluation -train_json ~/datasets/e0_rgb2ee_v2/atom_calibration.json -test_json ~/datasets/e0_rgb2ee/dataset.json -ss camera -st camera -si -wf world

Evaluation procedure: https://youtu.be/7iKA81g-aNs

Evaluation Results: https://github.com/JorgeFernandes-Git/zau_bot/blob/main/e0_rgb2ee/results.md

_______________________________

Calibration Results per collection:

| Collection | Camera (px) |
| :-------------: | :-------------: |
| 000           |   0.2187   | 
| 001           |   0.1825   | 
| 002           |   0.2116   | 
| 003           |   0.2547   |
| 004           |   0.1240   | 
| 005           |   0.1246   | 
| 006           |   0.1971   | 
| 007           |   0.1359   | 
| 008           |   0.1217   | 
| 009           |   0.1233   | 
| 010           |   0.1738   | 
| 011           |   0.1166   | 
| 012           |   0.2856   | 
| 013           |   0.1688   | 
| 014           |   0.3206   | 
| 015           |   0.2657   | 
| **Averages**  |  **0.1891**   |

_______________________________

## Calibration tree and Transformation RGB to End-Effector:

![T_rgb_ee_graph](https://user-images.githubusercontent.com/80167550/218584440-05ee7397-67bf-46c9-8830-006ab8abd658.png)
![T_rgb_ee](https://user-images.githubusercontent.com/80167550/218582316-1aafdbf4-8685-4c01-b51a-128b5d56c6fa.png)
![T_rgb_ee_objs](https://user-images.githubusercontent.com/80167550/218583118-9471e054-4b94-443e-b9b6-04141e8bef9c.png)

_______________________________

## Videos:

Record bag file: https://youtu.be/mwAtXrQm8c4

Data collection: https://youtu.be/W_WFggovr9w

Run calibration: https://youtu.be/PX7BX9yNxMc

Evaluation procedure: https://youtu.be/7iKA81g-aNs

_______________________________

## Commands:

Record bag file:

    roslaunch e0_rgb2ee_calibration record_sensor_data.launch

Run script for move the manipulator:

    rosrun zau_bot_bringup execute_trajectories 

Play dataset:

    roslaunch e0_rgb2ee_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e0_rgb2ee/dataset.json -ow

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e0_rgb2ee_v2/dataset.json -ow

Run calibration:

    roslaunch e0_rgb2ee_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e0_rgb2ee_v2/dataset.json -v -rv -si -vo





