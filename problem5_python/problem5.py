# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 06:15:01 2024

@author: soham

This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

"""

import numpy as np
    
hh = float(input('Enter the time in hours: '))
mm = float(input('Enter the time in minutes: '))


def calculate_angle_diff(hh,mm):
    hour_hand_angle = hh*(360/12) + mm*(30/60)
    min_hand_angle = mm*(360/60)
    
    print('Hour Hand Angle =',hour_hand_angle)
    print('Minute Hand Angle =',min_hand_angle)
    
    return abs(hour_hand_angle - min_hand_angle)
    

print('Difference Between Hour Hand and Minute Hand =', calculate_angle_diff(hh, mm))