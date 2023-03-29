#!/usr/bin/env python3

import graphviz
import matplotlib

red = matplotlib.colors.rgb2hex([1, 0, 0])
black = matplotlib.colors.rgb2hex([0, 0, 0])
green = matplotlib.colors.rgb2hex([0, 0.5, 0])
blue = matplotlib.colors.rgb2hex([0, 0, 1])


def create_node(g, rgb, link, label):
    g.node(link, label=label, _attributes={'penwidth': '2', 'color': rgb}, )
    return g


def create_edge(g, parent, child, label, rgb):
    g.edge(parent, child, color=rgb, style='solid', _attributes={'penwidth': '1', 'fontcolor': rgb},
           label=label)
    return g


if __name__ == "__main__":
    g = graphviz.Digraph()

    # nodes
    g = create_node(g, red, 'odom', 'odom'+'\n(world link)')
    g = create_node(g, black, 'base_footprint', 'base_footprint')
    g = create_node(g, black, 'AGV_link', 'AGV_link')
    g = create_node(g, black, 'base_link', 'base_link')
    g = create_node(g, black, 'shoulder_link', 'shoulder_link')
    g = create_node(g, black, 'upper_arm_link', 'upper_arm_link')
    g = create_node(g, black, 'forearm_link', 'forearm_link')
    g = create_node(g, black, 'wrist_1_link', 'wrist_1_link')
    g = create_node(g, black, 'wrist_2_link', 'wrist_2_link')
    g = create_node(g, black, 'wrist_3_link', 'wrist_3_link')
    g = create_node(g, black, 'ee_link', 'ee_link')
    g = create_node(g, black, 'gripper_link', 'gripper_link')
    g = create_node(g, black, 'ee_camera_link', 'ee_camera_link')
    g = create_node(g, black, 'ee_camera_rgb_frame', 'ee_camera_rgb_frame')
    g = create_node(g, black, 'ee_camera_depth_frame', 'ee_camera_depth_frame')
    g = create_node(g, black, 'ee_camera_depth_optical_frame',
                    'ee_camera_depth_optical_frame')
    g = create_node(g, green, 'ee_camera_rgb_optical_frame',
                    'ee_camera_rgb_optical_frame'+'\n(data from sensor ' + 'camera' + ')')
    g = create_node(g, black, 'AGV_camera_link', 'AGV_camera_link')
    g = create_node(g, black, 'AGV_camera_rgb_frame', 'AGV_camera_rgb_frame')
    g = create_node(g, green, 'AGV_camera_rgb_optical_frame', 'AGV_camera_rgb_optical_frame'+'\n(data from sensor ' + 'camera' + ')')
    g = create_node(g, black, 'AGV_camera_depth_frame', 'AGV_camera_depth_frame')
    g = create_node(g, black, 'AGV_camera_depth_optical_frame', 'AGV_camera_depth_optical_frame')
    g = create_node(g,black,'wheels_links','wheels_links')
    g = create_node(g,black,'inertial_link','inertial_link')
    g = create_node(g,black,'imu_link','imu_link')
    
    # edges
    g = create_edge(g,'odom','base_footprint','dynamic',black)
    g = create_edge(g,'base_footprint','AGV_link','static',black)
    g = create_edge(g,'AGV_link','base_link','To be calibrated\n'+'static',blue)
    g = create_edge(g,'base_link','shoulder_link','dynamic',black)
    g = create_edge(g,'shoulder_link','upper_arm_link','dynamic',black)
    g = create_edge(g,'upper_arm_link','forearm_link','dynamic',black)
    g = create_edge(g,'forearm_link','wrist_1_link','dynamic',black)
    g = create_edge(g,'wrist_1_link','wrist_2_link','dynamic',black)
    g = create_edge(g,'wrist_2_link','wrist_3_link','dynamic',black)
    g = create_edge(g,'wrist_3_link','ee_link','dynamic',black)
    g = create_edge(g,'ee_link','gripper_link','static',black)
    g = create_edge(g,'ee_link','ee_camera_link','static',black)
    g = create_edge(g,'ee_camera_link','ee_camera_rgb_frame','To be calibrated\n'+'static',blue)
    g = create_edge(g,'ee_camera_rgb_frame','ee_camera_rgb_optical_frame','static',black)
    g = create_edge(g,'ee_camera_link','ee_camera_depth_frame','static',black)
    g = create_edge(g,'ee_camera_depth_frame','ee_camera_depth_optical_frame','static',black)
    g = create_edge(g,'AGV_link','AGV_camera_link','static',black)
    g = create_edge(g,'AGV_camera_link','AGV_camera_rgb_frame','To be calibrated\n'+'static',blue)
    g = create_edge(g,'AGV_camera_rgb_frame','AGV_camera_rgb_optical_frame','static',black)
    g = create_edge(g,'AGV_camera_link','AGV_camera_depth_frame','static',black)
    g = create_edge(g,'AGV_camera_depth_frame','AGV_camera_depth_optical_frame','static',black)
    g = create_edge(g,'AGV_link','wheels_links','dynamic',black)
    g = create_edge(g,'AGV_link','inertial_link','static',black)
    g = create_edge(g,'AGV_link','imu_link','static',black)
    
    # render graph
    g.render(filename='tree', cleanup=True)
    
    g.format = 'png'
    g.render('tree', view=True, cleanup=True)
