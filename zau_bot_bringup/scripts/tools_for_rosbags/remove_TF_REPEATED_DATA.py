#!/usr/bin/env python3

import argparse
import rosbag
from tqdm import tqdm
from pytictoc import TicToc


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-bfi", "--bagfile_in", help='Full path to the bagfile', type=str, required=True)
    ap.add_argument("-bfo", "--bagfile_out", help='Full path to the bagfile', type=str, required=True)
    args = vars(ap.parse_args())
    
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
    
    last_tf_messages = {}
    for topic, msg, t in tqdm(bag.read_messages(), total=bag.get_message_count(), desc='Processing bag file'):
        if topic == "/tf" or topic == "/tf_static":
            filtered_transforms = []
            for transform in msg.transforms:
                if (
                    transform.header.frame_id == "zau/odom" and
                    transform.child_frame_id == "zau/map_rn0" and
                    (
                        transform.header.stamp.secs, transform.header.stamp.nsecs,
                        transform.child_frame_id
                    ) not in last_tf_messages
                ):
                    last_tf_messages[(
                        transform.header.stamp.secs, transform.header.stamp.nsecs,
                        transform.child_frame_id
                    )] = True
                    filtered_transforms.append(transform)
            msg.transforms = filtered_transforms
            bag_out.write(topic, msg, t)
        else:
            bag_out.write(topic, msg, t)
    
    bag.close() # close the bag file.
    bag_out.close() # close the bag file.

    print('Finished in ' + str(round(tictoc.tocvalue(),2)) + ' seconds.')
