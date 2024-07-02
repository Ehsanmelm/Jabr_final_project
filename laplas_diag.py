def laplas_diag_method(matrix):
    if len(matrix) == 2 :
        val = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return val
    elif len(matrix) == 1:
        return matrix[0][0]

    det = 0
    for j in range(len(matrix)):

        sub_matrix = [[0 for col in range(len(matrix)-1)] for row in range(len(matrix)-1)]

        row= 0
        for i in matrix[1:]:
            sub_matrix[row] = i[:j] + i[j+1:]
            row+=1

        sign = (-1) ** (j % 2)  
        sub_det = laplas_diag_method(sub_matrix)
        det += sign * matrix[0][j] * sub_det
    
    return det

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[-1,3,2], [3,-2,1], [5,-1,-3]]
matrix = [[1,2,3], [0,1,2], [-1,2,1]]
matrix = [ [5,4,2,1], [2,3,1,-2], [-5,-7,-3 ,9] , [1,-2,-1,4] ]
matrix = [[1,5], [6,2]]

print(laplas_diag_method(matrix))
