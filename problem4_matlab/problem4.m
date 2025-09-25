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
% # Last update: May 14, 2024
clc
clear all
close all
%% Main Body of Code
disp("===================================================")
disp("Enter any two numbers")
a = input("Enter the first number ");
b = input("Enter the second number ");

fprintf('First Element: %d \n',car(cons(a,b)))
fprintf('Last Element: %d \n',cdr(cons(a,b)))
disp("===================================================")

function [pair] = cons(a,b)
    pair = [a,b];
    return
end

function elem1 = car(pair)
    elem1 = pair(1);
    return
end

function elem2 = cdr(pair)
    elem2 = pair(end);
    return
end