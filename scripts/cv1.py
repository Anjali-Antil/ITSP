#!/usr/bin/env python3
import controler
import rospy
from time import sleep
import numpy as np
import math


def return_oringin(iris):
    iris.set_waypoint(iris.curr_x, iris.curr_y, 10)
    iris.set_pose()
    iris.set_waypoint(0,0, 10)
    iris.set_pose()
    iris.land(0.01)




if __name__ == '__main__':
    try:
        iris_controller = controler.Flight_controller()
    except rospy.ROSInterruptException:
        pass
    alt = 3.0
    iris_controller.toggle_arm(True)
    iris_controller.takeoff(alt)
    iris_controller.set_offboard_mode()
    
   
    iris_controller.move_to(2, 1, 3)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, 0)
    iris_controller.set_pose()
    print(iris_controller.curr_yaw)
    iris_controller.move_to(2, 1, 3)
    print(iris_controller.curr_yaw)
    
    
    iris_controller.move_to(1, 1, 3)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, 0)
    iris_controller.set_pose()
    print(iris_controller.curr_yaw)
    iris_controller.move_to(1, 1, 3)
    print(iris_controller.curr_yaw)
    
    
    
    sleep(10)
    #return_oringin(iris_controller)
    
