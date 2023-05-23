#!/usr/bin/env python3

import argparse
import time
import rosbag
from pytictoc import TicToc
import geometry_msgs.msg



if __name__ == "__main__":
    # Parse command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-bfi", "--bagfile_in", help='Full path to the bagfile', type=str, required=True)
    ap.add_argument("-bfo", "--bagfile_out", help='Full path to the bagfile', type=str, required=True)
    ap.add_argument("-ttk", "--transformations_to_keep", help='Transformations to keep in the bag file', type=str, required=True,  nargs='+')
    args = vars(ap.parse_args())
    
    bag_out = rosbag.Bag(args['bagfile_out'], 'w')
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
    
    # Get initial stamp to compute mission time
    # for topic, msg, stamp in bag.read_messages():
    #     initial_stamp = stamp
    #     break
    
    for topic, msg, stamp in bag.read_messages():
        # mission_time = (stamp - initial_stamp)

        # if mission_time.to_sec() > 10: # just for testing fast, analyze messages only until 10 secs mission time.
        #     break
        
        if topic == "/tf" and msg.transforms:
            transforms_to_keep = []
            for i in range(len(msg.transforms)):                
                if msg.transforms[i].header.frame_id in transformations_to_keep and msg.transforms[i].child_frame_id in transformations_to_keep:
                    transforms_to_keep.append(msg.transforms[i])
            
            # print(f'Transformations to keep: {transforms_to_keep}')        
            msg.transforms = transforms_to_keep                        
            bag_out.write(topic, msg, stamp)
            
        else:
            bag_out.write(topic, msg, stamp)
    
    bag.close() # close the bag file.
    bag_out.close() # close the bag file.
    
    print('Finished in ' + str(round(tictoc.tocvalue(),2)) + ' seconds.')
    
    