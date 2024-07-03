
# # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # matrix = [[-1,3,2], [3,-2,1], [5,-1,-3]]
# # matrix = [[1,2,3], [0,1,2], [-1,2,1]]
# # matrix = [ [5,4,2,1], [2,3,1,-2], [-5,-7,-3 ,9] , [1,-2,-1,4] ]
# # matrix = [[1,5], [6,2]]
# # matrix = [[1,3], [6,8]]


def laplas_diag_method(matrix):
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 0:
            return 0
        
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    elif n == 1:
        return matrix[0][0]

    det = 0
    for j in range(n):
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        sign = (-1) ** (j % 2)
        sub_det = laplas_diag_method(sub_matrix)
        det += sign * matrix[0][j] * sub_det

    return det

dim_num = int(input())
matrix = []

for i in range(dim_num):
    arr = list(map(float , input().split()))
    matrix.append(arr)

det = laplas_diag_method(matrix)
print(f"{det:.2f}")

