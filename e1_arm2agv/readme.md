## Single Calibrate a Manipulator with RGB astra camera on the end-effector, mounted on top of an AGV. (Unsuccessful)
Transformation from camera to end-effector was was previously calculated in e0_rgb2ee.
_______________________________

Summary: 
* Using ATOM framework to manipulator to AGV calibration. 
* Aims to find the transformation of the base's manipulator w.r.t the AGV.
* The camera used was a depth astra. 
* The calibration used a total of 50 collections.
* The optimization didn't converge (see videos).
_______________________________

![e1_arm2agv_graph](https://user-images.githubusercontent.com/80167550/218805628-258351d5-0e79-447c-b5e4-60f4745cb0d9.png)
![e1_arm2agv](https://user-images.githubusercontent.com/80167550/218804005-4002dbdc-bc06-4bbc-9bda-8e96d2b83538.png)
![e2_arm2agv_rgb2ee_2](https://user-images.githubusercontent.com/80167550/218804070-d13b14cf-8128-4003-8b71-df22493c8a3a.png)
_______________________________

## ATOM config file:
This is how I define in the config.yaml 'sensor' part:
https://github.com/JorgeFernandes-Git/zau_bot/blob/c2133a59d0ac973aba61e6209d5c1a353ebc2550/e1_arm2agv/e1_arm2agv_calibration/calibration/config.yml#L75-L81
_______________________________

## Videos
* Set Initial Estimate: https://youtu.be/DbFU10SCOL8
* Run Calibration: https://youtu.be/JhHzo6qumo0 

## Commands:
Record bag file:

    roslaunch e0_rgb2ee_record_bag record_sensor_data.launch

Run script for move the manipulator:

    rosrun zau_bot_bringup execute_trajectories 

Play dataset

    roslaunch e1_arm2agv_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e1_arm2agv/dataset.json -ow