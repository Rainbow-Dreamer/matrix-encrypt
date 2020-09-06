descriptions = '计算密钥矩阵的逆(对角矩阵属于正交矩阵，其逆等于其转置)，然后用加密的文件的bytes数组的矩阵乘以密钥矩阵的逆，即可解密为原文件'
write_style = ['wb']
def decrypt(self):
    with open(self.choose_filename_path,
              encoding=decrypt_file_format,
              errors=errors_settings) as f:
        text = f.read()    
    mat_decrypt = self.filedialog.askopenfilename(initialdir='.', title='选择密钥文件',
                                            filetype=(("所有文件", "*.*"),))
    if mat_decrypt:
        with open(mat_decrypt, encoding='utf-8-sig') as f:
            data = f.read()
        if not (data[0] == '(' and data[-1] == ')'):
            self.current_msg.configure(text='密钥文件格式不正确')
            return
    diags, num, overflow = eval(data)
    text = [ord(i) for i in text]
    for g in range(num):
        current = diags[g]
        for h in range(num * g, num * (g + 1)):
            text[h] //= current
    decrypted_text = bytes(text[:-overflow])
    self.results = [decrypted_text]
    self.current_msg.configure(
        text = '解密成功，第一个文件是明文'
    )   
