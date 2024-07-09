import sys
from copy import deepcopy
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit 
from PyQt5.QtGui import QFont
import numpy as np

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
        return None  

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
    

class EncryptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Encryption App")
        self.setGeometry(300, 300, 500, 300)

        self.inputtext_textedit = QTextEdit()
        self.encrypted_textedit = QTextEdit()
        self.decrypt_textedit = QTextEdit()

        self.inputtext_textedit.setFixedSize(150,150)
        self.encrypted_textedit.setFixedSize(150,150)
        self.decrypt_textedit.setFixedSize(150,150)

        self.inputtext_textedit.setFont(QFont('Arial', 15))
        self.encrypted_textedit.setFont(QFont('Arial', 15))
        self.decrypt_textedit.setFont(QFont('Arial', 15))

        self.inputtext_textedit.setStyleSheet("border: 2px solid black;")
        self.encrypted_textedit.setStyleSheet("border: 2px solid black;")
        self.decrypt_textedit.setStyleSheet("border: 2px solid black;")

        self.decrypt_textedit.hide()  

        self.encrypt_button = QPushButton("Encrypt", self)
        self.decrypt_button = QPushButton("Decrypt", self)

        self.setup_ui()

    def setup_ui(self):
        input_label = QLabel("inputtext:")
        encrypted_label = QLabel("Encrypted:")
        decrypt_label = QLabel("Decrypted:")
        
        input_label.setFont(QFont('Arial', 15))
        encrypted_label.setFont(QFont('Arial', 15))
        decrypt_label.setFont(QFont('Arial', 15))


        input_label.setStyleSheet("font-weight: bold " )
        encrypted_label.setStyleSheet("font-weight: bold;")
        decrypt_label.setStyleSheet("font-weight: bold;")

        layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        form_layout.addWidget(input_label)
        form_layout.addWidget(self.inputtext_textedit)
        form_layout.addWidget(encrypted_label)
        form_layout.addWidget(self.encrypted_textedit)
        form_layout.addWidget(decrypt_label)
        form_layout.addWidget(self.decrypt_textedit)

        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)

        layout.addLayout(form_layout)
        layout.addLayout(button_layout)


        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(30)

        self.setLayout(layout)

        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)

        self.setStyleSheet("background-color: gray;")


    def encrypt(self):

        message = self.inputtext_textedit.toPlainText()
        key = [[6,24,1],[13,16,8],[10,2,1]]

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

        self.encrypted_textedit.setPlainText(encrypted_message.strip().replace(" " , ''))

        

    def decrypt(self, key):
        encoded_text = self.encrypted_textedit.toPlainText().replace(' ', '')

        key = [[6,24,1],[13,16,8],[10,2,1]]
        key = get_inverse_key(key)

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
                        
        self.decrypt_textedit.show() 
        self.decrypt_textedit.setPlainText(decoded_text.strip())




if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle("Fusion")

    window = EncryptionApp()
    window.show()
    sys.exit(app.exec_())