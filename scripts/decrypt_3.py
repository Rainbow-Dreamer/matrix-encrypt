descriptions = 'Read the file in binary form, get the array of its bytes, reverse the array, and decrypt it to the original file.'
write_style = ['wb']


def decrypt(self):
    with open(self.filenames[0], 'wb') as file:
        with open(self.choose_filename_path, 'rb') as f:
            for line in reversed(f.readlines()):
                file.write(bytes(list(line)[::-1]))
    self.current_msg.configure(
        text=f'Decrypt successfully, saved at {self.filenames[0]}')
