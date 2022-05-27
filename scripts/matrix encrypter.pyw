from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import random, math
import numpy as np
import os
import sys
import fractions

sys.path.append('scripts')
from matrixpro.matrix import *
with open('scripts/encrypt_config.py', encoding='utf-8') as f:
    exec(f.read())
write_style = []


class Root(Tk):

    def __init__(self):
        super(Root, self).__init__()
        self.minsize(1000, 600)
        self.filedialog = filedialog
        self.title('matrix encrypter')
        self.ask_which = ttk.Label(
            self, text='please choose the encryption algorithm')
        self.choosebox = Listbox(self)
        for i in range(9):
            self.choosebox.insert(END, f'number {i+1}')
        self.ask_which.place(x=0, y=0)
        self.choosebox.place(x=0, y=30)
        self.choosefile = ttk.Button(
            self,
            text='please choose the file to encrypt/decrypt',
            command=self.openfile)
        self.choose_filename = ttk.Label(self, text='', wraplength=300)
        self.choosefile.place(x=200, y=60)
        self.choose_filename.place(x=200, y=90)
        self.choose_filename_path = None
        self.save_filename = ttk.Label(self, text='', wraplength=300)
        self.save_filename_path = None
        self.save_filename.place(x=200, y=230)
        self.encrypt_button = ttk.Button(self,
                                         text='encrypt',
                                         command=self.encrypt_choose)
        self.decrypt_button = ttk.Button(self,
                                         text='decrypt',
                                         command=self.decrypt_choose)
        self.see_descriptions_button = ttk.Button(
            self,
            text='check encryption algorithm',
            command=self.see_descriptions)
        self.see_descriptions_button2 = ttk.Button(
            self,
            text='check decryption algorithm',
            command=self.see_descriptions2)
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
                  encoding='utf-8',
                  errors='ignore') as f:
            exec(f.read(), globals())
        messagebox.showinfo(title=f'encryption algorithm {current}',
                            message=descriptions)

    def see_descriptions2(self):
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/decrypt_{current}.py',
                  encoding='utf-8',
                  errors='ignore') as f:
            exec(f.read(), globals())
        messagebox.showinfo(title=f'decryption algorithm {current}',
                            message=descriptions)

    def openfile(self):
        filename = filedialog.askopenfilename(title="Choose file",
                                              filetypes=(("All files", "*"), ))
        if filename:
            self.choose_filename_path = filename
            self.choose_filename.configure(text=filename)

    def savefile(self, mode=0):
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/encrypt_{current}.py'
                  if mode == 0 else f'scripts/decrypt_{current}.py',
                  encoding='utf-8',
                  errors='ignore') as f:
            exec(f.read(), globals())
        self.filenames = []
        if len(write_style) == 2:
            current_mode = 1
        else:
            current_mode = 0
        for each in range(len(write_style)):
            filename = filedialog.asksaveasfile(
                title="Choose the save path of key file"
                if current_mode == 1 and each == 0 else
                ("Choose the save path of ciphertext"
                 if mode == 0 else "Choose the save path of plaintext"),
                filetypes=(("All files", "*"), ))
            if filename:
                self.filenames.append(filename.name)
        if len(self.filenames) == len(write_style):
            self.current_msg.configure(text='The file will be saved at:\n' +
                                       '\n'.join(self.filenames))

    def encrypt_choose(self):
        if not self.choose_filename_path:
            self.current_msg.configure(
                text='please choose the file to encrypt/decrypt first')
            return
        self.savefile(mode=0)
        self.update()
        if not write_style or len(self.filenames) != len(write_style):
            self.current_msg.configure(
                text=
                'please choose the save path of the encrypted/decrypted file')
            return
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/encrypt_{current}.py',
                  encoding='utf-8',
                  errors='ignore') as f:
            exec(f.read(), globals())
        encrypt(self)

    def decrypt_choose(self):
        if not self.choose_filename_path:
            self.current_msg.configure(
                text='please choose the file to encrypt/decrypt first')
            return
        self.savefile(mode=1)
        self.update()
        if not write_style or len(self.filenames) != len(write_style):
            self.current_msg.configure(
                text=
                'please choose the save path of the encrypted/decrypted file')
            return
        current = self.choosebox.index(ACTIVE) + 1
        with open(f'scripts/decrypt_{current}.py',
                  encoding='utf-8',
                  errors='ignore') as f:
            exec(f.read(), globals())
        decrypt(self)


root = Root()
root.mainloop()