number_range = 2, 5
write_style = ['w', 'wb']
descriptions = 'Shift each 8bit integer of the bytes array of plaintext by a random number in positive or negative direction first, then divide by a random integer (from the range between two integers), \
The division is converted from ASCII to characters as ciphertext, and the remainder of the array and the array of random integers is used as the key, which is faster and suitable for encrypting larger files'


# this is method 2, and this method is prepared for larger data to encrypt.
# the encrypting matrix in this method will be a string,
# and we will not calculating the inverse of the encrypting matrix
# in this method.
def encrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()

    text_length = len(text)
    if encrypt2_mode == 'string':
        text = [i + shift_num for i in text]
        shift_num = number_range[1]
        encrypt_ls = [
            random.randint(*number_range) for i in range(text_length)
        ]
        encrypt_str = ''.join([str(j) for j in encrypt_ls])
        encrypt_text = [text[i] // encrypt_ls[i] for i in range(text_length)]
        mod_str = ''.join(
            [str(text[i] % encrypt_ls[i]) for i in range(text_length)])
    elif encrypt2_mode == 'integer':
        text = [i for i in text]
        encrypt_str = random.randint(*number_range)
        encrypt_text = [text[i] // encrypt_str for i in range(text_length)]
        mod_str = ''.join(
            [str(text[i] % encrypt_str) for i in range(text_length)])
    with open(self.filenames[0], 'w', encoding='utf-8', errors='ignore') as f:
        f.write(str(tuple((encrypt_str, mod_str))))
    with open(self.filenames[1], 'wb') as f:
        f.write(bytes(encrypt_text))
    self.current_msg.configure(
        text=
        f'Encrypt successful,  the first file is key file, saved at {self.filenames[0]},'
        + '\n' +
        f'the second file is ciphertext file, saved at {self.filenames[1]}')
