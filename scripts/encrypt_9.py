# this method will use a password to encode the file,
# the password could be any combinations of any characters as long as you can type.
write_style = ['w']
descriptions = '以二进制形式读取要加密的文件，得到其bytes的数组。设定的密码转换成ASCII码的列表，\
然后从第一个到最后一个循环对每一个bytes进行正方向的移位。移位之后的bytes数组按照ASCII码转换成字符，\
以文本文件的格式形成密文。'


def encrypt(self):
    self.password_enter = ttk.Label(self, text='请输入想设置的密码')
    self.password_enter_show = ttk.Entry(self)
    self.current_encrypt_button = ttk.Button(self,
                                             text='开始加密',
                                             command=lambda: encrypt2(self))
    self.password_enter.place(x=200, y=350)
    self.password_enter_show.place(x=200, y=380)
    self.current_encrypt_button.place(x=200, y=450)


def encrypt2(self):
    password = self.password_enter_show.get()
    if not password:
        self.current_msg.configure(text='请输入密码')
        return
    N = len(password)
    password_list = [ord(i) for i in password]
    counter = 0
    with open(self.filenames[0], 'w', encoding='utf-8-sig',
              errors='ignore') as file:
        with open(self.choose_filename_path, 'rb') as f:
            for line in f:
                current_len = len(line)
                file.write(''.join([
                    chr(line[j - counter] + password_list[j % N])
                    for j in range(counter, counter + current_len)
                ]))
                counter += current_len
    self.current_msg.configure(text=f'加密成功，第一个文件是密文，已保存在{self.filenames[0]}')
    self.password_enter.destroy()
    self.password_enter_show.destroy()
    self.current_encrypt_button.destroy()