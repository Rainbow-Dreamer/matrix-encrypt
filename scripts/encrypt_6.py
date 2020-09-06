
# this method is to fill the data bytes of the file into a matrix,
# and calculate the transpose of the matrix, and then fill in data bytes
# of the transposed matrix to the encrypted file.
# (This method mainly applies for all of the files excepts plain text files)
descriptions = '以二进制形式读取文件，得到其bytes的数组，将数组装入一个维度为文件的bytes数量的向下取整平方根的方块矩阵，\
将矩阵进行转置，取出所有元素作为密文的bytes数组，写入新文件即可得到加密的文件。'
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
    self.results = [bytes(text_new)]
    self.current_msg.configure(
       text = '加密成功，第一个文件是密文'
   )    
    