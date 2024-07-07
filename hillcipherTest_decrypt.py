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

# def decrypt_hillcipher(encrypted_message, key):
#     key_length = len(key)
#     decrypted_message = ""

#     inv_key = get_inverse_key(key)
#     if inv_key is None:
#         return "NO_VALID_KEY"

#     blocks = encrypted_message.split()
#     for block in blocks:
#         vector = [ord(c) - ord('A') if c != '_' else 26 for c in block]

#         decrypted_vector = [[sum(row[i] * vector[i] for i in range(key_length)) % 27] for row in inv_key]

#         decrypted_block = ''.join(chr(int(val[0] + ord('A'))) if val[0] != 26 else '_' for val in decrypted_vector)
#         decrypted_message += decrypted_block

#     return decrypted_message.replace('_', ' ')

# def get_inverse_key(key):
#     determinant = GosJordan_diag(key)
#     if determinant == 0:
#         return None

#     dim_num = len(key)
#     adjugate = [[] for _ in range(dim_num)]

#     for i in range(dim_num):
#         for j in range(dim_num):
#             minor = [[key[m][n] for n in range(dim_num) if n != j] for m in range(dim_num) if m != i]
#             adjugate[j].append((-1) ** (i + j) * GosJordan_diag(minor))

#     inverse_key = [[adjugate[j][i] / determinant for j in range(dim_num)] for i in range(dim_num)]
#     return inverse_key



import numpy as np

def decrypt_hillcipher(encrypted_message, key):
    key_length = len(key)
    decrypted_message = ""

    inv_key = np.linalg.inv(key)
    inv_key = np.round(inv_key * np.linalg.det(key)).astype(int) % 27

    blocks = encrypted_message.split()
    for block in blocks:
        vector = [ord(c) - ord('A') if c != '_' else 26 for c in block]

        decrypted_vector = np.dot(inv_key, vector) % 27

        decrypted_block = ''.join(chr(val + ord('A')) if val != 26 else '_' for val in decrypted_vector)
        decrypted_message += decrypted_block

    return decrypted_message.replace('_', ' ')
# dim_num = int(input())
# key = []
# for i in range(dim_num):
#     input_list = list(map(int, input().split()))
#     key.append(input_list)

# is_key_valid = True if GosJordan_diag(key) != 0 else False
# message = input("")

# if is_key_valid:
#     encrypted_message = decrypt_hillcipher(message, key)
#     print(encrypted_message.replace(' ', ''))
# else:
#     print("NO_VALID_KEY")

dim_num = int(input())
key = []
for i in range(dim_num):
    input_list = list(map(int, input().split()))
    key.append(input_list)

is_key_valid = True if GosJordan_diag(key) != 0 else False
message = input("")

if is_key_valid:
    # encrypted_message = encrypt_hillcipher(message, key)
    # print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt_hillcipher(message, key)
    # decrypted_message = 'OGOSXRBFSJMXQWSAJAX_NECS'
    print("Decrypted message:", decrypted_message)

else:
    print("NO_VALID_KEY")