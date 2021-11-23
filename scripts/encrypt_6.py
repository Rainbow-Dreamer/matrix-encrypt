# this method is to fill the data bytes of the file into a matrix,
# and calculate the transpose of the matrix, and then fill in data bytes
# of the transposed matrix to the encrypted file.
# (This method mainly applies for all of the files excepts plain text files)
descriptions = 'Read the file in binary form, get an array of its bytes, load the array into a square matrix with the dimension of the number of bytes of the file rounded down to the square root, \
Transpose the matrix, remove all elements as the array of bytes of the ciphertext, and write to a new file to get the encrypted file.'

write_style = ['wb']


def encrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    text = [i for i in text]
    text_length = len(text)
    num = math.ceil(text_length**0.5)
    overflow = num**2 - text_length
    last_byte = text[-1]
    overflow_byte = random.choice([i for i in range(255) if i != last_byte])
    text += [overflow_byte] * overflow
    text_new = []
    for j in range(num):
        for k in range(num):
            current = j + num * k
            text_new.append(text[current])
    with open(self.filenames[0], 'wb') as f:
        f.write(bytes(text_new))
    self.current_msg.configure(
        text=
        f'Encrypt successful,  the first file is ciphertext file, saved at {self.filenames[0]}'
    )
