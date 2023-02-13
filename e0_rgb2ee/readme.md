Play dataset:

    roslaunch e0_rgb2ee_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e0_rgb2ee/dataset.json -ow

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e0_rgb2ee_v2/dataset.json -ow

Run calibration:

    roslaunch e0_rgb2ee_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e0_rgb2ee_v2/dataset.json -v -rv -si -vo


Output:

+------------+-------------+
| Collection | camera (px) |
+------------+-------------+
|    000     |    0.2187   |
|    001     |    0.1825   |
|    002     |    0.2116   |
|    003     |    0.2547   |
|    004     |    0.1240   |
|    005     |    0.1246   |
|    006     |    0.1971   |
|    007     |    0.1359   |
|    008     |    0.1217   |
|    009     |    0.1233   |
|    010     |    0.1738   |
|    011     |    0.1166   |
|    012     |    0.2856   |
|    013     |    0.1688   |
|    014     |    0.3206   |
|    015     |    0.2657   |
|  Averages  |    0.1891   |


