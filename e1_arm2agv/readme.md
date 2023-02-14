## Single Calibrate a Manipulator with RGB astra camera on the end-effector, mounted on top of an AGV.
Transformation from camera to end-effector was was previously calculated in e0_rgb2ee.
_______________________________

Calibration results: 

## Commands:

Record bag file:

    roslaunch e0_rgb2ee_calibration record_sensor_data.launch

Play dataset

    roslaunch e1_arm2agv_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e1_arm2agv/dataset.json -ow