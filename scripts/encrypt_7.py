descriptions = '在文件的bytes数组的随机的位置上的byte改变成随机的byte整数(0-255)，\
执行指定的次数，即可得到加密后的文件。（每次选择的位置会保证跟之前的不重复）密钥为改变的位置和改变之前的值的元祖集合。'

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
    with open(self.filenames[0], 'w', encoding='utf-8-sig',
              errors='ignore') as f:
        f.write(str(places))
    with open(self.filenames[1], 'wb') as f:
        f.write(bytes(text))
    self.current_msg.configure(
        text=f'加密成功，第一个文件是密钥文件，已保存在{self.filenames[0]},' + '\n' +
        f'第二个文件是密文，已保存在{self.filenames[1]}')