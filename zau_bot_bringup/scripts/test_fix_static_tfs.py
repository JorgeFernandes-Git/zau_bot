#!/usr/bin/env python3

# stdlib
import os
import sys
import argparse
import subprocess
from os.path import exists
from copy import deepcopy
from datetime import date, datetime

import matplotlib
import atom_core.config_io
import atom_core.drawing

# 3rd-party
import yaml
import numpy
import rospy
import rospkg
import rosbag
import jinja2
import matplotlib.pyplot as plt
import networkx as nx
from pytictoc import TicToc

# local packages
from atom_core.utilities import checkDirectoryExistence
from atom_core.naming import generateLabeledTopic
from colorama import Style, Fore
from graphviz import Digraph
from urdf_parser_py.urdf import URDF
from matplotlib import cm
from jinja2 import Environment, FileSystemLoader

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
    # print('\n' + str(bag_topics))

    # get initial stamp to compute mission time
    for topic, msg, stamp in bag.read_messages():
        initial_stamp = stamp
        break

    static_tfs = []
    for topic, msg, stamp in bag.read_messages():
        mission_time = (stamp - initial_stamp)

        if mission_time.to_sec() > 10: # just for testing fast, analyze messages only until 10 secs mission time.
            break
        
        if topic == '/tf_static':
            for transform_idx, transform in enumerate(msg.transforms): # iterate all transforms
                
                if transform.header.frame_id == 'zau/base_link' and transform.child_frame_id =='cam_2_link': # the specific transform we want to change
                    # Set a new transform value for rotation
                    print('Changing transform in msg on topic /tf with parent ' + transform.header.frame_id + ' and child ' + transform.child_frame_id  + ' at time ' + str((stamp-initial_stamp).to_sec()))
                    print('Before: ' + str(transform.transform.rotation))
                    transform.transform.rotation.z = 33.7 # TODO set the correct values
                    print('After: ' + str(transform.transform.rotation))
                
                static_tfs.append(transform)
                # print(f'transform_idx {transform_idx} is \n{msg}')
                # tf_static_msg = transform
        
        if topic == '/tf':
            for transform_idx, transform in enumerate(msg.transforms): # iterate all transforms
                msg.transforms.extend(static_tfs) # extend static tfs to tf topic

        # write msg to bag_out
        bag_out.write(topic, msg, stamp)

    bag.close() # close the bag file.
    bag_out.close() # close the bag file.

    # Print final report
    print('Finished in ' + str(round(tictoc.tocvalue(),2)) + ' seconds.')