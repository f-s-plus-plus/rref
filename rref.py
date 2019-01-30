def rref(matrix):
    if((len(matrix) + 1) == len(matrix[0])):
        row = 0
        while row < len(matrix):
            inc = 1
            if (matrix[row][row] != 0 and (inc + row) < len(matrix)):
                while (inc + row) < len(matrix):
                    column = row
                    multiplier = matrix[row + inc][column] / matrix[row][column]
                    while column < len(matrix[row]):
                        matrix_row = matrix[row]
                        matrix[row + inc][column] = matrix[row + inc][column] - multiplier * matrix_row[column]
                        column += 1
                    inc += 1
            row += 1

        row = len(matrix) - 1
        column = len(matrix[0]) - 2
        inc = 1
        print(str(row) + " : " + str(column))
        while row > 0:
            multiplier = matrix[row - inc][column] / matrix[row][column]
            column = len(matrix[0]) - 1
            if(row == column):
                row -= 1
                inc = 1
            else:
                column -= 1
            matrix[row - inc][column] = matrix[row - inc][column] - multiplier * matrix[row][column]



        for row in matrix:
            print(row)
    else:
        print("The dimensions are off!")


matrix_pass = [
    [1, 2, 6, 4],
    [3, 2, 4, 5],
    [1, 9, 2, 5]
]

rref(matrix_pass)