# this method will use a password to encode the file,
# the password could be any combinations of any characters as long as you can type.
write_style = ['w']
descriptions = '以二进制形式读取要加密的文件，得到其bytes的数组。设定的密码转换成ASCII码的列表，\
然后从第一个到最后一个循环对每一个bytes进行正方向的移位。移位之后的bytes数组按照ASCII码转换成字符，\
以文本文件的格式形成密文。'

def encrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()    
    self.password_enter = ttk.Label(self, text='请输入想设置的密码')
    self.password_enter_show = ttk.Entry(self)
    self.current_encrypt_button = ttk.Button(self, text='开始加密', command=lambda: encrypt2(self, text))
    self.password_enter.place(x=200, y=350)
    self.password_enter_show.place(x=200, y=380)
    self.current_encrypt_button.place(x=200, y=450)
    
def encrypt2(self, text):
    password = self.password_enter_show.get()
    if not password:
        self.current_msg.configure(
        text = '请输入密码'
    )    
        return
    N = len(password)
    text_len = len(text)
    password_list = [ord(i) for i in password]
    result = [chr(text[j] + password_list[j % N]) for j in range(text_len)]
    encrypted_text =  ''.join(result)
    self.results = [encrypted_text]
    self.current_msg.configure(
        text = '加密成功，第一个文件是密文'
    )    
    self.password_enter.destroy()
    self.password_enter_show.destroy()
    self.current_encrypt_button.destroy()