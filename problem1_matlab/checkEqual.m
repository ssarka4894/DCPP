function [value] = checkEqual(ListInput,elem_len,KInput)
    c=0;
    
    for i=1:elem_len
        for j=1:elem_len
            sum = 0;
            if j >= i
                sum = ListInput(i) + ListInput(j);
                if sum == KInput
                    value = true;
                    c = c+1;
                    return
                end
            end
        end
    end

    if c==0
        value = false;
        return
    end
end