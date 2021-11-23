descriptions = 'Using an orthogonal matrix to encrypt the file, in this case a diagonal matrix, the details of encryption are similar to the first encryption algorithm, \
The advantage of using diagonal matrix encryption is that when decrypting the key matrix, only the transpose of the matrix needs to be calculated when calculating the \
inverse of the key matrix (because one of the properties of an orthogonal matrix is that (because one of the properties of an orthogonal matrix is that its inverse is \
equal to its transpose), thus greatly speeding up the decryption process (the computation of the inverse of a large matrix often requires much more arithmetic power than the computation of its transpose).\
is more suitable for encryption and decryption of large files. Another difference with the first encryption algorithm is that the encrypted object here is an array of bytes of the file.'

write_style = ['w', 'w']
number_range = 2, 3
# considering that method 1 is very slow for encrypting and decrypting
# relatively large file (even for long plain text), and the main reason
# of that is you need to calculate the inverse of the encrpyt matrix when you
# decrypt the file, so in this method 5, we are using the orthogonal matrix,
# which inverse is its transpose (the transpose of a matrix is very easy
# to calculate and fast), and diagonal matrix for encrypting is also good
# for consideration.


def encrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    text = [i for i in text]
    text_length = len(text)
    num = math.ceil(text_length**0.5)
    overflow = num**2 - text_length
    diags = [random.randint(*number_range) for j in range(num)]
    text += [0] * overflow
    for g in range(num):
        current = diags[g]
        for h in range(num * g, num * (g + 1)):
            text[h] *= current
    encrypted_text = ''.join([chr(i) for i in text])
    with open(self.filenames[0], 'w', encoding='utf-8-sig',
              errors='ignore') as f:
        f.write(str((diags, num, overflow)))
    with open(self.filenames[1], 'w', encoding='utf-8-sig',
              errors='ignore') as f:
        f.write(encrypted_text)
    self.current_msg.configure(
        text=
        f'Encrypt successful,  the first file is key file, saved at {self.filenames[0]},'
        + '\n' +
        f'the second file is ciphertext file, saved at {self.filenames[1]}')
