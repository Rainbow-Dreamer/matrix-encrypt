write_style = ['w', 'w']
descriptions = 'Take the downward rounded square root of the total number of characters of the file to be encrypted as the dimension (number of rows and columns), \
generate a square matrix where each element of the square matrix is a random number picked from the range between two integers. \
It is necessary to ensure that the determinant of this random number matrix is not zero, i.e., it is guaranteed to be invertible. Translate all the characters of the file to be encrypted into \
ASCII code and then load it into a square matrix of the same size, then multiply the ASCII code matrix of the encrypted file by the random number matrix to get the \
The new matrix is then translated from ASCII back to characters, and then all elements of the new matrix are taken out as ciphertext. The random number matrix needs to be saved as a key as well.'


def encrypt(self):
    with open(self.choose_filename_path,
              encoding=encrypt_file_format,
              errors=errors_settings) as f:
        text = f.read()
    text_length = len(text)
    num = math.ceil(text_length**0.5)
    overflow = num**2 - text_length
    size = [num, num]
    length = size[0] * size[1]
    encrypt_mat = build(*size)
    encrypt_mat.fillin([random.randint(*number_range) for i in range(length)])
    while encrypt_mat.det() == 0:
        encrypt_mat.fillin(
            [random.randint(*number_range) for i in range(length)])
    while True:
        try:
            encrypted_text = encrypt2(text, encrypt_mat, size)
            break
        except:
            continue
    with open(self.filenames[0], 'w', encoding='utf-8-sig',
              errors='ignore') as f:
        f.write(str((encrypt_mat.element(), num, overflow)))
    with open(self.filenames[1], 'w', encoding='utf-8-sig',
              errors='ignore') as f:
        f.write(encrypted_text)
    self.current_msg.configure(
        text=
        f'Encrypt successful,  the first file is key file, saved at {self.filenames[0]},'
        + '\n' +
        f'the second file is ciphertext file, saved at {self.filenames[1]}')


def encrypt2(text, mat, sizes):
    text_num = [ord(i) for i in text]
    text_mat = form(text_num, *sizes)
    new_mat = text_mat * mat
    new_mat_element = new_mat.element()
    return ''.join([chr(j) for j in new_mat_element])
