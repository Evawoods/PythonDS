def frequency(num):
    freq = {}
    for digit in num:
        freq[digit] = freq.get(digit, 0) + 1
    return freq

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    return frequency(str(num1)) == frequency(str(num2))