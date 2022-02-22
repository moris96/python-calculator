import math
from tkinter import *
from tkinter import messagebox
from math import pi, sqrt, pow


win = Tk()
win.geometry("500x500")
win.resizable(0,0)
win.title("Calculator")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# advanced math stuff
def btn_pi(item):
    global expression
    expression = expression + str(math.pi)
    input_text.set(expression)

def btn_sqrt(item): #square root
    global expression
    expression = math.sqrt(float(expression))
    input_text.set(expression)

def btn_squared(item): #exponent (to the power of)
    global expression
    expression = float(input_text.get())**2
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


class InputA:
    pass


class InputB:
    pass


def retrive_input(equation=None):
    try:
        global expression
        inputValue1 = InputA.get()
        inputValue2 = InputB.get()
        inputValue1 = float(inputValue1)
        inputValue2 = float(inputValue2)

        expression = float(math.sqrt(inputValue1 * inputValue1 + inputValue2 * inputValue2))
        equation.set(float(expression))
        expression = str(expression)

    except:
        equation.set("Error")
        expression = ""





def bt_equal():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = ""

    except: #error message when dividing by 0 or incorrect calculation
        input_text.set("ERROR")

expression = ""



input_text = StringVar()


input_frame = Frame(win, width=500, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(win, width=500, height=500, bg="grey")
btns_frame.pack()



## calculator layout:
# first row
clear = Button(btns_frame, text="C", fg="black", width=48, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg="black", width=15, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# second row
seven = Button(btns_frame, text="7", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg="black", width=15, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row
four = Button(btns_frame, text="4", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="black", width=15, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# fourth row
one = Button(btns_frame, text="1", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="black", width=15, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# fifth row
zero = Button(btns_frame, text="0", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, padx=1, pady=1)
decimal = Button(btns_frame, text=".", fg="black", width=15, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=1, padx=1, pady=1)
pie = Button(btns_frame, text="π", fg="black", width=15, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_pi("π")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg="black", width=15, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

# sixth row
squareRoot = Button(btns_frame, text="√", fg="black", width=15, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_sqrt("√")).grid(row=5, column=0, padx=1, pady=1)
squared = Button(btns_frame, text="x²", fg="black", width=15, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_squared("x²")).grid(row=5, column=1, padx=1, pady=1)


# run app
win.mainloop()