## Configure calibration package

    rosrun atom_calibration configure_calibration_pkg -n zau_full_calibration -utf

## Collect data

    roslaunch zau_full_calibration collect_data.launch output_folder:=~/datasets/zau_full_calibration_vf overwrite:=true

## Dataset playback

    roslaunch zau_full_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json $ATOM_DATASETS/zau_full_calibration/dataset.json -ow

## Run the calibration

    roslaunch zau_full_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/zau_full_calibration_vf/dataset.json -v -rv -si -csf "lambda name: int(name) not in [7, 22, 23, 24]"


