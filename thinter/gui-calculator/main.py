# tkinter is gui module to create the graphical interfaces
# we have two methods mainly in tkinter
# 1) Tk() method to create a main widget or window
# 2) mainloop() used to run the window

from tkinter import *

val1 = ""
val2 = ""
temp = 1
opt = ""
def bf1():
    global val2, val1, temp
    print("1")
    if temp == 1:
        val1 = val1 + "1"
    elif temp == 2:
        val2 = val2 + "1"
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)

def bf2():
    print("2")
    global val2, val1, temp
    if temp == 1:
        val1 = val1 + "2"
    elif temp == 2:
        val2 = val2 + "2"
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)



def bf3():
    global val2, val1, temp
    print("3")
    if temp == 1:
        val1 = val1 + "3"
    elif temp == 2:
        val2 = val2 + "3"
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)

def bf4():
    global val2, val1, temp
    print("4")
    if temp == 1:
        val1 = val1 + "4"
    elif temp == 2:
        val2 = val2 + "4"
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)

def bf5():
    global val2, val1, temp
    print("5")
    if temp == 1:
        val1 = val1 + "5"
    elif temp == 2:
        val2 = val2 + "5"
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)


def bf6():
    global val2, val1, temp
    print("6")
    if temp == 1:
        val1 = val1 + "6"
    elif temp == 2:
        val2 = val2 + "6"
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)


def bf7():
    global val2, val1,temp
    print("7")
    if temp == 1:
        val1 = val1 + "7"
    elif temp == 2:
        val2 = val2 + "7"
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)


def bf8():
    global val2, val1, temp
    print("8")
    if temp == 1:
        val1 = val1 + "8"
    elif temp == 2:
        val2 = val2 + "8"
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)


def bf9():
    global val2, val1, temp
    print("9")
    if temp == 1:
        val1 = val1 + "9"
    elif temp == 2:
        val2 = val2 + "9"
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)


def bf0():
    global val2, val1, temp
    print("0")
    if temp == 1:
        val1 = val1 + "0"
    elif temp == 2:
        val2 = val2 + "0"
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)

def bfadd():
    global val2, val1, temp, opt
    print("addition")
    val1 = int(val1)
    temp = 2
    opt = '+'
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)

def bfsub():
    global val2, val1, temp, opt
    print("addition")
    val1 = int(val1)
    temp = 2
    opt = '-'
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)

def bfmul():
    global val2, val1, temp, opt
    print("addition")
    val1 = int(val1)
    temp = 2
    opt = '*'
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)

def bfdiv():
    global val2, val1, temp, opt
    print("addition")
    val1 = int(val1)
    temp = 2
    opt = '/'
    label = Label(window, text=f"{val1} {opt} {val2}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)

def bftotal():
    global val2, val1, temp, opt
    val2 = int(val2)
    temp = 1
    if opt == '+':
        sum = val1 + val2
    elif opt == '-':
        sum = val1-val2
    elif opt == '*':
        sum = val1 * val2
    elif opt == '/':
        sum = val1/val2
    print(sum)
    label = Label(window, text=f"{val1} {opt} {val2} = {sum}", font=("Arial", 20), background="Yellow")
    label.place(x=700,y=40)
    val1=""
    val2=""
    opt=""





# creating tkinter object
window = Tk()


# crating a label widget which disaplays the string
mylabel = Label(text="Calculator", font=("Arial",20))
mb1 = Button(window, text="1", command=bf1, width=30, height=4, bg="skyblue",font=("Arial",15))
mb2 = Button(window, text="2", command=bf2, width=30, height=4, bg="skyblue",font=("Arial",15))
mb3 = Button(window, text="3", command=bf3, width=30, height=4, bg="skyblue",font=("Arial",15))
mb4 = Button(window, text="4", command=bf4, width=30, height=4, bg="skyblue",font=("Arial",15))
mb5 = Button(window, text="5", command=bf5, width=30, height=4, bg="skyblue",font=("Arial",15))
mb6 = Button(window, text="6", command=bf6, width=30, height=4, bg="skyblue",font=("Arial",15))
mb7 = Button(window, text="7", command=bf7, width=30, height=4, bg="skyblue",font=("Arial",15))
mb8 = Button(window, text="8", command=bf8, width=30, height=4, bg="skyblue",font=("Arial",15))
mb9 = Button(window, text="9", command=bf9, width=30, height=4, bg="skyblue",font=("Arial",15))
mb0 = Button(window, text="0", command=bf0, width=30, height=4, bg="skyblue",font=("Arial",15))
mb11 = Button(window, text="+", command=bfadd, width=10, height=2, bg="skyblue",font=("Arial",25))
mb12 = Button(window, text="-", command=bfsub, width=10, height=2, bg="skyblue",font=("Arial",25))
mb13 = Button(window, text="*", command=bfmul, width=10, height=2, bg="skyblue",font=("Arial",25))
mb14 = Button(window, text="/", command=bfdiv, width=10, height=2, bg="skyblue",font=("Arial",25))
mb15 = Button(window, text="=", command=bftotal, width=10, height=2, bg="skyblue",font=("Arial",25))

# placing widgets
mylabel.place(x=700, y=0)
mb1.place(x=100, y=100)
mb2.place(x=500, y=100)
mb3.place(x=900, y=100)
mb4.place(x=100, y=200)
mb5.place(x=500, y=200)
mb6.place(x=900, y=200)
mb7.place(x=100, y=300)
mb8.place(x=500, y=300)
mb9.place(x=900, y=300)
mb0.place(x=500, y=400)
mb11.place(x=1300, y=100)
mb12.place(x=1300, y=200)
mb13.place(x=1300, y=300)
mb14.place(x=1300, y=400)
mb15.place(x=1300, y=600)

# packing label
#mylabel.grid(row=1, column=5)

print(val1, val2)

window.mainloop()
