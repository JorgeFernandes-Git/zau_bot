#!/usr/bin/env python3

import argparse
import os
import time
import rosbag
from pytictoc import TicToc
import geometry_msgs.msg
from tqdm import tqdm

"""
Usage:

./delete_tfs_in_bagfile -bfi original.bag -ttk base_link shoulder_link upper_arm_link forearm_link wrist_1_link wrist_2_link wrist_3_link ee_link cam_1_link cam_1_color_frame cam_1_color_optical_frame cam_1_depth_frame cam_1_depth_optical_frame

"""


if __name__ == "__main__":
    # Parse command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-bfi", "--bagfile_in", help='Full path to the bagfile', type=str, required=True)
    ap.add_argument("-bfo", "--bagfile_out", help='Full path to output the bagfile. If not given will be named processed.bag and placed on the same folder as the input bag.', type=str, required=False)
    ap.add_argument("-ttk", "--transformations_to_keep", help='Transformations to keep in the bag file', type=str, required=True,  nargs='+')
    args = vars(ap.parse_args())
    
    if args['bagfile_out'] is None:
        path = os.path.dirname(args['bagfile_in'])
        print(path)
        args['bagfile_out'] = path + '/cropped.bag'
        
    print('Creating a new bag ' + args['bagfile_out'])
    transformations_to_keep = args['transformations_to_keep']
    
    # --------------------------------------------------------------------------
    # Read the bag input file
    # --------------------------------------------------------------------------
    bag_file = args['bagfile_in']
    print('Loading bagfile ' + bag_file)
    bag = rosbag.Bag(bag_file) # load the bag file
    bag_info = bag.get_type_and_topic_info()
    bag_types = bag_info[0]
    bag_topics = bag_info[1]
    
    # --------------------------------------------------------------------------
    # Initial setup
    # --------------------------------------------------------------------------
    tictoc = TicToc()
    tictoc.tic()
    bag_out = rosbag.Bag(args['bagfile_out'], 'w')
    
    
    # --------------------------------------------------------------------------
    # Get initial stamp to compute mission time
    # --------------------------------------------------------------------------
    for topic, msg, stamp in bag.read_messages():
        initial_stamp = stamp
        break
    
    # --------------------------------------------------------------------------
    # Writing new bagfile
    # --------------------------------------------------------------------------
    print('Converting bagfile. Please wait...')
    for topic, msg, stamp, connection_header in tqdm(bag.read_messages(return_connection_header=True), total=bag.get_message_count(), desc='Processing bag messages'):
        mission_time = (stamp - initial_stamp)

        if mission_time.to_sec() > 10: # just for testing fast, analyze messages only until 10 secs mission time.
            break
        
        if topic == "/tf" and msg.transforms:
            transforms_to_keep = []
            for i in range(len(msg.transforms)):                
                if msg.transforms[i].header.frame_id in transformations_to_keep and msg.transforms[i].child_frame_id in transformations_to_keep:
                    transforms_to_keep.append(msg.transforms[i])
            
            # print(f'Transformations to keep: {transforms_to_keep}')        
            msg.transforms = transforms_to_keep                        
            bag_out.write(topic, msg, stamp, connection_header=connection_header)
            
        else:
            bag_out.write(topic, msg, stamp, connection_header=connection_header)
    
    bag.close() # close the bag file.
    bag_out.close() # close the bag file.
    
    print('Finished in ' + str(round(tictoc.tocvalue(),2)) + ' seconds.')
    
    