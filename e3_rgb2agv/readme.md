## Calibration of an RGB astra camera mounted on the AGV (sensor in motion calibration).
_______________________________

## Commands:

Launch AGV for calibration:

    roslaunch zau_bot_bringup moving_base_odom.launch calibration_pattern:=true

Launch teleop to control the AGV through the keyboard:

    roslaunch zau_bot_bringup my_teleop.launch 

Record bag file:

    roslaunch e3_rgb2agv_record_bag record_sensor_data.launch

## Calibration using the transformations in the bagfile instead of the ones produced by the xacro description:

    rosrun atom_calibration configure_calibration_pkg -n e3_rgb2agv_calibration -utf

 