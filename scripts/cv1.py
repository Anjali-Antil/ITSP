#!/usr/bin/env python
import controler
import rospy
from time import sleep
import numpy as np
import math
import cv2
from pyzbar.pyzbar import decode

with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()
print (myDataList)


def return_oringin(iris):
    iris.set_waypoint(iris.curr_x, iris.curr_y, 1.5)
    iris.set_pose()
    iris.set_waypoint(0,0, 1.5)
    iris.set_pose()
    iris.land(0.01)

def helper(img):
    for barcode in decode(img):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        
        if myData in myDataList:
            myOutput ='Authorized'
            print(myOutput)
            myColor = (0,255,0)
        else:
            myOutput ='UnAuthorized'
            print(myOutput)
            myColor = (0,0,255)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)
    
    
    return img


class trajectory:
    def __init__(self):
        self.waypoints = []
        self.coff = []
        self.index = []


if __name__ == '__main__':
    try:
        iris_controller = controler.Flight_controller()
    except rospy.ROSInterruptException:
        pass
    alt = 2.0
    iris_controller.toggle_arm(True)
    iris_controller.takeoff(alt)
    iris_controller.set_offboard_mode()
   
    
   
    iris_controller.move_to(0, 0.5, 1.4)
    img = helper(iris_controller.rgb_image)
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    sleep(5)
    img = helper(iris_controller.rgb_image)
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    sleep(5)
    img = helper(iris_controller.rgb_image)
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    sleep(5)
    
    iris_controller.move_to(-0.5, 1.0, 1.8)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, math.pi)
    iris_controller.set_pose()
    print(iris_controller.curr_yaw)
    iris_controller.move_to(-0.5, 1.0, 1.8)
    print(iris_controller.curr_yaw)
    img = helper(iris_controller.rgb_image)
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    sleep(5)
    img = helper(iris_controller.rgb_image)
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    sleep(10)
    iris_controller.move_to(3, -1, 1.4)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, math.pi/2)
    iris_controller.set_pose()
    img = helper(iris_controller.rgb_image)
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    sleep(10)
    img = helper(iris_controller.rgb_image)
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    sleep(10)
    return_oringin(iris_controller)
    '''
    iris_controller.move_to(-0.5,9.5,1.4)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, 0)
    iris_controller.set_pose()
    print(iris_controller.curr_yaw)
    iris_controller.move_to(-0.5,9.5,1.4)
    print(iris_controller.curr_yaw)
    img = helper(iris_controller.rgb_image)
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    iris_controller.move_to(4.1,8,1.3)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, 0)
    iris_controller.set_pose()
    print(iris_controller.curr_yaw)
    iris_controller.move_to(4.1,8,1.3)
    print(iris_controller.curr_yaw)
    img = helper(iris_controller.rgb_image)
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    iris_controller.move_to(7,0,3)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, 0)
    iris_controller.set_pose()
    print(iris_controller.curr_yaw)
    iris_controller.move_to(7,0,3)
    print(iris_controller.curr_yaw)
    
    iris_controller.move_to(4.4, -0.5, 1.4)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, 0)
    iris_controller.set_pose()
    print(iris_controller.curr_yaw)
    iris_controller.move_to(4.4, -0.4, 1.4)
    print(iris_controller.curr_yaw)

    #iris_controller.set_waypoint(-3.5,2, alt)
    #iris_controller.set_pose()'''
    '''print('Current yaw  : '+str(iris_controller.curr_yaw))
    print('set yaw = 0')
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, 0)
    iris_controller.set_pose()
    sleep(3)
    print('set yaw = 1')
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, math.pi/2)
    iris_controller.set_pose()
    print(iris_controller.curr_yaw)
    sleep(5)'''
    '''iris_controller.move_to(5, 0, 3)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, 0)
    
    iris_controller.set_pose()
    print(iris_controller.curr_yaw)
    iris_controller.move_to(5, 0, 3)
    print(iris_controller.curr_yaw)
    sleep(10)'''
    '''while True:
        iris_controller.move_to(iris_controller.target_x,iris_controller.target_y,iris_controller.target_z)
        iris_controller.set_orientation(iris_controller.curr_roll,iris_controller.curr_pitch, iris_controller.target_angle)
        iris_controller.set_pose()'''
    '''iris_controller.move_to(0, 0, 1.5)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, 0)
    iris_controller.set_pose()
    sleep(5)
    iris_controller.set_orientation(iris_controller.curr_roll, iris_controller.curr_pitch, math.pi/2)
    iris_controller.set_pose()
    sleep(3)
    image = iris_controller.rgb_image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #return_oringin(iris_controller)'''

    cv2.destroyAllWindows()

    