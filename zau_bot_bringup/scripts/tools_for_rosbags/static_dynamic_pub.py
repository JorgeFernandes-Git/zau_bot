#!/usr/bin/env python

import rospy
import tf2_ros
import geometry_msgs.msg
import math

if __name__ == '__main__':
    
    rospy.init_node('tf2_broadcaster')
    
    br_in_tf = tf2_ros.TransformBroadcaster()
    br_in_static_tf = tf2_ros.StaticTransformBroadcaster()
    
    d = geometry_msgs.msg.TransformStamped()
    d2 = geometry_msgs.msg.TransformStamped()
    s = geometry_msgs.msg.TransformStamped()

    d.header.frame_id = "parent"
    d.child_frame_id = "dynamic_child"
    
    d2.header.frame_id = "parent"
    d2.child_frame_id = "dynamic_child_2"
    
    s.header.frame_id = "zau/base_link"
    s.child_frame_id = "base_link"

    s.header.stamp = rospy.Time.now()
    s.transform.translation.x = 0.0
    s.transform.translation.y = 2.0
    s.transform.translation.z = 0.0
    s.transform.rotation.x = 0.0
    s.transform.rotation.y = 0.0
    s.transform.rotation.z = 0.0
    s.transform.rotation.w = 1.0
    br_in_static_tf.sendTransform(s)
    
    # rate = rospy.Rate(10.0)
    
    # while not rospy.is_shutdown():
    #     d.header.stamp = rospy.Time.now()
    #     d.transform.translation.x = 2.0
    #     d.transform.translation.y = 0.0
    #     d.transform.translation.z = 0.0
    #     d.transform.rotation.x = 0.0
    #     d.transform.rotation.y = 0.0
    #     d.transform.rotation.z = 0.0
    #     d.transform.rotation.w = 1.0
    #     br_in_tf.sendTransform(d)
        
    #     d2.header.stamp = rospy.Time.now()
    #     d2.transform.translation.x = 2.0
    #     d2.transform.translation.y = 2.0
    #     d2.transform.translation.z = 0.0
    #     d2.transform.rotation.x = 0.0
    #     d2.transform.rotation.y = 0.0
    #     d2.transform.rotation.z = 0.0
    #     d2.transform.rotation.w = 1.0
    #     br_in_tf.sendTransform(d2)
        
    #     rate.sleep()
    #     print('Publish...')

    
    
    