write_style = ['w', 'w']
descriptions = '以要加密的文件的总字符数量的向下取整平方根作为维数（行数和列数）\
生成一个方块矩阵，方块矩阵里的每个元素都是从两个整数之间的范围里挑选的随机数。\
需要确保这个随机数矩阵的行列式不为0，也就是保证可逆。把要加密的文件的字符全部翻译成\
ASCII码然后装入一个同样大小的方块矩阵，然后将加密文件的ASCII码矩阵乘以随机数矩阵，得到的\
新矩阵再从ASCII码翻译回字符，然后把新矩阵的所有元素取出来作为密文。随机数矩阵作为密钥也需要保存起来。'


def encrypt(self):
    with open(self.choose_filename_path,
              encoding=encrypt_file_format,
              errors=errors_settings) as f:
        text = f.read()
    text_length = len(text)
    num = math.ceil(text_length**0.5)
    overflow = num**2 - text_length
    size = [num, num]
    length = size[0] * size[1]
    encrypt_mat = build(*size)
    encrypt_mat.fillin([random.randint(*number_range) for i in range(length)])
    while encrypt_mat.det() == 0:
        encrypt_mat.fillin(
            [random.randint(*number_range) for i in range(length)])
    encrypted_text = encrypt2(text, encrypt_mat, size)
    with open(self.filenames[0], 'w', encoding='utf-8-sig',
              errors='ignore') as f:
        f.write(str((encrypt_mat.element(), num, overflow)))
    with open(self.filenames[1], 'w', encoding='utf-8-sig',
              errors='ignore') as f:
        f.write(encrypted_text)
    self.current_msg.configure(
        text=f'加密成功，第一个文件是密钥文件，已保存在{self.filenames[0]},' + '\n' +
        f'第二个文件是密文，已保存在{self.filenames[1]}')


def encrypt2(text, mat, sizes):
    text_num = [ord(i) for i in text]
    text_mat = form(text_num, *sizes)
    new_mat = text_mat * mat
    new_mat_element = new_mat.element()
    return ''.join([chr(j) for j in new_mat_element])
