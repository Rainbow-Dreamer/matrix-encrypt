write_style = ['w']
descriptions = '以密文的ASCII码矩阵乘上密钥矩阵的逆即可得到明文的ASCII码矩阵，再从ASCII码转换成字符即可解密为明文。'


def decrypt(self):
    with open(self.choose_filename_path,
              encoding=decrypt_file_format,
              errors=errors_settings) as f:
        text = f.read()
    mat_decrypt = self.filedialog.askopenfilename(initialdir='.',
                                                  title='选择密钥文件',
                                                  filetype=(("所有文件", "*.*"), ))
    if mat_decrypt:
        with open(mat_decrypt, encoding='utf-8-sig') as f:
            data = f.read()
        if not (data[0] == '(' and data[-1] == ')'):
            self.current_msg.configure(text='密钥文件格式不正确')
            return
        mat_list, mat_size_num, overflow = eval(data)
        mat_size = [mat_size_num, mat_size_num]
        mat_decrypt = form(mat_list, *mat_size)
        decrypted_text = decrypt2(text, mat_decrypt, mat_size)
        if overflow != 0:
            decrypted_text = decrypted_text[:-overflow]
        with open(self.filenames[0],
                  'w',
                  encoding='utf-8-sig',
                  errors='ignore') as f:
            f.write(decrypted_text)
    self.current_msg.configure(text=f'解密成功，已保存在{self.filenames[0]}')


def decrypt2(text, mat, sizes):
    text_list = [ord(i) for i in text]
    text_mat = form(text_list, *sizes)
    decrypt_mat = (text_mat * mat.inv_lu()).formated()
    decrypt_mat_element = decrypt_mat.element()
    return ''.join([chr(x) for x in decrypt_mat_element])