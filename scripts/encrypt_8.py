descriptions = 'Read the file in binary form, get an array of its bytes, line up the odd bits of the array together \
to form an odd bytes array, and the even bits are lined up to form an even bytes array, and then the odd bytes array is connected to the even bytes array, \
to get the ciphertext.'

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
    self.current_msg.configure(
        text=
        f'Encrypt successful,  the first file is ciphertext file, saved at {self.filenames[0]}'
    )
