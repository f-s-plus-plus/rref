def rref(matrix):
    #checks to see if the dimensions of the matrix is valid
    if(len(matrix) + 1) == len(matrix[0]):

        #takes care of the lower staircase
        row = 0
        while row < len(matrix):
            inc = 1
            if matrix[row][row] != 0 and (inc + row) < len(matrix):
                while (inc + row) < len(matrix):
                    column = row
                    multiplier = matrix[row + inc][column] / matrix[row][column]
                    while column < len(matrix[row]):
                        matrix_row = matrix[row]
                        matrix[row + inc][column] = matrix[row + inc][column] - multiplier * matrix_row[column]
                        column += 1
                    inc += 1
            row += 1

        #takes care of the upper staircase
        row = len(matrix) - 1
        while row > 0:
            inc = 1
            while row - inc >= 0:
                column = row
                multiplier = matrix[row - inc][column] / matrix[row][column]
                column = len(matrix[0]) - 1
                while column >= row:
                    matrix[row - inc][column] = matrix[row - inc][column] - multiplier * matrix[row][column]
                    column -= 1
                inc += 1
            row -= 1

        #turns all the coefficients into 1s
        while row < len(matrix):
            multiplier = 1 / matrix[row][row]
            column = 0
            while column < len(matrix[row]):
                matrix[row][column] = multiplier * matrix[row][column]
                if matrix[row][column] == -0.0:
                    matrix[row][column] = 0
                column += 1
            row += 1
        return matrix
    else:
        #returns null if the dimensions are invalid
        return None


matrix_pass = [
    [1, 2, 6, 4],
    [3, 2, 4, 5],
    [0, 9, 2, 5]
]
print(rref(matrix_pass))