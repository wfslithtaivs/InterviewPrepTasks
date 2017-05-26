def len_between_indexes(array, start, finish):
    """" Calculates amount of rain between given buildings"""
    amount = 0

    max_value = min(array[start], array[finish])

    if finish == -1 and len(array) == 3: 
            amount += max_value - array[1]

    elif finish == -1 and len(array) > 3: 
        for i in range(start + 1, len(array)):
            amount += max_value - array[i]               
    else:
        for i in range(start + 1, finish):
            amount += max_value - array[i]

    return amount

def rain(buildings):
    """How much rain is trapped in Codelandia?"""

    rain_amount = 0
    rain_stack = []
    a = buildings + [0] # sentinell 

    if len(a) < 3:
        return rain_amount

    else:
        if a[0] > a[1]: # first element is a local maximum
            rain_stack.append(0)

        # iterate over list of buildings
        for i in range(1, len(a) - 1):

             # if we have a local maximum (optimization)
           if a[i] > a[i-1] and a[i] >= a[i+1]:

                while len(rain_stack) > 1 and a[rain_stack[-1]] <= a[i]:
                    rain_stack.pop()

                if len(rain_stack) == 1 and a[rain_stack[-1]] <= a[i]:
                    rain_amount += len_between_indexes(a, rain_stack[-1], i)
                    rain_stack.pop()

                rain_stack.append(i)
                
    while len(rain_stack) > 1:
        rain_amount += len_between_indexes(a, rain_stack[0], rain_stack[1])
        rain_stack.pop(0)
    return rain_amount

print rain([10, 5, 10]) #5
print rain([10, 2, 3, 4, 10]) #21
print rain([2, 3, 10, 5, 5, 10, 3, 2]) #10
print rain([4, 2, 3, 3, 3]) #1
print rain([4, 2, 3, 3, 3, 4]) #1
