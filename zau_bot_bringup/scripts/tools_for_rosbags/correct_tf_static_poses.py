#!/usr/bin/env python3

# stdlib
import os
import argparse
from tqdm import tqdm

# 3rd-party
import rosbag
from pytictoc import TicToc

# local packages

if __name__ == "__main__":
    # Parse command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-bfi", "--bagfile_in", help='Full path to the bagfile', type=str, required=True)
    ap.add_argument("-bfo", "--bagfile_out", help='Full path to output the bagfile. If not given will be named processed.bag and placed on the same folder as the input bag.', type=str, required=False)
    args = vars(ap.parse_args())
    
    if args['bagfile_out'] is None:
        path = os.path.dirname(args['bagfile_in'])
        print(path)
        args['bagfile_out'] = path + '/corrected.bag'
        
    print('Creating a new bag ' + args['bagfile_out'])

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

        if topic == '/tf_static': # tackle tf messages especially
            for transform_idx, transform in enumerate(msg.transforms): # iterate all transforms
                if transform.header.frame_id == 'zau/base_link' and transform.child_frame_id =='cam_2_link': # the specific transform we want to change
         
                    # Set a new transform value for rotation
                    print('Changing transform in msg on topic /tf_static with parent ' + transform.header.frame_id + ' and child ' + transform.child_frame_id  + ' at time ' + str((stamp-initial_stamp).to_sec()))
                    print('Before\n: ' + str(transform.transform.rotation))
                    transform.transform.rotation.x = -0.0085252
                    transform.transform.rotation.y = 0.0146204
                    transform.transform.rotation.z = -0.7473817
                    transform.transform.rotation.w = 0.6641793
                    print('After:\n' + str(transform.transform.rotation))
                    
                if transform.header.frame_id == 'ee_link' and transform.child_frame_id =='cam_1_link': # the specific transform we want to change
                    
                    # Set a new transform value for rotation
                    print('Changing transform in msg on topic /tf_static with parent ' + transform.header.frame_id + ' and child ' + transform.child_frame_id  + ' at time ' + str((stamp-initial_stamp).to_sec()))
                    print('Before:\n' + str(transform.transform.rotation))
                    # -0.2758865, 0.6493113, -0.2783442, 0.6517715
                    transform.transform.rotation.x = -0.2758865
                    transform.transform.rotation.y = 0.6493113
                    transform.transform.rotation.z = -0.2783442
                    transform.transform.rotation.w = 0.6517715
                    print('After\n: ' + str(transform.transform.rotation))

        # write msg to bag_out
        bag_out.write(topic, msg, stamp, connection_header=connection_header)

    bag.close() # close the bag file.
    bag_out.close() # close the bag file.

    # Print final report
    print('Finished in ' + str(round(tictoc.tocvalue(),2)) + ' seconds.')


   