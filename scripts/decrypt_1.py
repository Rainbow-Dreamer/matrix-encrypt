write_style = ['w']
descriptions = 'The ASCII matrix of the ciphertext is multiplied by the inverse of the key matrix to obtain the ASCII matrix of the plaintext, which is then converted from ASCII to characters to decrypt the plaintext.'


def decrypt(self):
    mat_decrypt = self.filedialog.askopenfilename(title='Choose key file',
                                                  filetypes=(("All files",
                                                              "*"), ))
    if mat_decrypt:
        with open(mat_decrypt, encoding='utf-8') as f:
            data = f.read()
        if not (data[0] == '(' and data[-1] == ')'):
            self.current_msg.configure(text='Incorrect key file format')
            return
        mat_list, overflow = eval(data)
        mat_size = int(len(mat_list)**(1 / 2))
        length = mat_size**2
        mat_decrypt = form(mat_list, mat_size, mat_size)
        whole_file_size = os.path.getsize(self.choose_filename_path)
        convert_times = whole_file_size // length
        with open(self.choose_filename_path,
                  encoding=decrypt_file_format,
                  errors=errors_settings) as f, open(self.filenames[0],
                                                     'w',
                                                     encoding='utf-8',
                                                     errors='ignore') as file:
            for i in range(convert_times):
                text = f.read(length)
                if not text:
                    if overflow != 0:
                        file.seek(file.tell() - overflow, os.SEEK_SET)
                        file.truncate()
                    self.current_msg.configure(text='decrypt progress: 100 %')
                    self.current_msg.update()
                    break
                current = decrypt2(text, mat_decrypt, mat_size)
                file.write(current)
                self.current_msg.configure(
                    text=
                    f'decrypt progress: {round(((i+1)/convert_times)*100, 3)} %'
                )
                self.current_msg.update()
    self.current_msg.configure(
        text=f'Decrypt successfully, saved at {self.filenames[0]}')


def decrypt2(text, mat, sizes):
    text_list = [ord(i) for i in text]
    text_mat = form(text_list, sizes, sizes)
    decrypt_mat = (text_mat * mat.inv_lu()).formated()
    decrypt_mat_element = decrypt_mat.element()
    return ''.join([chr(x) for x in decrypt_mat_element])