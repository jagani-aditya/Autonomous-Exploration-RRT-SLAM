#!/usr/bin/env python3

# Import libraries
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from rrt_exploration.msg import PointArray
from functions import robot,informationGain,discount
from numpy.linalg import norm
from copy import copy
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point
import random


global visited_nodes
visited_nodes = []

mapData=OccupancyGrid()
info_radius = 1.0

global x
global y
global count 

count = 0

def compute_distance(a,b):
    x1,y1 = a[0],a[1]
    x2,y2 = b[0],b[1]

    x = (x2 - x1)**2
    y = (y2-y1)**2

    dist = (x + y)**0.5

    return dist

def odom_cb(data):
    # Calculates robots current location using Odometry

    global robot_x
    global robot_y

    robot_x = data.pose.pose.position.x
    robot_y = data.pose.pose.position.y
    
def detected_points_callback(data):
    flag = 0

    frontiers=[]
    for point in data.points:
        frontiers.append([point.x,point.y])

    centroids=copy(frontiers)	

    #------------------------ determines max info gain-------------------------------------------------			
    infoGain=[]
    info_radius = 1.0


    for ip in range(0,len(centroids)):
        infoGain.append(informationGain(mapData,[centroids[ip][0],centroids[ip][1]],info_radius))

    #---------------------------------------------------------------------------------------------------			
    index = infoGain.index( max(infoGain) )
    closest_frontier_loc = centroids[index]

    goal_x = closest_frontier_loc[0]
    goal_y = closest_frontier_loc[1]
    visited_nodes.append([goal_x,goal_y])

    prev_goal_x = goal_x
    prev_goal_y = goal_y


    goal_point = Point()
    goal_point.x = goal_x
    goal_point.y = goal_y
    

    if (abs(robot_x - goal_x) < 5.5) and (abs(robot_y - goal_y) < 5.5):
        print('GOAL X = ',goal_x, ' GOAL Y = ', goal_y )
        goal_pub.publish(goal_point)    
        print("============================")
    
    else: pass




if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')

        global goal_pub
        goal_pub = rospy.Publisher('/goal_locs',Point,queue_size = 2)

        rospy.Subscriber('/filtered_points', PointArray, detected_points_callback)
        rospy.Subscriber('/odom', Odometry, odom_cb)
        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")