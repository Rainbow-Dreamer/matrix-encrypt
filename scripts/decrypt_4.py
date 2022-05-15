descriptions = 'Read the file in binary form, get its array of bytes, and decrypt the original file by multiplying the inverse of the key matrix by the matrix of the array of bytes.'
write_style = ['wb']


def decrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    mat_decrypt = self.filedialog.askopenfilename(title='Choose key file',
                                                  filetype=(("All files",
                                                             "*.*"), ))
    if mat_decrypt:
        with open(mat_decrypt, encoding='utf-8-sig') as f:
            data = f.read()
        if not (data[0] == '(' and data[-1] == ')'):
            self.current_msg.configure(text='Incorrect key file format')
            return
    perm_num, pre_zeros, num = eval(data)
    text = [i for i in text]
    text_mat = build(num, num)
    text_mat.fillin(text)
    perm_mat = build(num, num)
    perm_str = '0' * pre_zeros + bin(perm_num)[2:]
    perm_ls = [int(i) for i in perm_str]
    perm_mat.fillin(perm_ls)
    decrypt_mat = np.array(perm_mat.T().row) @ np.array(text_mat.row)
    decrypt_text = matrix(decrypt_mat.tolist()).element()
    with open(self.filenames[0], 'wb') as f:
        f.write(bytes(decrypt_text))
    self.current_msg.configure(
        text=f'Decrypt successfully, saved at {self.filenames[0]}')
