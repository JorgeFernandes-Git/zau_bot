## Simultaneous calibration of a Mobile Manipulator with two cameras. (Successful) https://github.com/JorgeFernandes-Git/zau_bot/issues/8
_______________________________

Summary: 
* Using ATOM framework to perform simultaneous calibration of a mobile manipulator with two cameras, one on the AGV and other on the end-effector of the manipulator.
* Aims to determine the transformations RGB1 w.r.t. AGV and RGB2 w.r.t. end-effector.
* The cameras used was a depth astra. 
* The calibration used a total of 76 collections.
* The output is a URDF file with the optimized poses of the sensors.
_______________________________

Launch optimized URDF:

    roslaunch e4_dualrgb_optimized e4_dualrgb_optimized.launch

_______________________________

Evaluate two datasets: 

Summary:

**Eye-on-hand camera to AGV camera evaluation**:
| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm) | Rot (deg) |
| :-------------: | :---: | :---: | :---: | :---: | :---: |
|   Averages   |   0.9692  |    0.5517   |    0.6383   |   2.3284   |   0.2953  |

**Output with noise initial guess `nig` 0.1 0.1:**
|          Transformation #          | X (mm) |  Y (mm) | Z (mm) | Roll (deg) | Pitch (deg) | Yaw (deg) | Trans (mm) | Rot (deg) |
|---------------------------|---------------|---------------|---------------|------------------------|--------------------------|----------------------|-----------------|---------------|
|    camera_link-camera_rgb_frame    | 0.4202 | 22.0208 | 1.6476 |   0.1250   |    0.1200   |   0.1051  |  22.0864   |   0.2027  |
| camera_mb_link-camera_mb_rgb_frame | 0.1011 | 21.9076 | 0.0778 |   0.0310   |    0.0072   |   0.0915  |  21.9079   |   0.0969  |

**Cross collection rgb to rgb evaluations Eye-on-hand camera to Eye-on-hand camera (same sensor)**
| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm)	| Rot (deg) |
|--------------|-----------|-------------|-------------|------------|-----------|
|   Averages   |   1.2644  |    0.8206   |    0.6549   |   2.6085   |   0.2816  |

**Cross collection rgb to rgb evaluations AGV camera to AGV camera (same sensor)**
| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm)	| Rot (deg) |
|--------------|-----------|-------------|-------------|------------|-----------|
|   Averages   |   0.5603  |    0.4316   |    0.2013   |   1.1862   |   0.0876  |

**Cross collection rgb to rgb evaluations Eye-on-hand camera to AGV camera (different sensor)**

| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm)	| Rot (deg) |
|--------------|-----------|-------------|-------------|------------|-----------|
|   Averages   |   1.0331  |    0.5739   |    0.6544   |   2.5920   |   0.3016  |

Full Results: https://github.com/JorgeFernandes-Git/zau_bot/blob/main/e4_DualRGB/results.md

_______________________________

## Calibration Results per collection:
| Collection | camera (px) | camera_mb (px) |
| :-------------: | :-------------: | :-------------: |
|    000     |    0.4374   |     0.4328     |
|    001     |    0.4604   |     0.4336     |
|    002     |    0.4010   |     0.4833     |
|    003     |    0.6187   |     0.4513     |
|    004     |    1.3643   |     1.2832     |
|    005     |    0.6921   |     0.5444     |
|    006     |    0.7555   |     0.5322     |
|    007     |    0.6986   |     0.4913     |
|    008     |    1.7238   |     1.3597     |
|    009     |    0.4279   |     0.4421     |
|    010     |    0.4594   |     0.4571     |
|    011     |    0.4992   |     0.4630     |
|    012     |    0.4583   |     0.4355     |
|    013     |    0.4500   |     0.4492     |
|    014     |    0.5096   |     0.3843     |
|    015     |    0.4071   |     0.4504     |
|    016     |    0.5216   |     0.4505     |
|    017     |    1.0394   |     0.6981     |
|    018     |    0.7396   |     0.6325     |
|    019     |    0.6120   |     0.5990     |
|    020     |    0.6473   |     0.6332     |
|    021     |    0.9370   |     0.9245     |
|    022     |    0.5829   |     0.4756     |
|    023     |    0.6720   |     0.4403     |
|    024     |    0.7699   |     0.4909     |
|    025     |    0.6362   |     0.4872     |
|    026     |    0.6242   |     0.4919     |
|    027     |    0.6119   |     0.4643     |
|    028     |    0.7064   |     0.8290     |
|    029     |    1.1263   |     0.6725     |
|    030     |    3.5016   |     1.7318     |
|    031     |    6.1099   |     5.3651     |
|    032     |    0.6474   |     0.5885     |
|    033     |    0.5856   |     0.4609     |
|    034     |    6.4056   |     4.7812     |
|    035     |    7.0314   |     3.6756     |
|    036     |    0.5728   |     0.4571     |
|    037     |    0.4865   |     0.5008     |
|  Averages  |    1.2087   |     0.9196     |

_______________________________

## Calibration tree and Transformations:
![e4_calib](https://user-images.githubusercontent.com/80167550/219897972-468485d9-b73f-4abd-8dcf-f0cb7b35de04.png)
![e4_summary tree](https://user-images.githubusercontent.com/80167550/219896533-d4d178b8-6b6d-44b8-9ef5-1f4988aefd84.png)
![e4_DualRGB_1](https://user-images.githubusercontent.com/80167550/219896216-7cf44fb8-8eed-4c58-b72d-6db8ec8b8193.png)
![e4_DualRGB_2](https://user-images.githubusercontent.com/80167550/219896251-a3c3e85e-fef8-4c25-9127-7306621c0adf.png)
_______________________________

## Videos:
* Recording bag file: https://youtu.be/uqdgiYQlHes
* Set initial estimate: https://youtu.be/4XuS6R1rgMA
* Collect data: https://youtu.be/7nSu06WNkNg
* Run calibration: https://youtu.be/AqQp4M0psj4
* Evaluation procedure:
_______________________________

## Configure the calibration using the transformations in the bagfile instead of the ones produced by the xacro description:

    rosrun atom_calibration configure_calibration_pkg -n e4_dualrgb_calibration -utf

## Commands:
Launch AGV for calibration:

    roslaunch zau_bot_bringup zau_bot_bringup

Launch teleop to control the AGV through the keyboard:

    roslaunch zau_bot_bringup my_teleop.launch 

Record bag file:

    roslaunch e4_dualrgb_record_bag record_sensor_data.launch

Playback dataset for calibration (2 terminals):

    roslaunch e4_dualrgb_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e4_dualrgb_v3/dataset.json

Run calibration (2 terminals):

    roslaunch e4_dualrgb_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e4_dualrgb_v2/dataset.json -v -rv -si -vo -nig 0.1 0.1 -oj atom_calibration_nig_0.1_0.1.json

