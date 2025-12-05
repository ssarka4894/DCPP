%% Refresh
clc
clear all
close all
%% Count Elements
n = 25;
X = [1, 2];
value = count_step(n, X);
fprintf("================================================= \n")
fprintf("The number of probable step: %d \n", value)
fprintf("================================================= \n")

% Define function count_step
% with number of total steps: n
% and a set of possible steps taken: X
function result = count_step(n, X)
    storage = zeros(n + 1, 1);
    storage(1) = 1;
    for i = 1:n + 1
        for j = 1: length(X)
            if i - X(j) > 0
                storage(i) = storage(i) + storage(i - X(j));
            end
        end
    end
    result = storage(n + 1);
end

