# this method will use a password to encode the file,
# the password could be any combinations of any characters as long as you can type.
write_style = ['w']
descriptions = 'Read the file to be encrypted in binary form and get an array of its bytes. The set password is converted into a list of ASCII codes, \
Then each bytes is shifted in positive direction from the first to the last loop. The array of bytes after shifting is converted into characters according to ASCII codes,\
to form a ciphertext in the format of a text file.'


def encrypt(self):
    self.password_enter = ttk.Label(self, text='Please enter password')
    self.password_enter_show = ttk.Entry(self)
    self.current_encrypt_button = ttk.Button(self,
                                             text='Start encrypting',
                                             command=lambda: encrypt2(self))
    self.password_enter.place(x=200, y=350)
    self.password_enter_show.place(x=200, y=380)
    self.current_encrypt_button.place(x=200, y=450)


def encrypt2(self):
    password = self.password_enter_show.get()
    if not password:
        self.current_msg.configure(text='Please enter password')
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
    self.current_msg.configure(
        text=
        f'Encrypt successful,  the first file is ciphertext file, saved at {self.filenames[0]}'
    )
    self.password_enter.destroy()
    self.password_enter_show.destroy()
    self.current_encrypt_button.destroy()