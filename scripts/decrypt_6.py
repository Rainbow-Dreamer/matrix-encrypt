descriptions = 'Read the file in binary form, get an array of its bytes, fit the array into a square matrix with the dimension of the number of bytes of the file rounded down to the square root, \
Transpose the matrix, remove all elements as a new bytes array, and subtract the bits overflowed from the previous matrix to decrypt it to the original file.'

write_style = ['wb']


def decrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    text = [i for i in text]
    text_length = len(text)
    num = math.ceil(text_length**0.5)
    text_new = []
    for j in range(num):
        for k in range(num):
            current = j + num * k
            text_new.append(text[current])
    last_byte = text_new[-1]
    for i in range(text_length - 1, -1, -1):
        if text_new[i] != last_byte:
            overflow_ind = i - (text_length - 1)
            break
    text_new = text_new[:overflow_ind]
    with open(self.filenames[0], 'wb') as f:
        f.write(bytes(text_new))
    self.current_msg.configure(
        text=f'Decrypt successfully, saved at {self.filenames[0]}')
