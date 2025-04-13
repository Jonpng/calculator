from tkinter import *

# import everything from tkinter module
expression = ""

# Function to update expression 
# in the text entry box
def press(num):

    # point out the global expression variable 
    global expression

    # concatenation of string 
    expression = expression + str(num)

    # update the expression by using set method 
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""
    except:
        equation.set(" error ")
        expression = ""

#Function to clear the contents of text entry box 
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to toggle the sign of the current number
def toggle_sign():
    global expression
    if expression and expression[0] == '-':
        expression = expression[1:]
    else: 
        expression = '-' + expression
    equation.set(expression)

#driver code
if __name__ == "__main__":
    #create the GUI window
    gui = Tk()

     # set the background colour of GUI window
    gui.configure(background="gray28")

    # set the title of GUI window 
    gui.title("Calculator")

    equation = StringVar()

    #Create the text entry box for showing the expression
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    buttons = [
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
        ('0', 5, 1), ('+', 3, 1), ('-', 2, 3),
        ('*', 1, 2), ('/', 1, 1), ('=', 4, 3),
        ('C', 1, 0), ('.', 5, 2), ('^', 1, 3),
        ('x²', 1, 4), ('+/-', 5, 0)
    ]

    for (text, row, column) in buttons:
        btn = Button(gui, text=f' {text} ', fg='white', bg='grey40',
                     command=lambda t=text: press(t), height=1, width=7)
        btn.grid(row=row, column=column)

    num_rows = max(row for (_, row, _) in buttons) + 1
    num_columns = max(column for (_, _, column) in buttons) + 1
    window_width = num_columns * 65 #Adjust based on button size and padding
    window_height = num_rows * 35 #Adjust based on button size and padding

    gui.geometry(f"{window_width}x{window_height}")

#     # set the configuration of GUI window 
#     gui.geometry("265x175")

#     # StringVar() is the variable class we create an instance of this class
#     equation = StringVar()

#     # create the text entry box for showing the expression 
#     expression_field = Entry(gui, textvariable=equation)

#     # grid method is used for placing the widgets at respective positions in table like structure
#     expression_field.grid(columnspan=4, ipadx=70)
    
#  # create a Buttons and place at a particular location inside the root window 
#  # when user press the button, the command or function affiliated to that button is executed 
#     button1 = Button(gui, text=' 1 ', fg='white', bg='grey40',
#                     command=lambda: press(1), height=1, width=7)
#     button1.grid(row=4, column=0)
    
#     button2 = Button(gui, text=' 2 ', fg='white', bg='grey40',
#                     command=lambda: press(2), height=1, width=7)
#     button2.grid(row=4, column=1)

#     button3 = Button(gui, text=' 3 ', fg='white', bg='grey40',
#                     command=lambda: press(3), height=1, width=7)
#     button3.grid(row=4, column=2)

#     button4 = Button(gui, text=' 4 ', fg='white', bg='grey40',
#                     command=lambda: press(4), height=1, width=7)
#     button4.grid(row=3, column=0)

#     button5 = Button(gui, text=' 5 ', fg='white', bg='grey40',
#                     command=lambda: press(5), height=1, width=7)
#     button5.grid(row=3, column=1)

#     button6 = Button(gui, text=' 6 ', fg='white', bg='grey40',
#                     command=lambda: press(6), height=1, width=7)
#     button6.grid(row=3, column=2)

#     button7 = Button(gui, text=' 7 ', fg='white', bg='grey40',
#                     command=lambda: press(7), height=1, width=7)
#     button7.grid(row=2, column=0)

#     button8 = Button(gui, text=' 8 ', fg='white', bg='grey40',
#                     command=lambda: press(8), height=1, width=7)
#     button8.grid(row=2, column=1)

#     button9 = Button(gui, text=' 9 ', fg='white', bg='grey40',
#                     command=lambda: press(9), height=1, width=7)
#     button9.grid(row=2, column=2)

#     button0 = Button(gui, text=' 0 ', fg='white', bg='grey40',
#                     command=lambda: press(0), height=1, width=7)
#     button0.grid(row=5, column=1)

#     plus = Button(gui, text=' + ', fg='white', bg='grey40',
#                   command=lambda: press("+"), height=1, width=7)
#     plus.grid(row=3, column=3)

#     minus = Button(gui, text=' - ', fg='white', bg='grey40',
#                   command=lambda: press("-"), height=1, width=7)
#     minus.grid(row=2, column=3)

#     multiply = Button(gui, text=' * ', fg='white', bg='grey40',
#                   command=lambda: press("*"), height=1, width=7)
#     multiply.grid(row=1, column=2)

#     divide = Button(gui, text=' / ', fg='white', bg='grey40',
#                   command=lambda: press("/"), height=1, width=7)
#     divide.grid(row=1, column=1)

#     equal = Button(gui, text=' = ', fg='white', bg='grey40',
#                   command=equalpress, height=1, width=7)
#     equal.grid(row=4, column=3)

#     clear = Button(gui, text='C', fg='white', bg='grey40',
#                   command=clear, height=1, width=7)
#     clear.grid(row=1, column=0)

#     Decimal= Button(gui, text='.', fg='white', bg='grey40',
#                     command=lambda: press('.'), height=1, width=7)
#     Decimal.grid(row=5, column=2)

#     exponent = Button(gui, text=' ^ ', fg='white', bg='grey40',
#                       command=lambda: press("**"), height=1, width=7)
#     exponent.grid(row=1, column=3)

#     square = Button(gui, text=' x² ', fg='white', bg='grey40',
#                     command=lambda: press("**2"), height=1, width=7)
#     square.grid(row=1, column=4)

#     toggle_sign_button = Button(gui, text=' +/- ', fg='white', bg='grey40',
#                                 command=toggle_sign, height=1, width=7)
#     toggle_sign_button.grid(row=5, column=0)

    #start the gui
    gui.mainloop()

