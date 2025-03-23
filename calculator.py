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

#driver code
if __name__ == "__main__":
    #create the GUI window
    gui = Tk()

     # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window 
    gui.title("Calculator")

    # set the configuration of GUI window 
    gui.geometry("270x150")

    # StringVar() is the variable class we create an instance of this class
    equation = StringVar()

    # create the text entry box for showing the expression 
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing the widgets at respective positions in table like structure
    expression_field.grid(columspan=4, ipadx=70)

    

