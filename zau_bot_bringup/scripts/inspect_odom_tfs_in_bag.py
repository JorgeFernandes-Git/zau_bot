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
    # Writing msgs of tf_static to topic /tf
    # --------------------------------------------------------------------------
    print('Writing msgs to topic /tf...')
    for topic, msg, stamp in bag.read_messages():
        mission_time = (stamp - initial_stamp)

        if mission_time.to_sec() > 30: # just for testing fast, analyze messages only until 10 secs mission time.
            break
        
        if topic == '/tf':

            for transform_idx, transform in enumerate(msg.transforms): # iterate all transforms
                # ros transform msg: http://docs.ros.org/en/noetic/api/tf/html/msg/tfMessage.html
                if transform.header.frame_id == 'zau/map_rn0' and transform.child_frame_id =='zau/odom': 
                    # Set a new transform value for rotation
                    print('Got transform in msg on topic /tf with parent ' + transform.header.frame_id + ' and child ' + transform.child_frame_id  + ' at time ' + str((stamp-initial_stamp).to_sec()))
                    print('transform.header.stamp = ' + str((transform.header.stamp-initial_stamp).to_sec()))

                    from sensor_msgs.msg import JointState
                    j = JointState()
                    j.header.stamp = transform.header.stamp
                    bag_out.write('odom_tf_msg', j, stamp)

                if transform.header.frame_id == 'zau/base_link' and transform.child_frame_id =='cam_2_link': 
                    # Set a new transform value for rotation
                    print('Got transform in msg on topic /tf with parent ' + transform.header.frame_id + ' and child ' + transform.child_frame_id  + ' at time ' + str((stamp-initial_stamp).to_sec()))
                    print('transform.header.stamp = ' + str((transform.header.stamp-initial_stamp).to_sec()))

                    from sensor_msgs.msg import JointState
                    j = JointState()
                    j.header.stamp = transform.header.stamp
                    bag_out.write('cam_2_tf_msg', j, stamp)


            # msg.transforms.extend(static_tfs) # extend static tfs to tf topic

        # Write msg to bag_out
        # bag_out.write(topic, msg, stamp)

    bag.close() # close the bag file.
    bag_out.close() # close the bag file.

    # Print final report
    print('Finished in ' + str(round(tictoc.tocvalue(),2)) + ' seconds.')