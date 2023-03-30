#Importing tkinter and math module
from tkinter import *
from math import *


#Creating tkinter window
##to display the widgets
window = Tk()

#Giving window a title
window.title('calculator')


# Creating entry widget which will
##display user input
e = Entry(window, width=37, borderwidth=20)
e.grid(row=0, column=0, columnspan=4)


#Defining functions for the buttons

##Function to continuously updates input field whenever you click a button
def button_click(number):
    
    """This function is to show values to the screen"""
    current_num = e.get()
    e.delete(0, END)
    e.insert(0, str(current_num) + str(number))

##Function to clear the display
def button_clear():
    """this function is to clear the screen"""
    e.delete(0, END)
    

def button_add():
    """This function perform the addition operation"""
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global operation
    f_num = float(first_number)
    operation = 'addition'



def button_subtract():
    """This function perform subtraction operation"""
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global operation
    f_num = float(first_number)
    operation = 'subtraction'

def button_multiply():
    """This function perform multiplication operation"""
    
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global operation
    f_num = float(first_number)
    operation = 'multiplication'


def button_divide():
    """This function perform division operation"""

    first_number = e.get()
    e.delete(0, END)
    global f_num
    global operation
    f_num = float(first_number)
    operation = 'division'



def button_root():
    """This function perform root operation"""

    first_number = e.get()
    e.delete(0, END)
    global f_num
    global operation
    f_num = float(first_number)
    e.insert(0, sqrt(f_num))
    operation = 'square root'

def button_exponent():
    """This function perform exponent operation"""

    first_number = e.get()
    e.delete(0, END)
    global f_num
    global operation
    f_num = float(first_number)
    operation = 'exponential'


def button_percentage():
    """This function calculate percentage"""
 
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global operation
    f_num = float(first_number)
    e.insert(0, f_num / float(100))
    operation = 'percentage'
    

##Function to calculate input values
def button_equal():
    """This function calculate and display the result"""
    second_num = e.get()
    e.delete(0, END)
    
    if operation == 'addition':
        e.insert(0, f_num + float(second_num))
    
    elif operation == 'subtraction':
        e.insert(0, f_num - float(second_num))
        
    elif operation == 'multiplication':
        e.insert(0, f_num * float(second_num))
    
    elif operation == 'division':
        e.insert(0, f_num / float(second_num))

    elif operation == 'exponential':
        e.insert(0, f_num ** float(second_num))


    

#generating buttons

button_1 = Button(window, text= '1', bg='light grey', padx=25, pady=20, command= lambda: button_click(1))
button_2 = Button(window, text= '2', bg='light grey', padx=25, pady=20, command= lambda: button_click(2))
button_3 = Button(window, text= '3', bg='light grey', padx=25, pady=20, command= lambda: button_click(3))
button_4 = Button(window, text= '4', bg='light grey', padx=25, pady=20, command= lambda: button_click(4))
button_5 = Button(window, text= '5', bg='light grey', padx=25, pady=20, command= lambda: button_click(5))
button_6 = Button(window, text= '6', bg='light grey', padx=25, pady=20, command= lambda: button_click(6))
button_7 = Button(window, text= '7', bg='light grey', padx=25, pady=20, command= lambda: button_click(7))
button_8 = Button(window, text= '8', bg='light grey', padx=25, pady=20, command= lambda: button_click(8))
button_9 = Button(window, text= '9', bg='light grey', padx=25, pady=20, command= lambda: button_click(9))
button_0 = Button(window, text= '0', bg='light grey', padx=25, pady=20, command= lambda: button_click(0))
button_point = Button(window, text= '.', bg='light grey', padx=26, pady=20, command= lambda: button_click('.'))


button_add = Button(window, text='+', bg='dim gray', padx=25, pady=20, command= button_add)
button_subtract = Button(window, text='-', bg='dim gray', padx=27, pady=20, command= button_subtract)
button_multiply = Button(window, text='x', bg='dim gray', padx=27, pady=20, command= button_multiply)
button_divide = Button(window, text='/', bg='dim gray', padx=27, pady=20, command= button_divide)


button_clear = Button(window, text= 'C', bg='dim gray', padx=24, pady=20, command= button_clear)
button_root = Button(window, text= '√', bg='dim gray', padx=24, pady=20, command= button_root)
button_exponent = Button(window, text= 'x^y', bg='dim gray', padx=18, pady=20, command= button_exponent)
button_percentage = Button(window, text= '%', bg='dim gray', padx=24, pady=20, command= button_percentage)
button_equal = Button(window, text= '=', bg= 'orange', padx=24, pady=20, command= button_equal)

#putting the button onto the screen

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_0.grid(row=5, column=0)
button_point.grid(row=5, column=1)

button_percentage.grid(row=1, column=3)
button_add.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)

button_clear.grid(row=1, column=0)
button_root.grid(row=1, column=1)
button_exponent.grid(row=1, column=2)

button_equal.grid(row=5, column=2)


window.mainloop()
