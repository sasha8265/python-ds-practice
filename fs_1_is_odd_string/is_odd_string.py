def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here

    # Use ASCII number for each character (a = 97) and use it to subtract from the ASCII number of each char to get a single number (character ASCII - (97 - 1))
    
    # would also work if we don't do the extra math and just use the ASCII numbers as they are

    base_val = ord("a") - 1

    total = sum((ord(char) - base_val) for char in word.lower())
    # print(total)

    if total % 2 == 0:
        return False
    
    return True



