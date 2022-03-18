# we write the given statements to import required modules
from tkinter import *
import pyperclip
from random import *
from array import array

res=""
# creating the tkinter window
root = Tk()
root.geometry('400x400')
root.title('Password Generator')
lb1 = Label(root,text = 'Welcome to QuickPass password generator', font = 'Helvetica 16 bold')
lb1.pack()
lb2 = Label(root, text = 'Choose the length of your password: ')
lb2.place(x = 90, y = 25)
pass_len = IntVar()
l = Spinbox(root,from_ = 8, to_ = 32, textvariable = pass_len)
l.place(x = 97, y = 50)

# generating the password
pass_str = StringVar()
def generate():
    e.delete(0,END)
    dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    l_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
    u_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    comb_list = list(set(dig + l_char + u_char + symbols))
    password = ''
    # to make sure we have one character of every type, we start by making a 4 character passcode containing one of each type
    password = choice(l_char) + choice(dig) + choice(u_char) + choice(symbols)

    # to fill in the rest of the passcode upto required length
    for i in range(pass_len.get() - 4):
        password = password + choice(comb_list)

    # to ensure there is no repeated patttern, we convert our password into an array and shuffle it
    password_list = array('u',password)
    shuffle(password_list)

    password = ''
    for j in password_list:
        password = password + j

    pass_str.set(password)
#Strength of password window 
def OpenSecondWindow():
    global res
    win2=Tk()
    win2.geometry('400x400')
    win2.title('Password Strength Displayer')
    lb1 = Label(win2,text = 'Welcome to QuickPass Password Strength Displayer', font = 'Helvetica 16 bold')
    lb1.pack()
    lb2 = Label(win2, text = 'Enter password to be checked: ')
    lb2.place(x = 90, y = 25)
    e = Entry(win2)
    
    e.place(x = 95, y = 130)
    lb3 = Label(win2)
    lb3.place(x = 95, y = 180)
    def Strength():
        inputs=e.get() 
        n = len(inputs) 
     
        # Checking lower alphabet in string 
        hasLower = False
        hasUpper = False
        hasDigit = False
        specialChar = False
        normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
         
        for i in range(n):
            if inputs[i].islower():
                hasLower = True
            if inputs[i].isupper():
                hasUpper = True
            if inputs[i].isdigit():
                hasDigit = True
            if inputs[i] not in normalChars:
                specialChar = True
     
        # Strength of password 
        if (hasLower and hasUpper and
            hasDigit and specialChar and n >= 8):
            lb3.configure(text="Strong")
             
        elif ((hasLower or hasUpper) and
              specialChar and n >= 6):
              lb3.configure(text="Moderate")
        else:
            lb3.configure(text="Weak")
    strength_btn = Button(win2, text = 'Check Strength',command = lambda: Strength())
    strength_btn.place(x = 120, y = 95)
    
    
    
#function to get the strength
def Getit(t):
    Strength(t)
    print (res)
    
def Strength(inputs):
    print(inputs)  
    n = len(inputs) 
 
    # Checking lower alphabet in string 
    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
     
    for i in range(n):
        if inputs[i].islower():
            hasLower = True
        if inputs[i].isupper():
            hasUpper = True
        if inputs[i].isdigit():
            hasDigit = True
        if inputs[i] not in normalChars:
            specialChar = True
 
    # Strength of password 
    if (hasLower and hasUpper and
        hasDigit and specialChar and n >= 8):
        return "Strong"
         
    elif ((hasLower or hasUpper) and
          specialChar and n >= 6):
          return "Moderate"
    else:
        return "Weak"
        
# adding buttons and text field to display password
gen_btn = Button(root, text = 'GENERATE PASSWORD',command = generate)
gen_btn.place(x = 120, y = 95)
e = Entry(root, textvariable = pass_str)
e.place(x = 95, y = 130)

#Button to enter second window
gen_btn = Button(root, text = 'Open Password Strength Displayer',command = OpenSecondWindow)
gen_btn.place(x = 100, y = 190)
# adding the copy functionality
def copy():
    pyperclip.copy(pass_str.get())
copy_btn = Button(root, text = 'copy',command = copy)
copy_btn.place(x = 175, y = 160)

root.mainloop()
