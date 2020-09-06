from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import random, math
from matrix import *
import numpy as np
with open('encrypt_config.py', encoding='utf-8-sig') as f:
    exec(f.read())
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.minsize(700, 600)
        self.filedialog = filedialog
        self.title('矩阵加密解密器')
        self.ask_which = ttk.Label(self, text='请选择你想要的加密方法')
        self.choosebox = Listbox(self)
        #self.choosebox.bind("<<ListboxSelect>>", self.enter_choose) 
        for i in range(9):
            self.choosebox.insert(END, f'第{i+1}种')
        self.ask_which.place(x=0, y=0)
        self.choosebox.place(x=0, y=30)        
        self.choosefile = ttk.Button(self, text='选择想要加密/解密的文件', command=self.openfile)
        self.choose_filename = ttk.Label(self, text='', wraplength=300)
        self.choosefile.place(x=200, y=60)
        self.choose_filename.place(x=200, y=90)
        self.choose_filename_path = None
        self.savefile = ttk.Button(self, text='选择保存加密/解密后的文件的路径', command=self.savefile)
        self.save_filename = ttk.Label(self, text='', wraplength=300)
        self.save_filename_path = None
        self.savefile.place(x=200, y=200)
        self.save_filename.place(x=200, y=230)        
        self.encrypt_button = ttk.Button(self, text='加密', command=self.encrypt_choose)
        self.decrypt_button = ttk.Button(self, text='解密', command=self.decrypt_choose)
        self.see_descriptions_button = ttk.Button(self, text='查看加密算法', command=self.see_descriptions)
        self.see_descriptions_button2 = ttk.Button(self, text='查看解密算法', command=self.see_descriptions2)
        self.encrypt_button.place(x=0, y=250)
        self.decrypt_button.place(x=0, y=300)
        self.see_descriptions_button.place(x=0, y=350)
        self.see_descriptions_button2.place(x=0, y=400)
        self.current_msg = ttk.Label(self, text='')
        self.current_msg.place(x=0, y=500)
        self.results = []
    
    def see_descriptions(self):
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/encrypt_{current}.py', encoding='utf-8-sig', errors='ignore') as f:
            exec(f.read(), globals()) 
        messagebox.showinfo(title=f'加密算法{current}', message=descriptions)
    
    def see_descriptions2(self):
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/decrypt_{current}.py', encoding='utf-8-sig', errors='ignore') as f:
            exec(f.read(), globals()) 
        messagebox.showinfo(title=f'解密算法{current}', message=descriptions)
        
    def enter_choose(self, e):
        current = self.choosebox.index(ANCHOR) + 1
        pass
    def openfile(self):
        filename = filedialog.askopenfilename(initialdir='.',
                                              title="选择文件",
                                              filetype=(("所有文件", "*.*"),))
        if filename:
            self.choose_filename_path = filename
            self.choose_filename.configure(text=filename)
    def savefile(self):
        if self.results:
            for each in self.results:
                filename = filedialog.asksaveasfile(initialdir='.',
                                                    title="选择文件",
                                                    filetype=(("所有文件", "*.*"),),
                                                    defaultextension=".txt")
                if filename:
                    current_write_style = write_style.pop(0)
                    if current_write_style == 'w':
                        with open(filename.name, 'w', encoding='utf-8-sig', errors='ignore') as f:
                            f.write(each)
                    elif current_write_style == 'wb':
                        with open(filename.name, 'wb') as f:
                            f.write(each)                        
            self.current_msg.configure(text = '保存文件成功')  
            self.results = []
        else:
            self.current_msg.configure(text = '暂时没有加密后的文件')
    
    def encrypt_choose(self):
        if not self.choose_filename_path:
            self.current_msg.configure(text = '请先选择要加密/解密的文件')    
            return
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/encrypt_{current}.py', encoding='utf-8-sig', errors='ignore') as f:
            exec(f.read(), globals()) 
        encrypt(self)
    
    def decrypt_choose(self):
        if not self.choose_filename_path:
            self.current_msg.configure(text = '请先选择要加密/解密的文件')    
            return
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/decrypt_{current}.py', encoding='utf-8-sig', errors='ignore') as f:
            exec(f.read(), globals()) 
        decrypt(self)
root = Root()
root.mainloop()