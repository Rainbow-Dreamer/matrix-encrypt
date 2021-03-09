descriptions = '使用正交矩阵来对文件进行加密，在这里为对角矩阵，加密的细节与第一种加密算法类似，\
使用对角矩阵加密的好处是解密的时候计算密钥矩阵的逆只需要计算矩阵的转置（因为正交矩阵的一个性质就是\
其逆等于其转置），从而大大加快了解密的速度，（计算一个大型矩阵的逆所费的算力往往要远大于计算其转置）\
更加适用于大型文件的加密和解密。另外一个与第一种加密算法的区别是这里的加密对象是文件的bytes数组。'

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
        text=f'加密成功，第一个文件是密钥文件，已保存在{self.filenames[0]},' + '\n' +
        f'第二个文件是密文，已保存在{self.filenames[1]}')
