descriptions = 'The bytes stored in the key that previously changed the location of the bytes are changed back to their original values to decrypt them to the original file.'
write_style = ['wb']


def decrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    mat_decrypt = self.filedialog.askopenfilename(title='Choose key file',
                                                  filetypes=(("All files",
                                                              "*"), ))
    if mat_decrypt:
        with open(mat_decrypt, encoding='utf-8') as f:
            data = f.read()
        if not (data[0] == '[' and data[-1] == ']'):
            self.current_msg.configure(text='Incorrect key file format')
            return
    places = eval(data)
    text = [i for i in text]
    for each in places:
        text[each[0]] = each[1]
    with open(self.filenames[0], 'wb') as f:
        f.write(bytes(text))
    self.current_msg.configure(
        text=f'Decrypt successfully, saved at {self.filenames[0]}')
