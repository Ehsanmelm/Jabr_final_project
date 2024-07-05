from copy import deepcopy

def GosJordan_diag(matrix, eps=1e-12):
    diag = 1
    copy_matrix = deepcopy(matrix)

    row, col = len(matrix), len(matrix[0])

    for i in range(min(row, col)):
        main_element = copy_matrix[i][i]

        if abs(main_element) < eps:
            return 0.0

        diag *= main_element

        for j in range(len(copy_matrix[i])):
            copy_matrix[i][j] /= main_element

        for j in range(row):
            if j != i:
                factor = copy_matrix[j][i]
                for k in range(len(copy_matrix[j])):
                    copy_matrix[j][k] -= factor * copy_matrix[i][k]

    for i in range(row):
        diag *= copy_matrix[i][i]

    return diag

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[-1,3,2], [3,-2,1], [5,-1,-3]]
matrix = [[1,2,3], [0,1,2], [-1,2,1]]
matrix = [ [5,4,2,1], [2,3,1,-2], [-5,-7,-3 ,9] , [1,-2,-1,4] ]
matrix = [[1,5], [6,2]]

dim_num = int(input())
matrix = []
for i in range(dim_num):
    arr = list(map(float , input().split()))
    matrix.append(arr)

diag = GosJordan_diag(matrix)
print(f"{int(diag)}")