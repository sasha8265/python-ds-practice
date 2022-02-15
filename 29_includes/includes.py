def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    
    # make a conditional for isinstance(collection, dict)
    # if sought is in values of dict collection return True
    
    # originally had this one listed after isinstance(collection, set) but didn't work - not sure why
    if isinstance(collection, dict):
        return sought in collection.values()

    # make a conditional for isinstance(collection, set) 
    # if sought is in collection return True
    if start is None or isinstance(collection, set):
        return sought in collection

    # if not a set or dict or start is not None
    # check if sought is in collection, starting at start index until the end of collection:
    return sought in collection[start:]

