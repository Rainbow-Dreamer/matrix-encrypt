write_style = ['wb']
descriptions = 'The entered password is converted to ASCII code by shifting the ASCII code of the cipher text from the first to the last character in a circular negative direction to decrypt the original file.'


def decrypt(self):
    self.password_enter = ttk.Label(self, text='Please enter password')
    self.password_enter_show = ttk.Entry(self)
    self.current_encrypt_button = ttk.Button(self,
                                             text='Start decrypting',
                                             command=lambda: decrypt2(self))
    self.password_enter.place(x=200, y=350)
    self.password_enter_show.place(x=200, y=380)
    self.current_encrypt_button.place(x=200, y=450)


def decrypt2(self):
    password = self.password_enter_show.get()
    if not password:
        self.current_msg.configure(text='Please enter password')
        return
    N = len(password)
    password_list = [ord(i) for i in password]
    counter = 0
    with open(self.filenames[0], 'wb') as file:
        with open(self.choose_filename_path, encoding='utf-8',
                  errors='ignore') as f:
            for line in f:
                current_len = len(line)
                file.write(
                    bytes([
                        ord(line[j - counter]) - password_list[j % N]
                        for j in range(counter, counter + current_len)
                    ]))
                counter += current_len
    self.current_msg.configure(
        text=f'Decrypt successfully, saved at {self.filenames[0]}')
    self.password_enter.destroy()
    self.password_enter_show.destroy()
    self.current_encrypt_button.destroy()