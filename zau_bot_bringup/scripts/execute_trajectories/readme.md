This script was developed to help record a bag file:

    rosrun zau_bot_bringup execute_trajectories

The script reads a csv file with a list of number, where each line is composed by 6 numbers, each number corresponding to a joint in the manipulator.
In other words, each line is a manipulator pose.

**How to use:**

_1._ The csv file already contains several poses, but to add new poses just uncomment this line and comment the line underneath:

zau_bot/zau_bot_bringup/scripts/execute_trajectories/execute_trajectories

https://github.com/JorgeFernandes-Git/zau_bot/blob/a0a1ece6515f83134ed92b7ae7f01a90b1f5492f/zau_bot_bringup/scripts/execute_trajectories/execute_trajectories#L199-L200

Open the robot on Rviz, put it in the desired pose and run the script:

    rosrun zau_bot_bringup execute_trajectories

The new pose will be added to the csv file in the last line.

_2._ Reverse the changes made above and run it. If no new poses are needed, just run it. The csv file has 45 poses, starting from the robot's home position.