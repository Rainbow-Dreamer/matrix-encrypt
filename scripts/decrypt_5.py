descriptions = 'Calculate the inverse of the key matrix (the diagonal matrix is an orthogonal matrix and its inverse is equal to its transpose), then multiply the matrix of the bytes array of the encrypted file by the inverse of the key matrix to decrypt it to the original file'
write_style = ['wb']


def decrypt(self):
    with open(self.choose_filename_path,
              encoding=decrypt_file_format,
              errors=errors_settings) as f:
        text = f.read()
    mat_decrypt = self.filedialog.askopenfilename(title='Choose key file',
                                                  filetypes=(("All files",
                                                              "*"), ))
    if mat_decrypt:
        with open(mat_decrypt, encoding='utf-8') as f:
            data = f.read()
        if not (data[0] == '(' and data[-1] == ')'):
            self.current_msg.configure(text='Incorrect key file format')
            return
    diags, num, overflow = eval(data)
    text = [ord(i) for i in text]
    for g in range(num):
        current = diags[g]
        for h in range(num * g, num * (g + 1)):
            text[h] //= current
    decrypted_text = bytes(text[:len(text) - overflow])
    with open(self.filenames[0], 'wb') as f:
        f.write(decrypted_text)
    self.current_msg.configure(
        text=f'Decrypt successfully, saved at {self.filenames[0]}')
