import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit 
from PyQt5.QtGui import QFont
from key_creator import key_matrix_creator
import numpy as np


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

    def matrix_to_letter(self, matrix):
        encrypted_string = ''
        for row in matrix:
            for num in row:
                encrypted_string += chr(num + 97)
        return encrypted_string

    def encrypt(self):
        inputtext = self.inputtext_textedit.toPlainText()

        # key = np.array([[1, 2], [1, 3]])
        key = np.array([[9, 8], [10, 9]])

        word_list = inputtext.split(" ")
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
                c = np.matmul(key, l)
                encrypted_matrix.append(c % 26)

            encrypted_message += " " + self.matrix_to_letter(encrypted_matrix)

        self.encrypted_textedit.setPlainText(encrypted_message.strip())

    def decrypt(self):
        encrypted_text = self.encrypted_textedit.toPlainText()
        # key = np.array([[1, 2], [1, 3]])
        key = np.array([[9, 8], [10, 9]])

        # key = np.array([[9, 8], [7, 7]])

        
        key = np.linalg.inv(key).astype(int)

        word_list = encrypted_text.split(" ")
        decrypted_message = ''

        for word in word_list:
            length = len(word)
            decrypted_matrix = []
            for i in range(0, len(word), 2):
                l = []
                try:
                    l += [ord(word[i]) - 97, ord(word[i + 1]) - 97]
                except:
                    l += [ord(word[i]) - 97, 0]
                c = np.matmul(key, l)
                decrypted_matrix.append(c % 26)

            decrypted_message += " " + self.matrix_to_letter(decrypted_matrix)[0:length]
            print(self.inputtext_textedit.toPlainText())
            if len(decrypted_message) > len(self.inputtext_textedit.toPlainText()) and decrypted_message[-1] == 'a':
                decrypted_message = decrypted_message[ : -1]


        self.decrypt_textedit.show() 
        self.decrypt_textedit.setPlainText(decrypted_message.strip())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle("Fusion")

    window = EncryptionApp()
    window.show()
    sys.exit(app.exec_())