import random
from copy import deepcopy

def GosJordan_diag(matrix):
    diag = 1
    copy_matrix = deepcopy(matrix)

    row , col = len(matrix) , len(matrix[0])
    
    for i in range(min(row,col)):

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
    return diag 

def key_matrix_creator():
    matrix = [[random.randint(0,10) for row in range(2)] for col in range(2)]

    key_matrix_diag = GosJordan_diag(matrix)

    if key_matrix_diag == 0:
        key_matrix_creator()

    return matrix

print(key_matrix_creator())