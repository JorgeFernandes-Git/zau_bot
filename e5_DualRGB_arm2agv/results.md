## Datasets:

Dataset_test (79 collections): https://drive.google.com/file/d/1wFW4SjAVjr3k-UN35T8Aa26naBnl1z0V/view?usp=share_link

Dataset_train (68 collections): https://drive.google.com/file/d/1L0ArLBiDdpDo8fE0uD48FVTik2TehdPy/view?usp=share_link

Atom_calibration_nig_0.1_0.1_v1: https://drive.google.com/file/d/1T8t0V8a5qLIYSbgZ6UvCwK61C4pCgubH/view?usp=share_link

Atom_calibration_nig_0.1_0.1_v2: https://drive.google.com/file/d/19ABeM4Q5zKBi3TsVYLVyIN8_-WXw-ix6/view?usp=share_link

_________________________________________

## Eye-on-hand camera to AGV camera evaluation using different datasets

Atom_calibration_nig_0.1_0.1_v2 and Dataset_train.

    rosrun atom_evaluation rgb_to_rgb_evaluation -train_json /home/jorge/datasets/e5_dualrgb_arm2agv_v3/atom_calibration_nig_0.1_0.1.json -test_json /home/jorge/datasets/e5_dualrgb_arm2agv_v3/dataset.json -ss camera -st camera_mb


| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm) | Rot (deg) |
|--------------|-----------|-------------|-------------|------------|-----------|
|     000      |   7.5607  |    0.2260   |    7.5382   |  13.5021   |   0.0888  |
|     001      |   8.7196  |    0.1379   |    8.7060   |  13.6024   |   0.0634  |
|     002      |   8.6190  |    0.1108   |    8.6154   |  13.4676   |   0.2481  |
|     003      |   8.7491  |    0.1614   |    8.7456   |  13.5863   |   0.2652  |
|     004      |   9.0500  |    0.1913   |    9.0441   |  13.7847   |   0.2048  |
|     005      |   7.0356  |    0.3257   |    7.0246   |  14.0791   |   0.2077  |
|     006      |   7.1774  |    0.3908   |    7.1634   |  14.0897   |   0.2447  |
|     007      |   7.0398  |    0.3414   |    7.0289   |  13.8228   |   0.1780  |
|     008      |   7.0743  |    0.2656   |    7.0581   |  13.7051   |   0.1798  |
|     009      |   7.6022  |    0.1987   |    7.5975   |  13.5872   |   0.1326  |
|     010      |   7.9541  |    0.2237   |    7.9388   |  13.7515   |   0.1943  |
|     011      |   8.0501  |    0.1484   |    8.0424   |  13.8036   |   0.1784  |
|     012      |   8.1143  |    0.1762   |    8.1053   |  13.8548   |   0.2041  |
|     013      |   8.0388  |    0.1579   |    8.0301   |  13.8326   |   0.2175  |
|     014      |   8.1838  |    0.1810   |    8.1755   |  13.8727   |   0.1585  |
|     015      |   8.3302  |    0.4146   |    8.3099   |  13.7610   |   0.1197  |
|     016      |   9.5499  |    0.4607   |    9.5309   |  14.1729   |   0.1267  |
|     017      |   9.8585  |    0.5817   |    9.8263   |  14.1158   |   0.1724  |
|     018      |   9.9628  |    0.6768   |    9.9236   |  14.1633   |   0.0714  |
|     019      |   9.6305  |    0.5685   |    9.6040   |  13.9520   |   0.1681  |
|     020      |   9.6509  |    0.6178   |    9.6203   |  13.9440   |   0.1186  |
|     021      |   9.6849  |    0.5941   |    9.6567   |  13.9695   |   0.0888  |
|     022      |   7.1640  |    0.5510   |    7.1346   |  14.0365   |   0.0909  |
|     023      |   7.2837  |    0.5789   |    7.2535   |  14.0983   |   0.1747  |
|     024      |   7.3296  |    0.2106   |    7.3179   |  13.6741   |   0.0555  |
|     025      |   7.5454  |    0.2790   |    7.5325   |  13.9298   |   0.1022  |
|     026      |   7.4142  |    0.2394   |    7.3915   |  14.0651   |   0.1149  |
|     027      |   6.4143  |    0.2286   |    6.4032   |  14.0100   |   0.0814  |
|     028      |   6.2719  |    0.4184   |    6.2286   |  13.5429   |   0.1697  |
|     029      |   6.1518  |    0.3263   |    6.1335   |  13.8648   |   0.1458  |
|     030      |   6.2021  |    0.3992   |    6.1805   |  13.7995   |   0.2201  |
|     031      |   5.7188  |    0.1674   |    5.7122   |  13.8933   |   0.2575  |
|     032      |   5.7047  |    0.2570   |    5.6928   |  13.8046   |   0.2943  |
|     033      |   5.8060  |    0.3045   |    5.7917   |  14.1661   |   0.2575  |
|     034      |   5.8373  |    0.2829   |    5.8256   |  14.2863   |   0.2298  |
|     035      |   5.6782  |    0.3383   |    5.6631   |  13.6887   |   0.1258  |
|     036      |   6.9604  |    0.5473   |    6.9353   |  13.9217   |   0.0441  |
|     037      |   6.9814  |    0.6118   |    6.9496   |  13.9905   |   0.0246  |
|     038      |   6.9168  |    0.5289   |    6.8951   |  14.2119   |   0.0535  |
|     039      |   6.9466  |    0.5516   |    6.9225   |  14.1997   |   0.0410  |
|     040      |   6.9670  |    0.4209   |    6.9515   |  14.2691   |   0.0667  |
|     041      |   7.0137  |    0.5219   |    6.9899   |  14.2023   |   0.0140  |
|     042      |   8.9515  |    1.0384   |    8.8871   |  14.2088   |   0.0541  |
|     043      |   8.8936  |    0.6106   |    8.8583   |  14.1493   |   0.0618  |
|     044      |   8.6519  |    0.3047   |    8.6404   |  14.0198   |   0.2091  |
|     045      |   8.4709  |    0.1885   |    8.4645   |  13.6442   |   0.1419  |
|     046      |   8.5216  |    0.1992   |    8.5149   |  13.5660   |   0.2154  |
|     047      |   8.5771  |    0.1996   |    8.5698   |  13.6449   |   0.1833  |
|     048      |   8.7573  |    0.4439   |    8.7406   |  13.9174   |   0.0572  |
|     049      |   8.0156  |    3.2265   |    7.3280   |  15.3848   |   0.3058  |
|     050      |   7.4074  |    0.3021   |    7.3947   |  13.8985   |   0.0967  |
|     051      |   8.3236  |    0.4510   |    8.3056   |  13.8233   |   0.1540  |
|     052      |   8.0272  |    0.2976   |    8.0136   |  13.7657   |   0.0338  |
|     053      |   6.4962  |    0.2229   |    6.4699   |  13.6873   |   0.0437  |
|     054      |   6.5075  |    0.2509   |    6.4705   |  13.9047   |   0.0470  |
|     055      |   7.6503  |    0.4161   |    7.5990   |  14.0112   |   0.0053  |
|     056      |   7.6630  |    0.3240   |    7.6235   |  14.2059   |   0.0560  |
|     057      |   7.5307  |    0.3214   |    7.4870   |  14.0237   |   0.0588  |
|     058      |   7.7447  |    0.3696   |    7.6964   |  14.0813   |   0.0162  |
|     059      |   7.6064  |    0.2636   |    7.5580   |  13.8565   |   0.0682  |
|     060      |   5.5983  |    0.1088   |    5.5899   |  13.6650   |   0.0513  |
|     061      |   5.5413  |    0.1190   |    5.5376   |  13.5798   |   0.1011  |
|     062      |   5.3524  |    0.1454   |    5.3320   |  13.3784   |   0.1186  |
|     063      |   5.5101  |    0.1614   |    5.5032   |  13.3203   |   0.0343  |
|     064      |   5.6142  |    0.1760   |    5.6007   |  13.4819   |   0.0594  |
|     065      |   5.7317  |    0.1865   |    5.7204   |  13.9243   |   0.1641  |
|     066      |   5.8010  |    0.2168   |    5.7893   |  13.9573   |   0.0904  |
|     067      |   5.8738  |    0.1721   |    5.8682   |  14.3434   |   0.1683  |
|     068      |   5.7506  |    0.1528   |    5.7459   |  14.0790   |   0.1334  |
|   Averages   |   7.4277  |    0.3737   |    7.3985   |  13.9072   |   0.1293  |

_________________________________________

## Ground truth frame evaluations using different datasets

train_json: Atom_calibration_nig_0.1_0.1_v2
test_json: Dataset_v2

    rosrun atom_evaluation ground_truth_frame_evaluation -train_json ~/datasets/e5_dualrgb_arm2agv_v3/atom_calibration_nig_0.1_0.1.json -test_json ~/datasets/e5_dualrgb_arm2agv_v3/dataset.json 

|          Transformation #          | X (mm) |  Y (mm) | Z (mm) | Roll (deg) | Pitch (deg) | Yaw (deg) | Trans (mm) | Rot (deg) |
|---------------------------|---------------|---------------|---------------|------------------------|--------------------------|----------------------|-----------------|---------------|
|       base_link_mb-base_link       | 0.2551 |  1.0701 | 7.5430 |   0.0151   |    0.0013   |   0.0028  |   7.6228   |   0.0154  |
|    camera_link-camera_rgb_frame    | 1.5183 | 24.2693 | 6.4312 |   0.0168   |    0.0303   |   0.0482  |  25.1935   |   0.0595  |
| camera_mb_link-camera_mb_rgb_frame | 0.4289 | 24.2033 | 7.9438 |   0.0048   |    0.0500   |   0.0564  |  25.4772   |   0.0755  |

_________________________________________

# Cross Collections

## Cross collection rgb to rgb evaluations **Eye-on-hand camera to Eye-on-hand camera (same sensor)**

Atom_calibration_nig_0.1_0.1_v2 and Dataset_test

    rosrun atom_evaluation cross_collection_rgb_to_rgb_evaluation -train_json /home/jorge/datasets/e5_dualrgb_arm2agv_v3/atom_calibration_nig_0.1_0.1.json -test_json /home/jorge/datasets/e5_dualrgb_arm2agv/dataset.json -ss camera -st camera -wf odom

| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm)	| Rot (deg) |
|--------------|-----------|-------------|-------------|------------|-----------|
|   Averages   |   0.9757  |    0.3604   |    0.7644   |   2.8479   |   0.1728  |

_________________________________________

## Cross collection rgb to rgb evaluations **AGV camera to AGV camera (same sensor)**

Atom_calibration_nig_0.1_0.1_v2 and Dataset_test

    rosrun atom_evaluation cross_collection_rgb_to_rgb_evaluation -train_json /home/jorge/datasets/e5_dualrgb_arm2agv_v3/atom_calibration_nig_0.1_0.1.json -test_json /home/jorge/datasets/e5_dualrgb_arm2agv/dataset.json -ss camera_mb -st camera_mb -wf odom

| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm)	| Rot (deg) |
|--------------|-----------|-------------|-------------|------------|-----------|
|   Averages   |   0.8567  |    0.7164   |    0.2279   |   2.0671   |   0.1048  |

_________________________________________

## Cross collection rgb to rgb evaluations **Eye-on-hand camera to AGV camera (different sensor)**

Atom_calibration_nig_0.1_0.1_v2 and Dataset_test

    rosrun atom_evaluation cross_collection_rgb_to_rgb_evaluation -train_json /home/jorge/datasets/e5_dualrgb_arm2agv_v3/atom_calibration_nig_0.1_0.1.json -test_json /home/jorge/datasets/e5_dualrgb_arm2agv/dataset.json -ss camera -st camera_mb -wf odom

| Collection # | RMS (pix) | X err (pix) | Y err (pix) | Trans (mm)	| Rot (deg) |
|--------------|-----------|-------------|-------------|------------|-----------|
|   Averages   |   4.7238  |    1.0850   |    4.3112   |   8.8375   |   0.1463  |

_________________________________________