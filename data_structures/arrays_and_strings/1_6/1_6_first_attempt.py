def rotate_pixels(img_matrix):
    res = []
    num_rows = len(img_matrix)
    num_cols = len(img_matrix[0])
    for i in range(num_rows):
        new_row = []
        for j in range(num_cols):
            new_row.append(img_matrix[num_cols - j - 1][i])
        print(new_row)
        res.append(new_row)
    return res


def main():
    # print
    # [7, 4, 1]
    # [8, 5, 2]
    # [9, 6, 3]
    rotate_pixels([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print(rotate_pixels([
        [2, 3, 4, 5],
        [3, 4, 5, 6],
        [4, 5, 6, 7],
        [5, 6, 7, 8]
    ]) == [
        [5, 4, 3, 2],
        [6, 5, 4, 3],
        [7, 6, 5, 4],
        [8, 7, 6, 5]
    ])


if __name__ == "__main__":
    main()