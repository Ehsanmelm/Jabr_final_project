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


def decrypt_hillcipher(encrypted_message, key):
    key_length = len(key)
    decrypted_message = ""

    encrypted_blocks = encrypted_message.split()

    for block in encrypted_blocks:
        vector = [ord(c) - ord('A') if c != '_' else 26 for c in block]
        vector = [[val] for val in vector]

        inverse_key = get_inverse_key(key)  # Obtain the inverse of the key matrix

        decrypted_vector = [[sum(row[i] * vector[i][0] for i in range(key_length)) % 27] for row in inverse_key]

        decrypted_block = ''.join(chr(val[0] + ord('A')) if val[0] != 26 else '_' for val in decrypted_vector)
        decrypted_message += decrypted_block

    return decrypted_message.replace('_', ' ')


def get_inverse_key(key):
    determinant = GosJordan_diag(key)

    if determinant == 0:
        return None  # Invalid key, determinant is 0

    key_length = len(key)
    adjugate_matrix = [[0] * key_length for _ in range(key_length)]

    for i in range(key_length):
        for j in range(key_length):
            minor = get_minor_matrix(key, i, j)
            minor_determinant = GosJordan_diag(minor)
            cofactor = (-1) ** (i + j) * minor_determinant
            adjugate_matrix[j][i] = cofactor

    inverse_key = [[adjugate_matrix[i][j] / determinant % 27 for j in range(key_length)] for i in range(key_length)]

    return inverse_key


def get_minor_matrix(matrix, i, j):
    minor = deepcopy(matrix)
    del minor[i]
    for row in minor:
        del row[j]
    return minor


dim_num = int(input())
key = []
for i in range(dim_num):
    input_list = list(map(int, input().split()))
    key.append(input_list)

is_key_valid = True if GosJordan_diag(key) != 0 else False
message = input("")

if is_key_valid:
    encrypted_message = decrypt_hillcipher(message, key)
    print(encrypted_message.replace(' ', ''))
else:
    print("NO_VALID_KEY")