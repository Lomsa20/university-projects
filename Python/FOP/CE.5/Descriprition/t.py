import tkinter as tk

# buttons
button_values = [ #5 row, 4 column
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

# basic symbols
right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

# counts of rows and columns
row_count = len(button_values) # 5
column_count = len(button_values[0]) # 4

# colors
color_dark_cyan = '#77A4BD'
color_light_grey = '#ADADAD'
color_yellow = '#F5B027'
color_black = '#180501'
color_white = 'white'

# window setup
window = tk.Tk() #create window
window.title('Calculator')
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text='0', font = ('Arial', 45, 'bold'),
                 background=color_black, foreground=color_white, anchor = 'e', width= column_count) # e means east

label.grid(row = 0, column = 0, columnspan = column_count, sticky = 'we') # sticky 'we' stretch from west to  east

for row in range(0, row_count):
    for column in range(0, column_count):
        value = button_values[row][column]
        button = tk.Button(frame, text = value, font=('Arial', 30, 'bold'),
                           width = column_count-1, height = 1,
                           command = lambda value = value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground = color_black, background = color_dark_cyan)
        elif value in right_symbols:
            button.config(foreground = color_white, background = color_yellow)
        else:
            button.config(foreground = color_white, background = color_light_grey)

        button.grid(row=row+1, column=column)

frame.pack()

# A+B, A-B, A*B, A/B
A = '0'
operator = None
B = None
def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)
def clear_all():
    global operator, A, B
    A = '0'
    B = None
    operator = None
def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator
    # this gives access to outer variables and give a global value

    if value in right_symbols:
        if value == '=':
            if A is not None and operator is not None:
                B = label['text']
                numA = float(A)
                numB = float(B)

                if operator == '+':
                    label['text'] = remove_zero_decimal(numA + numB)
                elif operator == '-':
                    label['text'] = remove_zero_decimal(numA - numB)
                elif operator == '×':
                    label['text'] = remove_zero_decimal(numA * numB)
                elif operator == '÷':
                    label['text'] = remove_zero_decimal(numA / numB)

                clear_all()
                # we update operator so we don't need A operator and b anymore and reset them with default state

        elif value in  "+-×÷":
            if operator is None:
                A = label['text']
                label['text'] = '0'
                B = '0'
            operator = value
         # if operator is None we will get the label and save it
         # to A and update it to zero
         # if there is 100 + and then * it will change + to *
    elif value in top_symbols:
        if value == 'AC':
            clear_all()
            label['text'] = '0' #removes everything and return 0
        elif value == '+/-':
            result = float(label['text']) * -1# if int we might lose any potential decimal places
            label['text'] = remove_zero_decimal(result)
        elif value == '%':
            result = float(label['text']) / 100 # convert into percentage
            label['text'] = remove_zero_decimal(result)
    else: # digits or any others
        if value == '.':
            if value not in label['text']:
                label['text'] += value
        elif value == "√":
            num = float(label['text'])
            if num < 0:
                label['text'] = "Error"
                clear_all()
            else:
                label['text'] = remove_zero_decimal(num ** 0.5)
        elif value in '0123456789':
            if label['text'] == '0':
                label['text'] = value # replace 0 for example if 05 it will be converted as 5
            else:
                label['text'] += value #append digits


#center window
window.update() # update window with the new size dimensions

window_width = window.winfo_width() # width of tkinter window
window_height = window.winfo_height() # height of tkinter window

screen_width = window.winfo_screenwidth() # width of screen
screen_height = window.winfo_screenheight() # width of screen

window_x = int(screen_width / 2 - window_width / 2)
    # screen_width / 2 center of screen
    # window_width / 2   half of window
window_y = int(screen_height / 2 - window_height / 2)

# format '(w)*(h)+(x)*(y)'
window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

window.mainloop()