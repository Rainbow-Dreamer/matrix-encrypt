descriptions = '以二进制形式读取文件，得到其bytes的数组，将数组按照长度分成两半，\
形成两个新的bytes数组，两个bytes数组每次各自拿出一个，直到两个bytes数组都遍历完，\
即可解密为原文件。'
write_style = ['wb']
def decrypt(self):
    with open(self.choose_filename_path, 'rb') as f:
        text = f.read()
    text = [i for i in text]
    lens = len(text)
    ind = lens // 2
    odds = text[:ind]
    evens = text[ind:]
    text_new = []
    if ind % 2 != 0:
        odds.append(0)
        for j in range(ind):
            text_new.append(evens[j])
            text_new.append(odds[j])
        text_new.pop()
    else:
        for j in range(ind):
            text_new.append(evens[j])
            text_new.append(odds[j])
    self.results = [bytes(text_new)]
    self.current_msg.configure(
        text = '解密成功，第一个文件是明文'
    )    
