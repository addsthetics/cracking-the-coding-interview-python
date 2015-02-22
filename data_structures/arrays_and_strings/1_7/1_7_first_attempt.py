def zero_matrix(matrix):
    """
    O(MN) and space of O(1)
    """
    m = len(matrix)
    n = len(matrix[0])
    zero_rows = []
    zero_cols = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.append(i)
                zero_cols.append(j)

    for row in zero_rows:
        zero_row(matrix, row, n)

    for column in zero_cols:
        zero_column(matrix, column, m)

    return matrix


def zero_row(matrix, row, num_cols):
    for i in range(num_cols):
        matrix[row][i] = 0


def zero_column(matrix, column, num_rows):
    for i in range(num_rows):
        matrix[i][column] = 0


def main():
    # True
    print(
        zero_matrix(
            [
                [1, 1, 1, 1],
                [1, 0, 1, 1],
                [1, 1, 1, 1],
            ]
        ) ==
        [
            [1, 0, 1, 1],
            [0, 0, 0, 0],
            [1, 0, 1, 1],
        ]
    )
    #True
    print(
        zero_matrix(
            [
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1],
            ]
        ) ==
        [
            [0, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
        ]
    )
    print(
        zero_matrix(
            [
                [1, 0, 1],
                [1, 1, 0],
                [0, 1, 1],
            ]
        ) ==
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    )


if __name__ == "__main__":
    main()