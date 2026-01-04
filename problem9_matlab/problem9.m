%% Refresh
clc
clear all
close all
%%
s = 'abcba';
k = 2;

result = longestSubstringKDistinct(s, k);
disp(result);   % Output: 3


function maxLen = longestSubstringKDistinct(s, k)
    % Handle edge cases
    if k <= 0 || isempty(s)
        maxLen = 0;
        return;
    end

    n = length(s);
    left = 1;
    maxLen = 0;

    % Map characters to counts using containers.Map
    freq = containers.Map('KeyType','char','ValueType','int32');

    for right = 1:n
        c = s(right);
        if isKey(freq, c)
            freq(c) = freq(c) + 1;
        else
            freq(c) = 1;
        end

        % Shrink window if more than k distinct characters
        while freq.Count > k
            leftChar = s(left);
            freq(leftChar) = freq(leftChar) - 1;
            if freq(leftChar) == 0
                remove(freq, leftChar);
            end
            left = left + 1;
        end

        % Update maximum length
        maxLen = max(maxLen, right - left + 1);
    end
end
