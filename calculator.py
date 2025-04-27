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

#function to handle keyboard events
def on_key(event):
    key = event.char
    if key.isdigit() or key in "+-*/.=":
        press(key)
    elif key == "\r": #Enter key
        equalpress()
    elif key == "\x08": #Backspace key
        clear()
    elif key == "^":
        press("**")
    elif key == "\x1b": #Escape key
        toggle_sign()

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

    #Bind keyboard events to functions
    gui.bind("<Key>", on_key)

    gui.mainloop()

