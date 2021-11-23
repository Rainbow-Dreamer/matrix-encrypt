descriptions = 'Read the file in binary form, get its array of bytes, divide the array into two halves according to its length, \
to form two new bytes arrays, and the two bytes arrays are taken out one at a time, until both bytes arrays are traversed, \
can be decrypted to the original file.'

write_style = ['wb']


def decrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    text = [i for i in text]
    lens = len(text)
    is_odd = lens % 2 != 0
    ind = lens // 2
    odds = text[:ind]
    evens = text[ind:]
    text_new = []
    for j in range(ind):
        text_new.append(evens[j])
        text_new.append(odds[j])
    if is_odd:
        text_new.append(evens[ind])
    with open(self.filenames[0], 'wb') as f:
        f.write(bytes(text_new))
    self.current_msg.configure(
        text=f'Decrypt successfully, saved at {self.filenames[0]}')
