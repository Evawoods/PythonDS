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

    occurs = {}

    for num in nums:
        occurs[num] = occurs.get(num,0) + 1
        
    mode_val = max(occurs, key=occurs.get)

    return mode_val
