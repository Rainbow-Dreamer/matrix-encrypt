write_style = ['w', 'w']
descriptions = 'Take the downward rounded square root of the total number of characters of the file to be encrypted as the dimension (number of rows and columns), \
generate a square matrix where each element of the square matrix is a random number picked from the range between two integers. \
It is necessary to ensure that the determinant of this random number matrix is not zero, i.e., it is guaranteed to be invertible. Translate all the characters of the file to be encrypted into \
ASCII code and then load it into a square matrix of the same size, then multiply the ASCII code matrix of the encrypted file by the random number matrix to get the \
The new matrix is then translated from ASCII back to characters, and then all elements of the new matrix are taken out as ciphertext. The random number matrix needs to be saved as a key as well.'


def encrypt(self):
    size = [encrypt1_matrix_size, encrypt1_matrix_size]
    length = encrypt1_matrix_size**2
    encrypt_mat = build(*size)
    encrypt_mat.fillin([random.randint(*number_range) for i in range(length)])
    while encrypt_mat.det() == 0:
        encrypt_mat.fillin(
            [random.randint(*number_range) for i in range(length)])
    whole_file_size = os.path.getsize(self.choose_filename_path)
    convert_times, remain_size = divmod(whole_file_size, length)
    with open(self.choose_filename_path,
              encoding=encrypt_file_format,
              errors=errors_settings) as f, open(self.filenames[1],
                                                 'w',
                                                 encoding='utf-8',
                                                 errors='ignore') as file:
        for i in range(convert_times):
            text = f.read(length)
            if not text:
                overflow = length - current_text_length
                self.current_msg.configure(text='encrypt progress: 100 %')
                self.current_msg.update()
                break
            current_text_length = len(text)
            file.write(encrypt2(text, encrypt_mat, size))
            self.current_msg.configure(
                text=
                f'encrypt progress: {round(((i+1)/convert_times)*100, 3)} %')
            self.current_msg.update()
    with open(self.filenames[0], 'w', encoding='utf-8', errors='ignore') as f:
        f.write(str((encrypt_mat.element(), overflow)))
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
