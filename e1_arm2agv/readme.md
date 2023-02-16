## Single Calibrate a Manipulator with RGB astra camera on the end-effector, mounted on top of an AGV.
Transformation from camera to end-effector was was previously calculated in e0_rgb2ee.
_______________________________

Calibration results: 

## Commands:

Record bag file:

    roslaunch e0_rgb2ee_record_bag record_sensor_data.launch

Run script for move the manipulator:

    rosrun zau_bot_bringup execute_trajectories 

Play dataset

    roslaunch e1_arm2agv_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e1_arm2agv/dataset.json -ow