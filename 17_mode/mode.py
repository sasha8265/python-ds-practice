def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # Count the number of times each number appears and add to a counter dictionary
    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    # find the largest value / highest frequency in the dictionary
    highest = max(counter.values())

    # return the key with the highest value
    for (num, count) in counter.items():
        if count == highest:
            return num
