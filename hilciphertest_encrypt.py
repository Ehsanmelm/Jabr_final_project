
def encrypt_hillcipher(message, key):
    message = message.upper().replace(' ', '') 
    key_length = len(key)  
    encrypted_message = ""

    if len(message) % key_length != 0:
        message += 'X' * (key_length - (len(message) % key_length))

    blocks = [message[i:i + key_length] for i in range(0, len(message), key_length)]

    for block in blocks:
        vector = [ord(c) - ord('A') for c in block]  
        vector = [[val] for val in vector] 

        encrypted_vector = [[sum(row[i] * vector[i][0] for i in range(key_length)) % 26] for row in key]

        encrypted_block = ''.join(chr(val[0] % 26 + ord('A')) for val in encrypted_vector)
        encrypted_message += encrypted_block

    return encrypted_message

message = "This is test hill cypher"
key = [[1, 2], [3, 1]]
encrypted_message = encrypt_hillcipher(message, key)
print("Encrypted message:", encrypted_message)