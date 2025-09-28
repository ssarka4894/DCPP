%% Refresh
%# Created by:
%##################################
%#########SOHAM SARKAR#############
%#####Arizona State University#####
%##################################

% # Do NOT distribute without written permission from Soham Sarkar
% # Do NOT use it for any commercial purpose
% 
% This problem was asked by Microsoft.

% Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.
% 
% Bonus: When, during the course of a day, will the angle be zero?

% # Contact email: ssarka30@asu.edu
% # Last update: May 14, 2024
clc
clear all
close all
%% Main Body of Code
disp("===================================================")
disp("Enter any two numbers")
hh = input("Enter the time in hours: ");
mm = input("Enter the time in minutes: ");
disp("===================================================")

fprintf('Angle Difference between minute hand and hour hand = %f \n', ...
    calculate_angle_diff(hh,mm));


function ang_diff = calculate_angle_diff(hh,mm)
    if hh > 12
        hh = hh - 12;
    end
    hour_hand_angle = hh*(360/12) + mm*(30/60);
    minute_hand_angle = mm*(360/60);
    
    fprintf('Hour Hand Angle = %f \n',hour_hand_angle);
    fprintf('Minute Hand Angle = %f \n',minute_hand_angle)
    
    ang_diff = abs(minute_hand_angle - hour_hand_angle);
    return
end
% 
% function elem1 = car(pair)
%     elem1 = pair(1);
%     return
% end
% 
% function elem2 = cdr(pair)
%     elem2 = pair(end);
%     return
% end