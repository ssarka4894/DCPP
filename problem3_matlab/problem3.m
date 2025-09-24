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
% # Last update: July 19, 2023
clc
clear all
close all
%% Main Body of Code
ListInput = input("Enter your list of numbers: ");
elem_len = length(ListInput);
result = find_lowest_positive_integer(ListInput,elem_len)
