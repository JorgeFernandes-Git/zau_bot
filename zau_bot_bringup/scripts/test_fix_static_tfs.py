#!/usr/bin/env python3

# stdlib
import argparse

# 3rd-party
import rosbag
from pytictoc import TicToc

# local packages

if __name__ == "__main__":
    # Parse command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-bfi", "--bagfile_in", help='Full path to the bagfile', type=str, required=True)
    ap.add_argument("-bfo", "--bagfile_out", help='Full path to the bagfile', type=str, required=True)
    args = vars(ap.parse_args())

    # --------------------------------------------------------------------------
    # Initial setup
    # --------------------------------------------------------------------------
    tictoc = TicToc()
    tictoc.tic()
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

    # Get initial stamp to compute mission time
    for topic, msg, stamp in bag.read_messages():
        initial_stamp = stamp
        break

    # --------------------------------------------------------------------------
    # Read msgs in topic tf_static
    # --------------------------------------------------------------------------
    print(f'Reading topic /tf_static msgs...')
    static_tfs = []
    for topic, msg, stamp in bag.read_messages():
        mission_time = (stamp - initial_stamp)

        if mission_time.to_sec() > 10: # just for testing fast, analyze messages only until 10 secs mission time.
            break
        
        if topic == '/tf_static':
            for transform_idx, transform in enumerate(msg.transforms): # iterate all transforms
                static_tfs.append(transform)
    
    # --------------------------------------------------------------------------
    # Writing msgs of tf_static to topic /tf
    # --------------------------------------------------------------------------
    print(f'Writing msgs to topic /tf...')
    for topic, msg, stamp in bag.read_messages():
        mission_time = (stamp - initial_stamp)

        if mission_time.to_sec() > 10: # just for testing fast, analyze messages only until 10 secs mission time.
            break
        
        if topic == '/tf':
            msg.transforms.extend(static_tfs) # extend static tfs to tf topic

        # Write msg to bag_out
        bag_out.write(topic, msg, stamp)

    bag.close() # close the bag file.
    bag_out.close() # close the bag file.

    # Print final report
    print('Finished in ' + str(round(tictoc.tocvalue(),2)) + ' seconds.')