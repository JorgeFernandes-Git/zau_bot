## Ground truth frame evaluations using different datasets

    rosrun atom_evaluation ground_truth_frame_evaluation -train_json  /home/jorge/datasets/e6_mm/atom_calibration_nig_0.1_0.1.json -test_json /home/jorge/datasets/e6_mm/dataset_corrected.json

|          frame #          | Xcal-Xgt (mm) | Ycal-Ygt (mm) | Zcal-Zgt (mm) | Roll_cal-Roll_gt (deg) | Pitch_cal-Pitch_gt (deg) | Yaw_cal-Yaw_gt (deg) | Average - Trans | Average - Rot |
|---------------------------|---------------|---------------|---------------|------------------------|--------------------------|----------------------|-----------------|---------------|
| base_link_mb_to_base_link |     9.2194    |     9.1957    |    17.4085    |         0.0491         |          0.0806          |        0.0806        |     21.7397     |     0.1924    |
|           camera          |     7.0570    |    20.7202    |     0.9205    |         0.0659         |          0.0101          |        0.0101        |     16.6333     |     0.3626    |
|         camera_mb         |     0.6239    |    22.4860    |    23.8324    |         0.0559         |          0.2354          |        0.2354        |     32.7719     |     0.4130    |
|          velodyne         |     1.7709    |     4.6873    |    26.4831    |         0.2674         |          0.0021          |        0.0021        |     26.9529     |     0.2849    |
