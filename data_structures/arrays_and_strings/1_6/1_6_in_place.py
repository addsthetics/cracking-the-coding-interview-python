def rotate_pixels(img_matrix):
    n = len(img_matrix)
    for i in range(n/2):
        for j in range(i, n - i - 1):
            # i = 0, 1
            top = img_matrix[i][j]
            #Bring left to top
            img_matrix[i][j] = img_matrix[n - j - 1][i]
            #Move bottom to left
            img_matrix[n - j - 1][i] = img_matrix[n - i - 1][n - j - 1]
            #Move right to bottom
            img_matrix[n - i - 1][n - j - 1] = img_matrix[j][n - i - 1]
            #Move top to the right
            img_matrix[j][n - i - 1] = top
    return img_matrix

def main():
    # print
    # [7, 4, 1]
    # [8, 5, 2]
    # [9, 6, 3]
    print (rotate_pixels([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))

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