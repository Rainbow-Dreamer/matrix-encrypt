number_range = 2, 5
write_style = ['w', 'wb']
descriptions = '把明文的bytes数组每个8bit整数先进行正或负方向的随机数的移位，然后除以一个随机的整数（从两个整数之间的范围），\
除数从ASCII码转换成字符作为密文，余数的数组和随机整数的数组作为密钥，速度较快，适合加密比较大的文件'
# this is method 2, and this method is prepared for larger data to encrypt.
# the encrypting matrix in this method will be a string,
# and we will not calculating the inverse of the encrypting matrix
# in this method.
def encrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    
    text_length = len(text)
    if encrypt2_mode == 'string':
        text = [i + shift_num for i in text]
        shift_num = number_range[1]
        encrypt_ls = [
            random.randint(*number_range) for i in range(text_length)
        ]
        encrypt_str = ''.join([str(j) for j in encrypt_ls])
        encrypt_text = [text[i] // encrypt_ls[i] for i in range(text_length)]
        mod_str = ''.join(
            [str(text[i] % encrypt_ls[i]) for i in range(text_length)])
    elif encrypt2_mode == 'integer':
        text = [i for i in text]
        encrypt_str = random.randint(*number_range)
        encrypt_text = [text[i] // encrypt_str for i in range(text_length)]
        mod_str = ''.join(
            [str(text[i] % encrypt_str) for i in range(text_length)])
    self.results = [str(tuple((encrypt_str, mod_str))), bytes(encrypt_text)] 
    self.current_msg.configure(text = '加密成功，第一个文件是密钥文件，第二个文件是密文')