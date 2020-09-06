write_style = ['w', 'wb']
descriptions = '以要加密的文件的bytes数组的向下取整平方根为维度生成一个随机的置换矩阵，\
将置换矩阵左乘以要加密的文件的bytes数组的矩阵，即可得到要加密的文件的bytes数组\
的矩阵的随机横行交换过后得到的新的数组，即可得到密文，密钥为随机的置换矩阵。'

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
    self.results = [str(tuple((encrypt_num, pre_zeros, num))), bytes(encrypt_text)]
    self.current_msg.configure(
        text = '加密成功，第一个文件是密钥文件，第二个文件是密文'
    )    
