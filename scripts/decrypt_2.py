number_range = 2, 5
write_style = ['wb']
descriptions = 'Multiply each 8bit integer of the ciphertext byte array by the corresponding divisor, add the corresponding remainder, \
Then shift back to the random number when encrypted to get the bytes array of the original text, and write it to the new file in binary form to decrypt it to the original file'


def decrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    mat_decrypt = self.filedialog.askopenfilename(title='Choose key file',
                                                  filetypes=(("All files",
                                                              "*"), ))
    if mat_decrypt:
        with open(mat_decrypt, encoding='utf-8') as f:
            data = f.read()
        if not (data[0] == '(' and data[-1] == ')'):
            self.current_msg.configure(text='Incorrect key file format')
            return
        encrypt_str, mod_str = eval(data)
        mod_mat = [int(i) for i in mod_str]
        N = len(text)
        if decrypt2_mode == 'string':
            shift_num = number_range[1]
            encrypt_str = [int(i) for i in encrypt_str]
            decrypt_text = [
                text[j] * encrypt_str[j] + mod_mat[j] - shift_num
                for j in range(N)
            ]
        elif decrypt2_mode == 'integer':
            decrypt_text = [
                text[j] * encrypt_str + mod_mat[j] for j in range(N)
            ]
        with open(self.filenames[0], 'wb') as f:
            f.write(bytes(decrypt_text))
    self.current_msg.configure(
        text=f'Decrypt successfully, saved at {self.filenames[0]}')
