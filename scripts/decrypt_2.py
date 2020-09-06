number_range = 2, 5
write_style = ['wb']
descriptions = '把密文的bytes数组每个8bit整数乘上对应的被除数，再加上对应的余数，\
然后再移位回加密时的随机数即可得到原文的bytes数组，以二进制形式写入新文件即可解密为原文件'
def decrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    mat_decrypt = self.filedialog.askopenfilename(initialdir='.', title='选择密钥文件',
                                             filetype=(("所有文件", "*.*"),))
    if mat_decrypt:
        with open(mat_decrypt, encoding='utf-8-sig') as f:
            data = f.read()
        if not (data[0] == '(' and data[-1] == ')'):
            self.current_msg.configure(text='密钥文件格式不正确')
            return
        encrypt_str, mod_str = eval(data)
        mod_mat = [int(i) for i in mod_str]
        N = len(text)
        if decrypt2_mode == 'string':
            shift_num = number_range[1]
            encrypt_str = [int(i) for i in encrypt_str]
            decrypt_text = [
                text[j] * encrypt_str[j] + mod_mat[j] - shift_num for j in range(N)
            ]
        elif decrypt2_mode == 'integer':
            decrypt_text = [text[j] * encrypt_str + mod_mat[j] for j in range(N)]
        self.results = [bytes(decrypt_text)]
        self.current_msg.configure(
        text = '解密成功，第一个文件是明文'
    )   
