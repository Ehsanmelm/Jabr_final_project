from copy import deepcopy

def GosJordan_diag(matrix):
    diag = 1
    copy_matrix = deepcopy(matrix)

    row , col = len(matrix) , len(matrix[0])
    
    for i in range(min(row,col)):
        # main_row = i

        # for j in range(i+1 , row):

        #     if abs(copy_matrix[j][i])> abs(copy_matrix[main_row][i]):
        #         main_row = j

# --------------------

        # if main_row != i:

        #     temp = copy_matrix[i] 
        #     copy_matrix[i] = copy_matrix[main_row]
        #     copy_matrix[main_row] = temp
        
        main_element = copy_matrix[i][i]
        diag *= main_element

        if main_element != 0 :

            for j in range((len(copy_matrix[i]))):
                copy_matrix[i][j] /= float(main_element)

        for j in range(row):

            if j != i:

                factor = copy_matrix[j][i] / copy_matrix[i][i] if copy_matrix[i][i] != 0 else 0

                for k in range(len(copy_matrix[j])):
                    copy_matrix[j][k] = copy_matrix[j][k] - (factor * copy_matrix[i][k])
      
    for i in range(row):
        for j in range(col):
            if i==j : 
                diag*= copy_matrix[i][j]
    return diag , copy_matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[-1,3,2], [3,-2,1], [5,-1,-3]]
matrix = [[1,2,3], [0,1,2], [-1,2,1]]
matrix = [ [5,4,2,1], [2,3,1,-2], [-5,-7,-3 ,9] , [1,-2,-1,4] ]
matrix = [[1,5], [6,2]]

diag = GosJordan_diag(matrix)
print(diag)