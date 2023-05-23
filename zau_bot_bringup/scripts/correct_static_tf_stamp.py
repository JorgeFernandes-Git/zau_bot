#!/usr/bin/env python3

import argparse
import time
import rosbag
from pytictoc import TicToc
import geometry_msgs.msg
from tf2_msgs.msg import TFMessage
from tqdm import tqdm


if __name__ == "__main__":
    # Parse command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-bfi", "--bagfile_in", help='Full path to the bagfile', type=str, required=True)
    ap.add_argument("-bfo", "--bagfile_out", help='Full path to the bagfile', type=str, required=True)
    args = vars(ap.parse_args())
    
    bag_out = rosbag.Bag(args['bagfile_out'], 'w')
    
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
    
    # Save initial stamp
    for topic, msg, stamp in bag.read_messages():
        initial_stamp = stamp
        break

    # Join all tf_static in one message and give the initial stamp
    static_tfs_to_join = []
    first_tf = True
    for topic, msg, stamp in bag.read_messages():
        if topic == '/tf_static' and msg.transforms:
            for i in range(len(msg.transforms)):
                msg.transforms[i].header.stamp = initial_stamp
                
            static_tfs_to_join.extend(msg.transforms)
    
    # Save all messages, putting the tf_static and first tf on the initial stamp
    first_time_static = True
    first_time_tf = True
    for topic, msg, stamp in tqdm(bag.read_messages(), total=bag.get_message_count(), desc='Processing bag file'):        
        if topic == '/tf_static':
            if first_time_static:
                tf_static_msg = TFMessage() # publish this transform on topic /tf_static
                tf_static_msg.transforms.extend(static_tfs_to_join)
                bag_out.write(topic, tf_static_msg, initial_stamp)
                first_time_static = False
        
        elif topic == '/tf':
            if first_time_tf == True:
                for i in range(len(msg.transforms)):                
                    msg.transforms[i].header.stamp = initial_stamp
                bag_out.write(topic, msg, initial_stamp)
                first_time_tf = False
            else:
                bag_out.write(topic, msg, stamp)
                
        elif topic != '/tf' and topic != 'tf_static':
            bag_out.write(topic, msg, stamp)   
            
    bag.close() # close the bag file.
    bag_out.close() # close the bag file.
    
    print('Finished in ' + str(round(tictoc.tocvalue(),2)) + ' seconds.')
    
    