
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


def encrypt_hillcipher(message, key):
    message = message.upper().replace(' ', '_')
    
    key_length = len(key)
    encrypted_message = ""

    if len(message) % key_length != 0:
        message += 'X' * (key_length - (len(message) % key_length))

    blocks = [message[i:i + key_length] for i in range(0, len(message), key_length)]

    for block in blocks:
        vector = [ord(c) - ord('A') if c != '_' else 26 for c in block]
        vector = [[val] for val in vector]

        encrypted_vector = [[sum(row[i] * vector[i][0] for i in range(key_length)) % 27] for row in key]

        encrypted_block = ''.join(chr(val[0] + ord('A')) if val[0] != 26 else '_' for val in encrypted_vector)
        encrypted_message += encrypted_block + ' '

    return encrypted_message.strip()


dim_num = int(input())
key = []
for i in range(dim_num):
    input_list = list(map(int , input().split()))
    key.append(input_list)

is_key_valid = True if GosJordan_diag(key) != 0 else False
message = input("")

if is_key_valid:

    encrypted_message = encrypt_hillcipher(message, key)
    print(encrypted_message.replace(' ' , ''))

else:
    print("NO_VALID_KEY")