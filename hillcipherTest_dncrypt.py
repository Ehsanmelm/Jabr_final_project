def decrypt_hillcipher(encrypted_message, key):
    key_size = len(key)
    key_inverse = get_matrix_inverse(key, 26)

    if key_inverse is None:
        print("The key is not invertible.")
        return ""

    decrypted_message = ""
    blocks = [encrypted_message[i:i + key_size] for i in range(0, len(encrypted_message), key_size)]

    for block in blocks:
        vector = [ord(c) - ord('A') for c in block]
        vector = [[val] for val in vector]

        decrypted_vector = matrix_multiply(key_inverse, vector, 26)

        decrypted_block = ''.join(chr(val[0] % 26 + ord('A')) for val in decrypted_vector)
        decrypted_message += decrypted_block

    return decrypted_message


def get_matrix_inverse(matrix, modulus):
    determinant = laplas_diag_method(matrix, modulus)
    multiplicative_inverse = find_multiplicative_inverse(determinant, modulus)

    if multiplicative_inverse is None:
        return None

    adjugate = get_matrix_adjugate(matrix)
    inverse = scalar_multiply(adjugate, multiplicative_inverse, modulus)

    return inverse

def laplas_diag_method(matrix , modulus):
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
        sub_det = laplas_diag_method(sub_matrix , modulus)
        det += sign * matrix[0][j] * sub_det

    return det % modulus


def find_multiplicative_inverse(num, modulus):
    for i in range(modulus):
        if (num * i) % modulus == 1:
            return i

    return None


def get_matrix_adjugate(matrix):
    size = len(matrix)
    adjugate = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            submatrix = [[matrix[row][col] for col in range(size) if col != j] for row in range(size) if row != i]
            adjugate[i][j] = ((-1) ** (i + j)) * laplas_diag_method(submatrix, 26)

    return adjugate


def scalar_multiply(matrix, scalar, modulus):
    return [[(val * scalar) % modulus for val in row] for row in matrix]


def matrix_multiply(matrix1, matrix2, modulus):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        return None

    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

            result[i][j] %= modulus

    return result


# Example usage
# message = "This is test hill cipher"
message = "HMSQSQBJEVXDHSYEDAMD"
key = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# encrypted_message = encrypt_hillcipher(message, key)
# print("Encrypted message:", encrypted_message)

decrypted_message = decrypt_hillcipher(message, key)
print("Decrypted message:", decrypted_message)