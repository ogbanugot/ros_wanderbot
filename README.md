# ros_wanderbot
ROS Simulation of the Kobuki robot

## Getting started with the wanderbot task

This guide assumes you have;  
-installed ROS (obviously)    
-installed turbot   
$ sudo apt-get install ros-kinetic-turtlebot   

## Build a catkin workspace

If you haven't already, create and build a catkin workspace

$ mkdir -p ~/catkin_ws/src  
$ cd ~/catkin_ws/  
$ catkin_make  

source your new setup.*sh file:  
$ source devel/setup.bash  

To make sure your workspace is properly overlayed by the setup script, make sure ROS_PACKAGE_PATH environment variable includes the directory you're in.  
$ echo $ROS_PACKAGE_PATH  
You should see  
/home/youruser/catkin_ws/src:/opt/ros/kinetic/share  

---

## Clone this repo and copy the folder "wanderbot" into 'catkin_ws/src' on your system

$ git clone ...  

## Building the wanderbot package    

1.First we have to change some things...  

Open catkin_ws/src/wanderbot/world/  
Open the file course.world  
Look for the line:  
<uri>file:///home/ugot/catkin_ws/src/wanderbot/world/course.material</uri>  
change 'ugot' to your own home/[ownername],   
you can find your 'ownername' by typing **pwd** on a new terminal  

2.Next install turtlebot_gazebo  

$ sudo apt-get install ros-kinetic-turtlebot-gazebo  

3.Finally let's build the wanderbot package  

cd into /catkin_ws  
Then run   

$ catkin_make  

This will add wanderbot to your package lists   
When this is done confirm by;  

$ rospack list

Check to see that wanderbot is on the list  

## Launch the wanderbot package

Launch wanderbot;  

$ roslaunch wanderbot course.launch

You should see the gazebo environment comeup with the turtlebot in the yellow stripped environment

goodluck :)  
