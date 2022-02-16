def counter(collection):
    counts = {}

    for x in collection:
        counts[x] = counts.get(x,0) + 1
    
    return counts


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    
    return counter(str(num1)) == counter(str(num2))



# ORIGINAL SOLUTION - before new counter function

# def same_frequency(num1, num2):

#     num1_str = sorted(str(num1))
#     num2_str = sorted(str(num2))
#     new_dict1 = {}
#     new_dict2 = {}
    
#     for n in num1_str:
#         count = num1_str.count(n)
#         new_dict1[n] = count

#     for n in num2_str:
#         count = num2_str.count(n)
#         new_dict2[n] = count
    
#     return new_dict1 == new_dict2