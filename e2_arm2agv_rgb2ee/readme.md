## Simultaneously calibrate a Manipulator with RGB astra camera on the end-effector, mounted on top of an AGV.
_______________________________

## Commands:

Record bag file:

    roslaunch e0_rgb2ee_calibration record_sensor_data.launch

Run script for move the manipulator:

    rosrun zau_bot_bringup execute_trajectories 