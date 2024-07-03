def matrix_inverse(matrix):

    rows, cols = len(matrix), len(matrix[0])
    if rows != cols: 
        raise ValueError("Matrix is not square.")
    
    augmented_matrix = []
    for i in range(rows):
        augmented_matrix.append(matrix[i] + [int(i == j) for j in range(rows)])
    
    for i in range(rows):

        pivot_row = i
        while augmented_matrix[pivot_row][i] == 0:
            pivot_row += 1
            if pivot_row == rows:
                raise ValueError("Matrix is not invertible.")
        
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]
        
        pivot_element = augmented_matrix[i][i]
        augmented_matrix[i] = [elem / pivot_element for elem in augmented_matrix[i]]
        
        for j in range(rows):
            if j != i:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = [elem - factor * augmented_matrix[i][idx] for idx, elem in enumerate(augmented_matrix[j])]
    
    inverse = [row[cols:] for row in augmented_matrix]
    
    return inverse

def matrix_to_letter(matrix ):
    encrypted_string = ''
    for row in matrix:
        for num in row:
            encrypted_string += chr(int(num + float(97)))

    return encrypted_string

def encrypt(plaintext, key):
    word_list = plaintext.split(" ")
    encrypted_message = ''
    
    for word in word_list:
        length = len(word)
        if length % 2 != 0:
            word += 'a'
        else:
            pass
        
        encrypted_matrix = []
        for i in range(0, len(word), 2):
            l = []
            try:
                l += [ord(word[i]) - 97, ord(word[i + 1]) - 97]
            except:
                l += [ord(word[i]) - 97, 0]
            
            a = key[0][0] * l[0] + key[0][1] * l[1]
            b = key[1][0] * l[0] + key[1][1] * l[1]
            c = a % 26
            d = b % 26
            
            encrypted_matrix.append([c, d])
        
        encrypted_message += " " + matrix_to_letter(encrypted_matrix )
    
    return encrypted_message

def decrypt(ciphertext,key):
    word_list = ciphertext.split(" ")
    decrypted_message = ''

    for word  in word_list:
        length = len(word)
        decrypted_matrix = []
        
        for i in range(0, len(word), 2):
            l = []
            try:
                l += [ord(word[i]) - 97, ord(word[i + 1]) - 97]
            except:
                l += [ord(word[i]) - 97, 0]
            
            a = key[0][0] * l[0] + key[0][1] * l[1]
            b = key[1][0] * l[0] + key[1][1] * l[1]
            c = a % 26
            d = b % 26
            
            decrypted_matrix.append([c, d])

        decrypted_message += " " + matrix_to_letter(decrypted_matrix )[0:length]
    
    return decrypted_message

# key = [[1, 2], [1, 3]]

dim_num = int(input())
key = []
for i in range(dim_num):
    arr = list(map(float , input().split()))
    key.append(arr)

msg = input("")


# det = laplas_diag_method(matrix)
# key = [[9, 8], [10, 9]] 

encrypted_message = encrypt(msg, key)
print("Encrypted message:", encrypted_message)

key_inverse = matrix_inverse(key)
# key_inverse = [[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]

decrypted_message = decrypt(encrypted_message,key_inverse)


if len(decrypted_message.strip()) > len(msg.strip()) and decrypted_message[-1] == 'a':
    decrypted_message = decrypted_message[:-1]

print("Decrypted message:", decrypted_message)


