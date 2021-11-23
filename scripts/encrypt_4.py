write_style = ['w', 'wb']
descriptions = 'Using the square root of the bytes array of the file to be encrypted as the dimension to generate a random permutation matrix, \
Multiply the replacement matrix left by the matrix of the bytes array of the file to be encrypted to get the bytes array of the file to be encrypted \
The new array is obtained by swapping the random horizontal rows of the matrix of the file to be encrypted, and the key is the random permutation matrix.'


# this is actually the third method that I came out in this series,
# this method is producing a permutation matrix to change the orders
# of the rows or columns of the matrix that fills the data of the file
# you want to encrypt.
def perm_row(length, ind):
    result = [0 for i in range(length)]
    result[ind] = 1
    return result


def perm(size):
    result = build(size)
    ls = list(range(size))
    inds = []
    while ls:
        current = random.randint(0, len(ls) - 1)
        inds.append(ls.pop(current))
    [result.rprow(i, perm_row(size, inds[i])) for i in range(size)]
    return result


def encrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    text = [i for i in text]
    text_length = len(text)
    num = math.ceil(text_length**0.5)
    sizes = [num, num]
    text_mat = build(*sizes)
    text_mat.fillin(text)
    perm_mat = perm(num)
    encrypt_mat = np.array(perm_mat.row) @ np.array(text_mat.row)
    encrypt_text = matrix(encrypt_mat.tolist()).element()
    bin_str = ''.join([str(i) for i in perm_mat.element()])
    encrypt_num = int(bin_str, 2)
    pre_zeros = len(bin_str) - len(bin(encrypt_num)) + 2
    with open(self.filenames[0], 'w', encoding='utf-8-sig',
              errors='ignore') as f:
        f.write(str(tuple((encrypt_num, pre_zeros, num))))
    with open(self.filenames[1], 'wb') as f:
        f.write(bytes(encrypt_text))
    self.current_msg.configure(
        text=
        f'Encrypt successful,  the first file is key file, saved at {self.filenames[0]},'
        + '\n' +
        f'the second file is ciphertext file, saved at {self.filenames[1]}')