descriptions = '将密钥里存储的之前改变bytes的位置的bytes改变回原值，即可解密为原文件。'
write_style = ['wb']


def decrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    mat_decrypt = self.filedialog.askopenfilename(initialdir='.',
                                                  title='选择密钥文件',
                                                  filetype=(("所有文件", "*.*"), ))
    if mat_decrypt:
        with open(mat_decrypt, encoding='utf-8-sig') as f:
            data = f.read()
        if not (data[0] == '[' and data[-1] == ']'):
            self.current_msg.configure(text='密钥文件格式不正确')
            return
    places = eval(data)
    text = [i for i in text]
    for each in places:
        text[each[0]] = each[1]
    with open(self.filenames[0], 'wb') as f:
        f.write(bytes(text))
    self.current_msg.configure(text=f'解密成功，已保存在{self.filenames[0]}')