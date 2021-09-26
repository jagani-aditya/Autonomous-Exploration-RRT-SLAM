#!/usr/bin/env python3

# Import libraries
import rospy
from nav_msgs.msg import OccupancyGrid

# Create object
map = OccupancyGrid()

def map_data_callback(data):

    # Detects the number of points that are explored and logs it in a file
    # File is stored in ~/.ros directory

    map_occupancy = data.data
    count = 0
    for i in map_occupancy:
        if i != -1:
            count = count + 1
        else:
            continue

    time = rospy.get_time()

    with open("manual_map3data.txt", "a") as f:
        f.write(str(count) + '\n')

    with open("manual_time3data.txt", "a") as g:
        g.write(str(time) + '\n')

if __name__ == '__main__':

    try:
        # Initialize the node
        rospy.init_node('data_logger_node')

        # Subscribes from map
        rospy.Subscriber('/map', OccupancyGrid, map_data_callback)

        # Spins the node
        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("Data Logging finished.")