## Run the script

    rosrun zau_bot_bringup dual_cam.py 

Configure the camera's topics on the topics.yaml in the config folder.

![dual_cam](https://user-images.githubusercontent.com/80167550/225006875-1c8b5ed5-ae3d-458d-9842-6b913746a203.png)

Useful commands to determine the queue_size and the slop for the ApproximateTimeSynchronizer:

    rostopic list

    rostopic info /my_topic

    rostopic echo /my_topic

    rostopic hz /my_topic


