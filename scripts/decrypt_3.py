descriptions = '以二进制形式读取文件，得到其bytes的数组，将数组倒序，即可解密为原文件。'
write_style = ['wb']


def decrypt(self):
    with open(self.filenames[0], 'wb') as file:
        with open(self.choose_filename_path, 'rb') as f:
            for line in reversed(f.readlines()):
                file.write(bytes(list(line)[::-1]))
    self.current_msg.configure(text=f'解密成功，已保存在{self.filenames[0]}')
