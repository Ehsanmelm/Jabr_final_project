from copy import deepcopy

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

def get_minor_matrix(matrix, i, j):
    minor = deepcopy(matrix)
    del minor[i]
    for row in minor:
        del row[j]
    return minor

def get_inverse_key(key):
    determinant = laplas_diag_method(key)

    if determinant == 0:
        return None  # Invalid key, determinant is 0

    key_length = len(key)
    d = 1
    while ((d * determinant) % 27 != 1):
        d += 1
        
    if key_length == 2:
        adjugate_matrix = [[(key[1][1] * d) % 27, (-1 * key[0][1] * d) % 27],
                           [(-1 * key[1][0] * d) % 27, (key[0][0] * d) % 27]]
        return adjugate_matrix

    adjugate_matrix = [[0] * key_length for _ in range(key_length)]

    for i in range(key_length):
        for j in range(key_length):
            minor = get_minor_matrix(key, i, j)
            minor_determinant = laplas_diag_method(minor)
            cofactor = (-1) ** (i + j) * minor_determinant
            adjugate_matrix[j][i] = cofactor

    inverse_key = [[(adjugate_matrix[i][j] * d) % 27 for j in range(key_length)] for i in range(key_length)]

    return inverse_key
    

def hillcypher_decrypt(encoded_text, key):
    blocks = []
    dim = len(key)
    for i in range(int(len(encoded_text)/dim)):
        blocks.append([])
        for c in encoded_text[dim * i:dim * (i + 1)]:
            code = ord(c) - ord('A')
            if code <= 25:
                blocks[i].append(code)
            else:
                blocks[i].append(26)
    
    decoded_text = ""
    for i in range(len(blocks)):
        temp = [0] * dim
        for j in range(dim):
            for k in range(dim):
                temp[j] += blocks[i][k] * key[j][k]

        for n in temp:
            code = n % 27
            if code <= 25:
                decoded_text += chr(ord('A') + code)
            else:
                decoded_text += "_"
                
    return decoded_text

def is_valid_key(key):
    det = laplas_diag_method(key)
    return det != 0
  
if __name__ == "__main__":
    dim_num = int(input())
    matrix = []
    for i in range(dim_num):
        input_list = list(map(int , input().split()))
        matrix.append(input_list)
    
    text = input("")
    print(text)
    if is_valid_key(matrix):
        key = get_inverse_key(matrix)
        print(hillcypher_decrypt(text, key))
    else:
        print("NO_VALID_KEY")