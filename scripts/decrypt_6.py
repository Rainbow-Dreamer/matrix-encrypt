descriptions = '以二进制形式读取文件，得到其bytes的数组，将数组装入一个维度为文件的bytes数量的向下取整平方根的方块矩阵，\
将矩阵进行转置，取出所有元素作为新的bytes数组，再减去之前矩阵溢出的位数即可解密为原文件。'

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
    self.current_msg.configure(text=f'解密成功，已保存在{self.filenames[0]}')