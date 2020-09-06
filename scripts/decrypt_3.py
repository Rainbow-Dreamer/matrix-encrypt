descriptions = '以二进制形式读取文件，得到其bytes的数组，将数组倒序，即可解密为原文件。'
write_style = ['wb']
def decrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    text = [i for i in text]
    text.reverse()
    self.results = [bytes(text)]
    self.current_msg.configure(
        text = '解密成功，第一个文件是明文'
    )    
    
