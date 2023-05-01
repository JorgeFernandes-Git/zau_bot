# Zau eye on hand camera calibration

## Record dataset

    roslaunch zau_eye_on_hand_calibration collect_data.launch output_folder:=$ATOM_DATASETS/zau_eye_on_hand_v2 overwrite:=true

## Dataset playback


    roslaunch zau_eye_on_hand_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/zau_eye_on_hand/dataset.json -ow

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