from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import random, math
from matrix import *
import numpy as np
with open('encrypt_config.py', encoding='utf-8-sig') as f:
    exec(f.read())
write_style = []


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.minsize(1000, 600)
        self.filedialog = filedialog
        self.title('矩阵加密解密器')
        self.ask_which = ttk.Label(self, text='请选择你想要的加密方法')
        self.choosebox = Listbox(self)
        #self.choosebox.bind("<<ListboxSelect>>", self.enter_choose)
        for i in range(9):
            self.choosebox.insert(END, f'第{i+1}种')
        self.ask_which.place(x=0, y=0)
        self.choosebox.place(x=0, y=30)
        self.choosefile = ttk.Button(self,
                                     text='选择想要加密/解密的文件',
                                     command=self.openfile)
        self.choose_filename = ttk.Label(self, text='', wraplength=300)
        self.choosefile.place(x=200, y=60)
        self.choose_filename.place(x=200, y=90)
        self.choose_filename_path = None
        self.save_filename = ttk.Label(self, text='', wraplength=300)
        self.save_filename_path = None
        self.save_filename.place(x=200, y=230)
        self.encrypt_button = ttk.Button(self,
                                         text='加密',
                                         command=self.encrypt_choose)
        self.decrypt_button = ttk.Button(self,
                                         text='解密',
                                         command=self.decrypt_choose)
        self.see_descriptions_button = ttk.Button(
            self, text='查看加密算法', command=self.see_descriptions)
        self.see_descriptions_button2 = ttk.Button(
            self, text='查看解密算法', command=self.see_descriptions2)
        self.encrypt_button.place(x=0, y=250)
        self.decrypt_button.place(x=0, y=300)
        self.see_descriptions_button.place(x=0, y=350)
        self.see_descriptions_button2.place(x=0, y=400)
        self.current_msg = ttk.Label(self, text='')
        self.current_msg.place(x=0, y=500)
        self.filenames = []

    def see_descriptions(self):
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/encrypt_{current}.py',
                  encoding='utf-8-sig',
                  errors='ignore') as f:
            exec(f.read(), globals())
        messagebox.showinfo(title=f'加密算法{current}', message=descriptions)

    def see_descriptions2(self):
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/decrypt_{current}.py',
                  encoding='utf-8-sig',
                  errors='ignore') as f:
            exec(f.read(), globals())
        messagebox.showinfo(title=f'解密算法{current}', message=descriptions)

    def enter_choose(self, e):
        current = self.choosebox.index(ANCHOR) + 1
        pass

    def openfile(self):
        filename = filedialog.askopenfilename(initialdir='.',
                                              title="选择文件",
                                              filetype=(("所有文件", "*.*"), ))
        if filename:
            self.choose_filename_path = filename
            self.choose_filename.configure(text=filename)

    def savefile(self, mode=0):
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/encrypt_{current}.py'
                  if mode == 0 else f'scripts/decrypt_{current}.py',
                  encoding='utf-8-sig',
                  errors='ignore') as f:
            exec(f.read(), globals())
        self.filenames = []
        if len(write_style) == 2:
            current_mode = 1
        else:
            current_mode = 0
        for each in range(len(write_style)):
            filename = filedialog.asksaveasfile(
                initialdir='.',
                title="选择密钥文件的保存路径" if current_mode == 1 and each == 0 else
                ("选择密文的保存路径" if mode == 0 else "选择明文的保存路径"),
                filetype=(("所有文件", "*.*"), ))
            if filename:
                self.filenames.append(filename.name)
        if len(self.filenames) == len(write_style):
            self.current_msg.configure(text='文件将保存在:\n' +
                                       '\n'.join(self.filenames))

    def encrypt_choose(self):
        if not self.choose_filename_path:
            self.current_msg.configure(text='请先选择要加密/解密的文件')
            return
        self.savefile(mode=0)
        self.update()
        if not write_style or len(self.filenames) != len(write_style):
            self.current_msg.configure(text='请先选择加密/解密后的文件保存的路径')
            return
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/encrypt_{current}.py',
                  encoding='utf-8-sig',
                  errors='ignore') as f:
            exec(f.read(), globals())
        encrypt(self)

    def decrypt_choose(self):
        if not self.choose_filename_path:
            self.current_msg.configure(text='请先选择要加密/解密的文件')
            return
        self.savefile(mode=1)
        self.update()
        if not write_style or len(self.filenames) != len(write_style):
            self.current_msg.configure(text='请先选择加密/解密后的文件保存的路径')
            return
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/decrypt_{current}.py',
                  encoding='utf-8-sig',
                  errors='ignore') as f:
            exec(f.read(), globals())
        decrypt(self)


root = Root()
root.mainloop()