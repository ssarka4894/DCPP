function [value] = returnProductList(ListInput,elem_len)
    result = [];
    for i=1:elem_len
        mul = 1;
            for j=1:elem_len
                if j ~= i
                    mul = mul*ListInput(j);
                end
            end
        result = [result, mul];
    end
    value = result;
    return
end