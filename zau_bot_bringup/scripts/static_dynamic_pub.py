#!/usr/bin/env python

import rospy
import tf2_ros
import geometry_msgs.msg
import math

if __name__ == '__main__':
    
    rospy.init_node('tf2_broadcaster')
    br = tf2_ros.TransformBroadcaster()
    d = geometry_msgs.msg.TransformStamped()
    s = geometry_msgs.msg.TransformStamped()

    d.header.frame_id = "parent"
    d.child_frame_id = "dynamic_child"
    
    s.header.frame_id = "parent"
    s.child_frame_id = "static_child"

    rate = rospy.Rate(10.0)
    
    while not rospy.is_shutdown():
        x = rospy.Time.now().to_sec() * math.pi

        d.header.stamp = rospy.Time.now()
        d.transform.translation.x = 10 * math.sin(x)
        d.transform.translation.y = 10 * math.cos(x)
        d.transform.translation.z = 0.0
        d.transform.rotation.x = 0.0
        d.transform.rotation.y = 0.0
        d.transform.rotation.z = 0.0
        d.transform.rotation.w = 1.0
         
        s.header.stamp = rospy.Time.now()
        s.transform.translation.x = 0.0
        s.transform.translation.y = 2.0
        s.transform.translation.z = 0.0
        s.transform.rotation.x = 0.0
        s.transform.rotation.y = 0.0
        s.transform.rotation.z = 0.0
        s.transform.rotation.w = 1.0

        br.sendTransform(d)
        br.sendTransform(s)
        
        rate.sleep()
        print('Publish...')

    
    
    