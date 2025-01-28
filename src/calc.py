from tkinter import *
import math
from pygame import mixer
import speech_recognition

## FUNCTIONALITY
# Handle click buttons function
def click(val):
    e = entryField.get()  # Getting the button's value
    answer = " "

    try:
        # Delete the last inserted value
        if val == "C":
            e = e[0:len(e) - 1]  # Slicing the content, then deleting the last entered value
            entryField.delete(0, "end") # Delete previous content
            entryField.insert(0, e) # Insert sliced content
            return

        # Clear entry field
        elif val == "CE":
            entryField.delete(0, "end")

        # Square root
        elif val == "√":
            answer = math.sqrt(eval(e))
            # eval() parses the expression argument and evaluates it as a Python expression
            # In this case, the eval() will turn the e string into an int/float

        # pi value
        elif val == "π":
            answer = math.pi

        # cos value
        elif val == "cosθ":
            answer = math.cos(math.radians(eval(e)))
            # cos() returns the cosine of x (in radians)
            # math.radians() transforms the input into rad to pass it to the cos()

        # sin value
        elif val == "sinθ":
            answer = math.sin(math.radians(eval(e)))

        # tan Value
        elif val == "tanθ":
            answer = math.tan(math.radians(eval(e)))

        # 2π value
        elif val == "2π":
            answer = 2 * math.pi

        # cosh value
        elif val == "cosh":
            answer = math.cosh(eval(e))
            # math.cosh() returns the hyperbolic cosine of x

        # sinh value
        elif val == "sinh":
            answer = math.sinh(eval(e))

        # tanh value
        elif val == "tanh":
            answer = math.tanh(eval(e))

        # cube root value
        elif val == chr(8731): # This is the convention that represents cube root
            answer = eval(e) ** (1 / 3) # ** means "to the power of"

        # x to the power y
        elif val == "x\u02b8":
            entryField.insert("end", "**")
            return # The last two lines (which clear the entry field) won't be executed
            # The user clicks this button after typing the "x" (the base). Then the value followed by "**" is returned, for them to type "y" (the power)

        # cube value
        elif val == "x\u00B3":
            answer = eval(e) ** 3

        # square value
        elif val == "x\u00B2":
            answer = eval(e) ** 2

        # ln value
        elif val == "ln":
            answer = math.log2(eval(e))
            # math.log2() returns the base 2 logarithm of x (2**[answer] = x)

        # deg value
        elif val == "deg":
            answer = math.degrees(eval(e))
            # Convert angle x from radians to degrees

        # radian value
        elif val == "rad":
            answer = math.radians(eval(e))
            # Convert angle x from degrees to radians

        # e value
        elif val == "e":
            answer = math.e

        # log10 value
        elif val == "log10":
            answer = math.log10(eval(e))
            # log10() returns the base 10 logarithm of x (10**[answer] = x)

        # factorial value
        elif val == "x!":
            answer = math.factorial(eval(e))

        # division operator
        elif val == chr(247):
            entryField.insert("end", "/")
            return # The last two lines (which clear the entry field) won't be executed

        elif val == "=":
            answer = eval(e)
            # The function will perform the equation written on the entry field

        else:
            entryField.insert("end", val)
            return # The last two lines (which clear the entry field) won't be executed
            # This statement handles the numbers' and operators buttons, inserting their values into the entry field

        entryField.delete(0, "end")
        entryField.insert(0, answer)

    except SyntaxError:
        pass

# Audio words understanding functionality
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def sqrt(*a):
    return math.sqrt(a[0])

def power(a,b):
    return math.pow(a,b)

def fact(*a):
    return math.factorial(a[0])

def cube(*a):
    return math.pow(a[0],3)

def square(*a):
    return math.pow(a[0],2)

def log10(*a):
    return math.log(a[0],10)

def ln(*a):
    return math.log(a[0],math.e)

operations = {"ADD": add, "SUM": add, "ADDITION": add, "PLUS": add,
              "SUBTRACT": sub, "DIFFERENCE": sub, "SUBTRACTION": sub,
              "MINUS": sub, "MULTIPLY": mul, "MULTIPLY BY": mul,
              "MULTIPLICATION": mul, "INTO": mul, "PRODUCT": mul,
              "DIVIDE": div, "DIVISION": div, "DIV": div, "BY": div,
              "MOD": mod, "MODULUS": mod, "REMAINDER": mod, "ROOT":sqrt,
              "SQUARE ROOT":sqrt, "POWER":power,"RAISE TO":power, "SQUARE":square,
              "CUBE":cube, "LOG":log10,"LN":ln,"NATURAL":ln, "FACTORIAL":fact
              } # When user says "ADD" (key), call the add function (value)

# Audio capturing functionality
mixer.init()

def findNumbers(text):
    n=[] # Numbers will be added to this list
    for num in text:
        try:
            n.append(float(num)) # If a text is successfully converted into float, it is a number
        except ValueError:
            pass
    return n

def audio():
    mixer.music.load("assets\audio\click.wav")
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m, duration=0.2) # If there is a gap of 0.2 seconds, what comes next will be treated as another sentence
            voice = sr.listen(m)
            text = sr.recognize_google(voice) # Store the audio information as text

            mixer.music.load("assets\audio\click.wav") # After it's done, a click sound is made to indicate that to the user
            mixer.music.play()

            text_split = text.split(" ") # e.g. "multiply 2 and 5" becomes ["multiply" "2" "and" "5"]
            for word in text_split:
                if word.upper() in operations.keys(): # For each operation mentioned (e.g. "addition")
                    n = findNumbers(text_split) # n is an array that stores the numbers found in the list of words
                    result = operations[word.upper()](n[0], n[1]) # Trigger the corresponding dictionary key, which then triggers it's value (function), passing the numbers as parameters
                    entryField.delete(0, "end")
                    entryField.insert("end", result)
                else:
                    pass
        except:
            pass

root = Tk()
root.title("Smart Scientific Calculator")
root.config(bg="#1c1c26")

# Respectively width, height, distance from y-axis and from x-axis
root.geometry("680x486+100+100")

## CALCULATOR HEADER
# Logo image
logoImg=PhotoImage(file="assets\images\logo.png")
logoLabel=Label(root,
                image=logoImg,
                bg="#1c1c26",
                activebackground="#303040"
                )
logoLabel.grid(row=0, column=0)

entryField=Entry(root,
                 font=("arial", 18, "bold"),
                 justify=CENTER,
                 bg="#1c1c26",
                 fg="white",
                 bd="1",
                 relief=GROOVE,
                 width=30
                )
entryField.grid(row=0, column=0, columnspan=8) # Each of the 8 columns ocupy an equal width

# Microphone image
micImg=PhotoImage(file="assets\images\microphone.png")
micBtn=Label(root,
             image=micImg,
             bg="#1c1c26",
             activebackground="#303040",
             command=audio
             )
micBtn.grid(row=0, column=7)

## BUTTONS FIELD
# Number/operators buttons
btn_values = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
              "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
               "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
              "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
              "0", ".", "%", "=", "log10", "(", ")", "x!"]
row_value = 1
column_value = 0

for i in btn_values:
    btn = Button(root,
                 font=("arial", 15, "bold"),
                 bg="#1c1c26",
                 fg="white",
                 width=5,
                 height=2,
                 bd=1,
                 relief=GROOVE,
                 text=i,
                 activebackground="#303040",
                 # Lambda expressions/forms are used to create anonymous functions
                 command=lambda button=i: click(button) # "button" is the function's argument
                )
    btn.grid(row=row_value, column=column_value)
    column_value+=1 # The buttons on the list are added on the right side of the previous one
    if column_value>7: # Once the row has been filled with buttons, it goes to the beginning of the next row
        row_value+=1
        column_value=0

# Tkinter method which keeps the window on a loop in order for us to see it continuously
root.mainloop()
