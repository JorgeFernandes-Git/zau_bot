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

## Results

| Collection | cam_1 (px) | cam_2 (px) |
+------------+------------+------------+
|    000     |  13.7205   |  15.2582   |
|    001     |  46.8454   |  15.1646   |
|    002     |  18.0822   |  15.4222   |
|    003     |  38.8908   |  15.6728   |
|    004     |  39.0398   |  15.5057   |
|    005     |  27.8788   |  17.5612   |
|    006     |  32.4766   |  16.7013   |
|    008     |  38.0617   |  17.3372   |
|    009     |  38.1324   |  16.9963   |
|    010     |  19.2855   |  13.1992   |
|    011     |  30.1057   |  13.4610   |
|    012     |  40.5668   |  15.5665   |
|    013     |  32.1684   |  14.9359   |
|    014     |  44.5186   |  14.9171   |
|    015     |  47.2287   |  12.1561   |
|    016     |  32.4744   |  12.3493   |
|    017     |  26.1803   |  12.0615   |
|    018     |  20.1690   |  12.2438   |
|    019     |  19.0965   |  12.1519   |
|    020     |  23.2517   |  11.1018   |
|    021     |  20.8751   |  11.2431   |
|  Averages  |  30.9071   |  14.3337   |


