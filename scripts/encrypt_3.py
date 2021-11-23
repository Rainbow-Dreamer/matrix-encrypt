# this method is just simply reverse the order binary data of the file
# you want to encrypt, it is obviously not a method for plain text encrypting,
# but for media files (music files, video files, image files and so on)
# this is very useful and very quick to encrypt and decrypt.
descriptions = 'Read the file in binary form, get an array of its bytes, reverse the array and form the ciphertext,\
Form the encrypted file in binary form. The speed is the fastest among several algorithms, and it is more suitable for encrypting large files.'

write_style = ['wb']


def encrypt(self):
    with open(self.filenames[0], 'wb') as file:
        with open(self.choose_filename_path, 'rb') as f:
            for line in reversed(f.readlines()):
                file.write(bytes(list(line)[::-1]))
    self.current_msg.configure(
        text=
        f'Encrypt successful,  the first file is ciphertext file, saved at {self.filenames[0]}'
    )
