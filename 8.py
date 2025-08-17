from functools import reduce

def second_max(numbers):
    if not numbers:
        return None
        
    def reducer(acc, x):
        current_max, second_max_val = acc
        if current_max is None:
            return (x, None)
        if x > current_max:
            return (x, current_max)
        if x == current_max:
            return (current_max, x)
        if second_max_val is None or x > second_max_val:
            return (current_max, x)
        return acc
        
    return reduce(reducer, numbers, (None, None))[1]


print(second_max([5, 4, 3, 2, 5]))
print(second_max([1, 2, 3, 4]))
print(second_max([4, 4, 3, 2]))
print(second_max([1]))
print(second_max([]))