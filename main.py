# Getting Libraries
from tkinter import messagebox, simpledialog, Tk


def is_even(num):
    return num % 2 == 0


def get_even_letters(mes):
    even = []
    for i in range(len(mes)):
        if is_even(i):
            even.append(mes[i])
    return even


def get_odd_letters(mes):
    odd = []
    for i in range(len(mes)):
        if not is_even(i):
            odd.append(mes[i])
    return odd


def swap_letters(mes):
    temp = []
    if not is_even(len(mes)):
        mes = mes + 'x'
    even = get_even_letters(mes)
    odd = get_odd_letters(mes)

    for i in range(len(mes)//2):
        temp.append(odd[i])
        temp.append(even[i])
    new = ''.join(temp)
    return new


def choice():
    option = simpledialog.askstring("Select", "Do you want to encrypt or decrypt?")
    return option


def message():
    mes = simpledialog.askstring("message", "Enter the message:")
    return mes


root = Tk()

while True:
    option = choice()
    if option == "encrypt":
        mes = message()
        encrypt = swap_letters(mes)
        messagebox.showinfo("Encrypted message is :", encrypt)

    elif option == "decrypt":
        mes = message()
        decrypt = swap_letters(mes)
        messagebox.showinfo("Decrypted Message is :", decrypt)
    else:
        break
root.mainloop()