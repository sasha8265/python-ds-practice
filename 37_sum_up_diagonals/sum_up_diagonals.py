def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # create a total count starting at 0
    # find the index of each list in the matrix using range of the length of matrix
    # add values from each list using index from the range, and the same index in each list
    #do the same in reverse (-1) for the other diagonal (-1, -2, -3)

    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]

    return total



# m1 = [
#     [1,   2],
#     [30, 40],
# ]
# sum_up_diagonals(m1)


# m2 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# sum_up_diagonals(m2)