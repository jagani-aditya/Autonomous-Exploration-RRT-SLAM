# Autonomous Exploration RRT SLAM

## Project Description
This project addresses the subproblem of efficiently exploring unknown environments using RRT-SLAM to obtain a well-defined map. The algorithm identifies target points yielding the biggest contribution to a specific gain function at an initially unknown algorithm. Using which, it can efficiently search non-convex, high dimensional spaces by randomly drawing samples from the search space and building a space-filling tree that is inhertly biased to grow towards large unsearched areas.

## Platform
* Ubuntu 18.04 LTS
* ROS Melodic
* Gazebo 
* RViz

## Implementation
 
Navigate to the ROS package in the ```catkin_ws``` folder

```$ catkin_make```

```$ source devel/setup.bash ```

``` roslaunch explore_env turtlebot_gazebo.launch ``` 
