#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Point
import time

def goal_points_callback(data):

    goal_x = data.x
    goal_y = data.y

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = goal_x
    goal.target_pose.pose.position.y = goal_y
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)
    #wait = client.wait_for_result()


if __name__ == '__main__':
    try:
        rospy.init_node('robot_goal_allocator')

        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        rospy.loginfo('============ Waiting for Server ============')
        client.wait_for_server()
        rospy.loginfo('============ Action Server is Available ============')

        rospy.Subscriber('/goal_locs', Point, goal_points_callback)

        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")