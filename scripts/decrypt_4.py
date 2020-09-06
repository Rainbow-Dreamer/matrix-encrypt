descriptions = '以二进制形式读取文件，得到其bytes的数组，将密钥矩阵的逆乘以bytes的数组的矩阵即可解密为原文件。'
write_style = ['wb']
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
    self.results = [bytes(decrypt_text)]
    self.current_msg.configure(
        text = '加密成功，第一个文件是密文'
    )    
    