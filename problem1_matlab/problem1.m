%% Refresh
%# Created by:
%##################################
%#########SOHAM SARKAR#############
%#####Arizona State University#####
%##################################

% # Do NOT distribute without written permission from Soham Sarkar
% # Do NOT use it for any commercial purpose
% 
% # Contact email: ssarka30@asu.edu
% # Last update: June 20, 2023
clc
clear all
close all
%% Main Body of Code
ListInput = input("Enter your list of numbers: ");
elem_len = length(ListInput)
KInput = input("Enter a number: ");

a = checkEqual(ListInput,elem_len,KInput);
if a == 1
    disp("True")
else
    disp("False")
end
