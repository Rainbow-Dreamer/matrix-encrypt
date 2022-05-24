descriptions = 'Change the byte at a random position in the bytes array of the file to a random byte integer (0-255), \
Execute the specified number of times to get the encrypted file. The key is the set of meta ancestors of the changed location and the value before the change.'

write_style = ['w', 'wb']
# this method is to change bytes to random bytes at random places of the data
# bytes of the file, and generates a key which shows where has been
# added random bytes


def encrypt(self):
    global decrypt7_num
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    text = [i for i in text]
    text_length = len(text)
    places = random.sample(range(text_length), decrypt7_num)
    if 0 not in places:
        places.append(0)
        decrypt7_num += 1
    for each in range(decrypt7_num):
        current = places[each]
        places[each] = (current, text[current])
        text[current] = random.randint(0, 255)
    with open(self.filenames[0], 'w', encoding='utf-8', errors='ignore') as f:
        f.write(str(places))
    with open(self.filenames[1], 'wb') as f:
        f.write(bytes(text))
    self.current_msg.configure(
        text=
        f'Encrypt successful,  the first file is key file, saved at {self.filenames[0]},'
        + '\n' +
        f'the second file is ciphertext file, saved at {self.filenames[1]}')