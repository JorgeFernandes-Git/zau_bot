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

Evaluate two datasets: ...

_______________________________

## Calibration Results per collection:
| Collection | camera (px) | camera_mb (px) |
| :-------------: | :-------------: | :-------------: |
|    000     |    0.3955   |     0.2987     |
|    001     |    0.3991   |     0.2894     |
|    003     |    0.4079   |     0.3008     |
|    004     |    0.3920   |     0.2976     |
|    005     |    0.2638   |     0.2757     |
|    006     |    0.4179   |     0.2806     |
|    007     |    0.3221   |     0.2835     |
|    008     |    0.3717   |     0.2967     |
|    009     |    0.2990   |     0.2851     |
|    010     |    0.3095   |     0.2870     |
|    011     |    0.2284   |     0.2435     |
|    012     |    0.2314   |     0.1697     |
|    013     |    0.2097   |     0.1639     |
|    014     |    0.2178   |     0.1705     |
|    015     |    0.2272   |     0.1665     |
|    016     |    0.2227   |     0.1662     |
|    017     |    0.2342   |     0.1639     |
|    018     |    0.2236   |     0.1727     |
|    019     |    0.1993   |     0.1686     |
|    020     |    0.2233   |     0.1817     |
|    021     |    0.2447   |     0.2116     |
|    022     |    0.2053   |     0.2074     |
|    023     |    0.2728   |     0.2347     |
|    024     |    0.2798   |     0.2310     |
|    025     |    0.3193   |     0.3291     |
|    026     |    0.3723   |     0.3609     |
|    027     |    0.5020   |     0.3281     |
|    028     |    0.5174   |     0.3476     |
|    029     |    0.6707   |     0.3627     |
|    030     |    0.6520   |     0.3656     |
|    031     |    0.4693   |     0.3670     |
|    032     |    0.5675   |     0.3551     |
|    033     |    0.6942   |     0.3394     |
|    034     |    0.4854   |     0.5246     |
|    035     |    0.4680   |     0.6168     |
|    036     |    0.6836   |     0.6939     |
|    037     |    0.2960   |     0.2028     |
|    038     |    0.2471   |     0.2042     |
|    039     |    0.2090   |     0.1841     |
|    040     |    0.3512   |     0.1844     |
|    041     |    0.3331   |     0.1892     |
|    042     |    0.3622   |     0.3134     |
|    043     |    0.4612   |     0.6036     |
|    044     |    0.4596   |     0.5186     |
|    046     |    4.7992   |     0.5313     |
|    047     |    0.8208   |     0.3782     |
|    048     |    0.6313   |     0.3511     |
|    049     |    0.6479   |     0.2702     |
|    050     |    1.2631   |     0.2872     |
|    051     |    0.4497   |     0.2574     |
|    052     |    0.4888   |     0.2567     |
|    053     |    0.4413   |     0.2600     |
|    054     |    0.4179   |     0.2839     |
|    055     |    0.3689   |     0.2959     |
|    056     |    0.3098   |     0.2995     |
|    057     |    0.2723   |     0.2975     |
|    058     |    0.2457   |     0.2913     |
|    059     |    0.2595   |     0.2963     |
|    060     |    0.3142   |     0.2978     |
|    061     |    0.3158   |     0.2903     |
|    062     |    0.3293   |     0.2907     |
|    063     |    0.3273   |     0.2915     |
|    064     |    0.3452   |     0.3016     |
|    065     |    0.3124   |     0.2700     |
|    066     |    0.3274   |     0.2821     |
|    067     |    0.3147   |     0.2859     |
|    068     |    1.9908   |     2.3169     |
|    069     |    0.2679   |     0.1680     |
|    070     |    0.2824   |     0.1576     |
|    071     |    3.9299   |     3.6354     |
|    072     |    1.0905   |     0.9328     |
|    074     |    0.5836   |     0.6683     |
|    075     |    0.5275   |     0.6671     |
|    076     |    0.7180   |     0.6815     |
|  **Averages**  |    **0.5313**   |     **0.3896**     |
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

    rosrun atom_calibration dataset_playback -json /home/jorge/datasets/e4_dualrgb/dataset.json 

Run calibration (2 terminals):

    roslaunch e4_dualrgb_calibration calibrate.launch

    rosrun atom_calibration calibrate -json $ATOM_DATASETS/e4_dualrgb/dataset.json -v -rv -si -vo

