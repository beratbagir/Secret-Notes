import tkinter
from tkinter import *
import pybase64
from tkinter import messagebox


def save_and_encrypt_notes():
    title = weight_put.get()
    message = my_text.get("1.0", END)
    master_secret = my_entry.get()

window = Tk()
window.title("Secret Notes")
window.minsize(width=220, height=350)

#encryption

#def save_and_encrypt_notes():
    #title = weight_put.get()
    #message = my_text.get("1.0", END)
    #master_secret = my_entry.get()

    #with open("mysecret.txt", "a") as data_file:
        #data_file.write(f"\n{title}\n{message}")
def encrypt():
    secret = my_text.get(1.0,END)
    my_text.delete(1.0,END)

    if my_entry.get() == "password":
        secret = secret.encode("ascii")
        secret = pybase64.b64encode(secret)
        secret = secret.decode("ascii")
        my_text.insert(END, secret)

    else:
        messagebox.showwarning("Incorrect!","Incorrect Password, Try Again!")

def decrypt():
    secret = my_text.get(1.0,END)
    my_text.delete(1.0, END)

    if my_entry.get() == "password":
        secret = secret.encode("ascii")
        secret = pybase64.b64decode(secret)
        secret = secret.decode("ascii")
        my_text.insert(END, secret)


    else:
        messagebox.showwarning("Incorrect!","Incorrect Password, Try Again!")

#uı


my_label = Label(text="Enter your title")
my_label.config(fg="black")
my_label.pack()
weight_put = tkinter.Entry(width=15)
weight_put.pack()


my_label2 = Label(text="Enter your secret")
my_label2.config(fg="black")
my_label2.pack()
my_text = tkinter.Text(width=30, height=10)
my_text.pack()

my_label3 = Label(text="Enter master key")
my_label3.config(fg="red")
my_label3.pack()
my_entry = tkinter.Entry(width=15)
my_entry.pack()

encrypt_button = tkinter.Button(text="Save & Encrypt", command=encrypt)
encrypt_button.pack()

decrypt_button = tkinter.Button(text="Decrypt", command=decrypt)
decrypt_button.pack()




window.mainloop()