# this method is just simply reverse the order binary data of the file
# you want to encrypt, it is obviously not a method for plain text encrypting,
# but for media files (music files, video files, image files and so on)
# this is very useful and very quick to encrypt and decrypt.
descriptions = '以二进制形式读取文件，得到其bytes的数组，将数组倒序，形成密文，\
以二进制的形式形成加密的文件。速度是几种算法里最快的，更加适用于加密大型文件。'

write_style = ['wb']


def encrypt(self):
    with open(self.filenames[0], 'wb') as file:
        with open(self.choose_filename_path, 'rb') as f:
            for line in reversed(f.readlines()):
                file.write(bytes(list(line)[::-1]))
    self.current_msg.configure(text=f'加密成功，第一个文件是密文，已保存在{self.filenames[0]}')
