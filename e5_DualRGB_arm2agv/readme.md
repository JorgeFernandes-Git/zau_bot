## Full calibration of Mobile Manipulator - 3 transformations with 2 sensors ()
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

_______________________________

Evaluate two datasets:

Summary:

**Eye-on-hand camera to AGV camera evaluation**:
| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm) | Rot (deg) |
| :-------------: | :---: | :---: | :---: | :---: | :---: |
|   **Averages**   |   **0.5237**  |    **0.3206**   |    **0.2796**   |   **1.5091**   |   **0.2103**  |

**AGV camera to Eye-on-hand camera evaluation**:
| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm) | Rot (deg) |
| :-------------: | :---: | :---: | :---: | :---: | :---: |
|   **Averages**   |   **0.4665**  |    **0.2470**   |    **0.2788**   |   **1.5091**   |   **0.2103**  |

Full Results: https://github.com/JorgeFernandes-Git/zau_bot/blob/main/e5_DualRGB_arm2agv/results.md

_______________________________

## Calibration Results per collection:

| Collection | camera (px) | camera_mb (px) |
| :-------------: | :-------------: | :-------------: |
|    000     |    0.2609   |     0.1793     |
|    001     |    0.2559   |     0.1735     |
|    002     |    0.2168   |     0.1834     |
|    003     |    0.2115   |     0.1818     |
|    004     |    0.2497   |     0.1742     |
|    005     |    0.1899   |     0.1779     |
|    006     |    0.2045   |     0.1734     |
|    007     |    0.2212   |     0.1829     |
|    008     |    0.1713   |     0.1752     |
|    009     |    0.1793   |     0.1768     |
|    010     |    0.1590   |     0.1647     |
|    011     |    0.1314   |     0.1302     |
|    012     |    0.1386   |     0.1437     |
|    013     |    0.1480   |     0.1482     |
|    014     |    0.1426   |     0.1406     |
|    015     |    0.1923   |     0.1429     |
|    016     |    0.1791   |     0.1405     |
|    017     |    0.2562   |     0.1477     |
|    018     |    0.2268   |     0.1388     |
|    019     |    0.2444   |     0.1596     |
|    020     |    0.2562   |     0.2024     |
|    021     |    0.2463   |     0.1980     |
|    022     |    0.2094   |     0.1684     |
|    023     |    0.1731   |     0.1619     |
|    024     |    0.2485   |     0.2829     |
|    025     |    0.2178   |     0.2718     |
|    026     |    0.2974   |     0.2482     |
|    027     |    0.2887   |     0.2413     |
|    028     |    0.3510   |     0.2449     |
|    029     |    0.2811   |     0.2381     |
|    030     |    0.2647   |     0.2521     |
|    031     |    0.3944   |     0.3220     |
|    032     |    0.3912   |     0.3695     |
|    033     |    0.3936   |     0.3119     |
|    034     |    0.3453   |     0.2798     |
|    035     |    0.4559   |     0.2733     |
|    036     |    0.2581   |     0.1671     |
|    037     |    0.1661   |     0.1514     |
|    038     |    0.2078   |     0.1404     |
|    039     |    0.1563   |     0.1391     |
|    040     |    0.1282   |     0.1435     |
|    041     |    0.3069   |     0.1377     |
|    042     |    0.3777   |     0.3247     |
|    043     |    0.2790   |     0.2503     |
|    044     |    0.7027   |     0.8364     |
|    045     |    0.3217   |     0.3285     |
|    046     |    0.2678   |     0.2708     |
|    047     |    0.2505   |     0.2450     |
|    048     |    0.2598   |     0.2877     |
|    049     |    0.2581   |     0.2618     |
|    050     |    0.2255   |     0.2319     |
|    051     |    0.2323   |     0.2273     |
|    052     |    0.2344   |     0.2345     |
|    053     |    0.2458   |     0.2460     |
|    054     |    0.3258   |     0.2609     |
|    055     |    0.2976   |     0.2638     |
|    056     |    0.2945   |     0.2609     |
|    057     |    0.2735   |     0.2566     |
|    058     |    0.2707   |     0.2588     |
|    059     |    0.3000   |     0.2640     |
|    060     |    0.3257   |     0.2559     |
|    061     |    0.3344   |     0.2593     |
|    062     |    0.3444   |     0.2590     |
|    063     |    0.4732   |     0.4825     |
|    064     |    0.3489   |     0.3896     |
|    065     |    0.5171   |     0.4699     |
|    066     |    0.3923   |     0.3308     |
|    **067**     |    5.9530   |     5.3773     |
|    068     |    0.3103   |     0.2142     |
|    069     |    0.3614   |     0.3264     |
|    **070**     |    6.7073   |     6.3786     |
|    071     |    0.4560   |     0.2751     |
|    **072**     |    2.5759   |     2.3521     |
|    073     |    0.5938   |     0.6921     |
|    **074**     |    5.1277   |     6.0659     |
|    075     |    0.3479   |     0.2400     |
|    076     |    0.3007   |     0.1439     |
|    077     |    0.9064   |     0.7634     |
|    078     |    0.3584   |     0.2675     |
|    079     |    0.3321   |     0.3033     |
|  **Averages**  |    **0.5313**   |     **0.4917**     |


_______________________________

## Calibration tree and Transformations:

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

    roslaunch e5_dualrgb_arm2agv_calibration collect_data.launch output_folder:=$ATOM_DATASETS/e5_dualrgb_arm2agv overwrite:=true

Playback dataset for calibration (2 terminals):

    roslaunch e5_dualrgb_arm2agv_calibration dataset_playback.launch

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e5_dualrgb_arm2agv_v2/dataset.json 

Run calibration (2 terminals):

    roslaunch e5_dualrgb_arm2agv_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e5_dualrgb_arm2agv/dataset.json -v -rv -si -vo

Run evaluation:

    rosrun atom_evaluation rgb_to_rgb_evaluation -train_json ~/datasets/e5_dualrgb_arm2agv/atom_calibration.json -test_json ~/datasets/e5_dualrgb_arm2agv/atom_calibration.json -ss camera -st camera_mb -si


