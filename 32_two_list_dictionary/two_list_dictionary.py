def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

    # if len(keys) == len(values):
    #     for value in values:
    #         for key in keys:
    #             return {key:value}

    new_dict = {}

    # enumerate will give 2 loop variables:
    # 1st is the count of the iteration (defaults to start at 0 if not defined)
    # 2nd is the value of the iteration
    # will stop once the end of the length of keys is reached

    for idx, key in enumerate(keys):
        if idx < len(values):
            new_dict[key] = values[idx]
        # return None for the value if there are fewer values than keys
        else:
            new_dict[key] = None

    return new_dict