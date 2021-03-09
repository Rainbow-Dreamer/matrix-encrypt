descriptions = '以二进制形式读取文件，得到其bytes的数组，将数组的奇数位排在一起\
形成奇数bytes数列，偶数位排在一起形成偶数bytes数列，然后把奇数bytes数列接上偶数bytes数列，\
即可得到密文。'

write_style = ['wb']


# this method is rearranging the orders of the data bytes by a user-defined
# rule, and to decrypt we just need to do the inverse operations of the rule,
# in this method the default rule is reordering by odds and evens of indexes
# of the data bytes of the files
def encrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    text = [i for i in text]
    lens = len(text)
    text = [text[i] for i in range(lens) if i % 2 != 0
            ] + [text[i] for i in range(lens) if i % 2 == 0]
    with open(self.filenames[0], 'wb') as f:
        f.write(bytes(text))
    self.current_msg.configure(text=f'加密成功，第一个文件是密文，已保存在{self.filenames[0]}')