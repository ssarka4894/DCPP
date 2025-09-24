function [value] = find_lowest_positive_integer(ListInput,elem_len)
    output = 1;
    counter = 1;
    for i=1:elem_len
        if ListInput(i) > 0
            if ismember(counter, ListInput)
                counter = counter + 1;
            end
            output = counter;
        end
    end
    value = output;
    return
end