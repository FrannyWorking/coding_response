
# A quick note
# When I read this function requirement, I felt a bit confused.
# It first asks to reverse a list, but later it also asks for sorting a list.
# This means that the sorted list will effectively overwrite the reversed list,
# making the reverse process somewhat redundant.
# In a real work situation, I would confirm the details of this requirement with
# the person who proposed it to ensure that we both have a mutual understanding.
# In this coding test, if the task were simply to reverse the list, I would only need to return l[::-1].
# However, if it’s to reverse and then sort, the focus might be more on the sorting part.
# Please see the specific solution below. Thank you.

def reverse_list(l: list):
    """

    TODO: Reverse a list without using any built in functions



    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """
    # if the function was to reverse the list and then sort
    # please uncomment all the line between line 29 and 35
    # and comment line 37

    # l = l[::-1]
    # n = len(l)
    # for i in range(n):
    #     for j in range(0, n - i - 1):
    #         if l[j] > l[j + 1]:
    #             l[j], l[j + 1] = l[j + 1], l[j]
    # return l

    return l[::-1]


def solve_sudoku(matrix):
    """

    TODO: Write a programme to solve 9x9 Sudoku board.



    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.



    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """

    # a boolean value used in backtrack function
    finished = False

    def checkValidNum(matrix, i, j, num):
        # check if rows has already contains num
        if num in matrix[i][:]:
            return False
        # check if columns has already contains num
        if num in [row[j] for row in matrix]:
            return False
        # check if 3x3 board has already contains num
        if num in [matrix[i//3*3+row][j//3*3+column] for row in range(3) for column in range(3)]:
            return False
        return True

    # i is row, j is column
    def backtrack(matrix, i, j):
        nonlocal finished
        # reach the base case
        if i == 9:
            finished = True
            return

        # if it traverses to the column end
        # switch to next row
        if j == 9:
            backtrack(matrix, i+1, 0)
            return

        # skip non empty entry
        if matrix[i][j] != 0:
            backtrack(matrix, i, j+1)
            return

        # try number from 1 to 9 for each empty entry
        for num in range(1, 10):
            # check if a number is valid in empty entry
            if not checkValidNum(matrix, i, j, num):
                continue
            matrix[i][j] = num
            backtrack(matrix, i, j+1)
            # once finished, return the function, otherwise it will withdraw the change
            if finished:
                return
            matrix[i][j] = 0

    # call backtrack to solve sudoku
    backtrack(matrix, 0, 0)


if __name__ == "__main__":
    # test case for reverse_list
    num_list = [8, 2, 5, 6, 1]
    float_list = [3.1, 2.3, 1.9, 5.7, 9.1]
    str_list = ['ice', 'apple', 'banana', 'meat', 'drink']
    res1 = reverse_list(num_list)
    res2 = reverse_list(float_list)
    res3 = reverse_list(str_list)
    print(res1)
    print(res2)
    print(res3)

    # test case for solve_sudoku
    matrix = [[9, 0, 6, 8, 0, 1, 2, 0, 3],
              [0, 0, 0, 0, 4, 0, 0, 0, 0],
              [3, 0, 4, 0, 0, 0, 5, 0, 1],
              [2, 0, 0, 0, 0, 0, 0, 0, 8],
              [0, 6, 0, 0, 9, 0, 0, 5, 0],
              [5, 0, 0, 0, 0, 0, 0, 0, 6],
              [4, 0, 1, 0, 0, 0, 8, 0, 2],
              [0, 0, 0, 0, 1, 0, 0, 0, 0],
              [8, 0, 7, 6, 0, 3, 4, 0, 9]]

    sudoku_matrix = [[9, 7, 6, 8, 5, 1, 2, 4, 3],
                     [1, 2, 5, 3, 4, 9, 6, 8, 7],
                     [3, 8, 4, 2, 6, 7, 5, 9, 1],
                     [2, 4, 9, 5, 3, 6, 1, 7, 8],
                     [7, 6, 8, 1, 9, 2, 3, 5, 4],
                     [5, 1, 3, 7, 8, 4, 9, 2, 6],
                     [4, 3, 1, 9, 7, 5, 8, 6, 2],
                     [6, 9, 2, 4, 1, 8, 7, 3, 5],
                     [8, 5, 7, 6, 2, 3, 4, 1, 9]]

    solve_sudoku(matrix)
    for row in matrix:
        print(row)

