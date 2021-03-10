write_style = ['wb']
descriptions = '输入的密码转换成ASCII码对密文的字符对应的ASCII码进行从第一个到最后一个的循环的负方向的移位，即可解密为原文件。'


def decrypt(self):
    self.password_enter = ttk.Label(self, text='请输入密码')
    self.password_enter_show = ttk.Entry(self)
    self.current_encrypt_button = ttk.Button(self,
                                             text='开始解密',
                                             command=lambda: decrypt2(self))
    self.password_enter.place(x=200, y=350)
    self.password_enter_show.place(x=200, y=380)
    self.current_encrypt_button.place(x=200, y=450)


def decrypt2(self):
    password = self.password_enter_show.get()
    if not password:
        self.current_msg.configure(text='请输入密码')
        return
    N = len(password)
    password_list = [ord(i) for i in password]
    counter = 0
    with open(self.filenames[0], 'wb') as file:
        with open(self.choose_filename_path,
                  encoding='utf-8-sig',
                  errors='ignore') as f:
            for line in f:
                current_len = len(line)
                file.write(
                    bytes([
                        ord(line[j - counter]) - password_list[j % N]
                        for j in range(counter, counter + current_len)
                    ]))
                counter += current_len
    self.current_msg.configure(text=f'解密成功，已保存在{self.filenames[0]}')
    self.password_enter.destroy()
    self.password_enter_show.destroy()
    self.current_encrypt_button.destroy()