## Full calibration of Mobile Manipulator - 3 transformations with 2 sensors (Successful) https://github.com/JorgeFernandes-Git/zau_bot/issues/9 https://github.com/lardemua/atom/issues/543
_______________________________

Summary: 
* Using ATOM framework to perform full calibration of a mobile manipulator with two cameras, one on the AGV and other on the end-effector of the manipulator.
* Aims to determine the transformations: 
    * Manipulator arm base w.r.t. the AGV.
    * RGB1 w.r.t. AGV. 
    * RGB2 w.r.t. end-effector.
* The cameras used was a depth astra. 
* The calibration used a total of 79 collections.
* The output is a URDF file with the optimized poses of the sensors.
_______________________________

Launch optimized URDF:

    roslaunch e5_dualrgb_arm2agv_optimized e5_dualrgb_arm2agv_optimized.launch
_______________________________

Evaluate two datasets:

Summary:

**Eye-on-hand camera to AGV camera evaluation**:
| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm) | Rot (deg) |
| :-------------: | :---: | :---: | :---: | :---: | :---: |
|   Averages   |   7.4277  |    0.3737   |    7.3985   |  13.9072   |   0.1293  |

**Output with noise initial guess `nig` 0.1 0.1:**
|          Transformation #          | X (mm) |  Y (mm) | Z (mm) | Roll (deg) | Pitch (deg) | Yaw (deg) | Trans (mm) | Rot (deg) |
|---------------------------|---------------|---------------|---------------|------------------------|--------------------------|----------------------|-----------------|---------------|
|       base_link_mb-base_link       | 0.2551 |  1.0701 | 7.5430 |   0.0151   |    0.0013   |   0.0028  |   7.6228   |   0.0154  |
|    camera_link-camera_rgb_frame    | 1.5183 | 24.2693 | 6.4312 |   0.0168   |    0.0303   |   0.0482  |  25.1935   |   0.0595  |
| camera_mb_link-camera_mb_rgb_frame | 0.4289 | 24.2033 | 7.9438 |   0.0048   |    0.0500   |   0.0564  |  25.4772   |   0.0755  |

**Cross collection rgb to rgb evaluations Eye-on-hand camera to Eye-on-hand camera (same sensor)**
| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm)	| Rot (deg) |
|--------------|-----------|-------------|-------------|------------|-----------|
|   Averages   |   0.9757  |    0.3604   |    0.7644   |   2.8479   |   0.1728  |

**Cross collection rgb to rgb evaluations AGV camera to AGV camera (same sensor)**
| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm)	| Rot (deg) |
|--------------|-----------|-------------|-------------|------------|-----------|
|   Averages   |   0.8567  |    0.7164   |    0.2279   |   2.0671   |   0.1048  |

**Cross collection rgb to rgb evaluations Eye-on-hand camera to AGV camera (different sensor)**

| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm)	| Rot (deg) |
|--------------|-----------|-------------|-------------|------------|-----------|
|   Averages   |   4.7238  |    1.0850   |    4.3112   |   8.8375   |   0.1463  |

Full Results: https://github.com/JorgeFernandes-Git/zau_bot/blob/main/e5_DualRGB_arm2agv/results.md
_______________________________

## Calibration Results per collection:

| Collection | camera (px) | camera_mb (px) |
| :-------------: | :-------------: | :-------------: |
|    000     |    0.3132   |     0.2266     |
|    001     |    0.3118   |     0.2262     |
|    002     |    0.2356   |     0.2303     |
|    003     |    0.2311   |     0.2301     |
|    004     |    0.2610   |     0.2241     |
|    005     |    0.2288   |     0.2259     |
|    006     |    0.2075   |     0.2200     |
|    007     |    0.2467   |     0.2311     |
|    008     |    0.1912   |     0.2222     |
|    009     |    0.2115   |     0.2244     |
|    010     |    0.2030   |     0.2276     |
|    011     |    0.1812   |     0.2039     |
|    012     |    0.1896   |     0.2168     |
|    013     |    0.1831   |     0.2123     |
|    014     |    0.1833   |     0.2167     |
|    015     |    0.2079   |     0.2064     |
|    016     |    0.1986   |     0.2098     |
|    017     |    0.2649   |     0.2178     |
|    018     |    0.2317   |     0.2040     |
|    019     |    0.2317   |     0.1643     |
|    020     |    0.2402   |     0.2012     |
|    021     |    0.2352   |     0.2016     |
|    022     |    0.2064   |     0.1770     |
|    023     |    0.1843   |     0.1646     |
|    024     |    0.2399   |     0.3006     |
|    025     |    0.2189   |     0.2974     |
|    026     |    0.3010   |     0.2635     |
|    027     |    0.2960   |     0.2622     |
|    028     |    0.3605   |     0.2703     |
|    029     |    0.2933   |     0.2657     |
|    030     |    0.2687   |     0.2678     |
|    031     |    0.3957   |     0.3645     |
|    032     |    0.3946   |     0.3931     |
|    033     |    0.3943   |     0.3308     |
|    034     |    0.3482   |     0.3148     |
|    035     |    0.4776   |     0.3358     |
|    036     |    0.2559   |     0.1642     |
|    037     |    0.1662   |     0.1508     |
|    038     |    0.1914   |     0.1413     |
|    039     |    0.1452   |     0.1403     |
|    040     |    0.1332   |     0.1431     |
|    041     |    0.3624   |     0.2480     |
|    042     |    0.4330   |     0.4232     |
|    043     |    0.3678   |     0.3547     |
|    044     |    0.7185   |     0.8490     |
|    045     |    0.3323   |     0.3440     |
|    046     |    0.2996   |     0.2896     |
|    047     |    0.2626   |     0.2631     |
|    048     |    0.2829   |     0.3073     |
|    049     |    0.2857   |     0.2811     |
|    050     |    0.2223   |     0.2458     |
|    051     |    0.2236   |     0.2449     |
|    052     |    0.2369   |     0.2538     |
|    053     |    0.2428   |     0.2595     |
|    054     |    0.3159   |     0.2754     |
|    055     |    0.2909   |     0.2779     |
|    056     |    0.2953   |     0.2737     |
|    057     |    0.2793   |     0.2679     |
|    058     |    0.2799   |     0.2700     |
|    059     |    0.3104   |     0.2754     |
|    060     |    0.3344   |     0.2707     |
|    061     |    0.3434   |     0.2732     |
|    062     |    0.3501   |     0.2709     |
|    063     |    0.4753   |     0.4824     |
|    064     |    0.3712   |     0.4222     |
|    065     |    0.5210   |     0.4678     |
|    066     |    0.3982   |     0.3317     |
|    067     |    5.9500   |     5.3938     |
|    068     |    0.3263   |     0.2433     |
|    069     |    0.3651   |     0.3248     |
|    070     |    6.7066   |     6.3318     |
|    071     |    0.4881   |     0.3354     |
|    072     |    2.5656   |     2.3303     |
|    073     |    0.6033   |     0.7436     |
|    074     |    5.1378   |     6.0900     |
|    075     |    0.3518   |     0.2445     |
|    076     |    0.3384   |     0.2124     |
|    077     |    0.9191   |     0.7748     |
|    078     |    0.4135   |     0.2854     |
|    079     |    0.3527   |     0.3192     |
|  **Averages**  |    **0.5452**   |     **0.5205**     |


_______________________________

## Calibration tree and Transformations:

![e5_summary](https://user-images.githubusercontent.com/80167550/222408819-f7866d71-9897-4df3-9d31-5875d86dd720.png)

_______________________________

## Videos:
* Set initial estimate: https://youtu.be/EyRvSiWIfjA
* Run calibration: https://youtu.be/r8cS9na9IzU
* Evaluation procedure: https://youtu.be/DAciryNWxCg
_______________________________

## Configure the calibration using the transformations in the bagfile instead of the ones produced by the xacro description:

    rosrun atom_calibration configure_calibration_pkg -n e5_dualrgb_arm2agv_calibration -utf

## Commands:
Launch AGV for calibration:

    roslaunch zau_bot_bringup zau_bot_bringup

Launch teleop to control the AGV through the keyboard:

    roslaunch zau_bot_bringup my_teleop.launch 

Record bag file:

    roslaunch e4_dualrgb_record_bag record_sensor_data.launch

Collect dataset for calibration:

    roslaunch e5_dualrgb_arm2agv_calibration collect_data.launch output_folder:=$ATOM_DATASETS/e5_dualrgb_arm2agv_v3 overwrite:=true

Playback dataset for calibration (2 terminals):

    roslaunch e5_dualrgb_arm2agv_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e5_dualrgb_arm2agv_v2/dataset.json 

Run calibration (2 terminals):

    roslaunch e5_dualrgb_arm2agv_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e5_dualrgb_arm2agv_v3/dataset.json -v -rv -si -vo -nig 0.1 0.1 -oj atom_calibration_nig_0.1_0.1.json -csf "lambda name: int(name) not in [49, 49]"

Test with anchor pattern (-ap) (didn't work):

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e5_dualrgb_arm2agv/dataset.json -v -rv -si -vo -nig 0.1 0.1 -ap -oj atom_calibration_ap.json

Use output json (-oj) to save different calibration json file:

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e5_dualrgb_arm2agv/dataset.json -v -rv -si -vo -oj atom_calibration_no_nig.json

_______________________________

Run evaluations:

https://github.com/JorgeFernandes-Git/zau_bot/blob/main/e5_DualRGB_arm2agv/results.md

**rgb to rgb**

    rosrun atom_evaluation rgb_to_rgb_evaluation -train_json ~/datasets/e5_dualrgb_arm2agv_v3/dataset.json -test_json ~/datasets/e5_dualrgb_arm2agv/dataset.json -ss camera -st camera_mb -si

**ground truth frame**

    rosrun atom_evaluation ground_truth_frame_evaluation -train_json /home/jorge/datasets/e5_dualrgb_arm2agv_v3/atom_calibration_nig_0.1_0.1.json -test_json /home/jorge/datasets/e5_dualrgb_arm2agv_v3/dataset.json


_______________________________


FINAL VERSION RESULTS WITH 20 COLLECTIONS:

| Collection | camera (px) | camera_mb (px) |
|------------|-------------|----------------|
|    000     |    0.1831   |     0.1463     |
|    001     |    0.1317   |     0.1470     |
|    002     |    0.1032   |     0.1016     |
|    003     |    0.1056   |     0.1071     |
|    004     |    0.1161   |     0.1081     |
|    005     |    0.1431   |     0.1406     |
|    006     |    0.1396   |     0.1154     |
|    007     |    0.1236   |     0.1099     |
|    008     |    0.1213   |     0.1389     |
|    009     |    0.3493   |     0.3346     |
|    010     |    0.1471   |     0.1621     |
|    011     |    0.1120   |     0.1166     |
|    012     |    0.1288   |     0.1251     |
|    013     |    0.1029   |     0.1093     |
|    014     |    0.1082   |     0.0987     |
|    015     |    0.2129   |     0.1137     |
|    016     |    0.3414   |     0.2340     |
|    017     |    0.1794   |     0.1028     |
|    018     |    0.2036   |     0.0982     |
|    019     |    0.1022   |     0.1083     |
|    020     |    0.1086   |     0.1079     |
|  Averages  |    0.1554   |     0.1346     |
