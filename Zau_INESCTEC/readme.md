# Zau eye on hand camera calibration

## Record dataset

    roslaunch zau_eye_on_hand_calibration collect_data.launch output_folder:=$ATOM_DATASETS/zau_eye_on_hand overwrite:=true bag_rate:=0.5

## Dataset playback


    roslaunch zau_eye_on_hand_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/zau_eye_on_hand_v2/dataset.json -ow

## Run calibration

    roslaunch zau_eye_on_hand_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/zau_eye_on_hand_v2/dataset.json -v -rv -si -vo


| Collection | camera (px) |
|------------|-------------|
|    000     |   86.3182   |
|    001     |   75.1172   |
|    002     |   31.7358   |
|    003     |   61.2361   |
|    004     |   41.8608   |
|    005     |   46.6584   |
|    006     |   41.8746   |
|    007     |   117.7450  |
|    008     |   53.3336   |
|  Averages  |   61.7644   |
