from string import digits, ascii_uppercase, ascii_lowercase,punctuation
import tkinter as tk


root = tk.Tk()
root.geometry('300x300')
# Label
tk.Label(root, text = 'Password', bg = 'white').pack()
# Entry
psw_entry = tk.Entry(root, show = '*')
psw_entry.pack()
# Result Label
result_label = tk.Label(root, text = '')
result_label.pack(pady =10)
show_var = tk.BooleanVar() #checks show button
def show_password():

    if show_var.get():
        psw_entry.config(show = '')
    else:
        psw_entry.config(show = '*')
tk.Checkbutton(root, text = 'Show Password', variable = show_var, command= show_password).pack()

def strength_of_password():
    psw = psw_entry.get()
    has_digit = any(c in digits for c in psw)
    has_lower = any(c in ascii_lowercase for c in psw)
    has_upper = any(c in ascii_uppercase for c in psw)
    has_symb = any(c in punctuation for c in psw)

    type_counter = sum([has_digit, has_lower, has_upper, has_symb])

    weakness = []

    """--- Weaknesses ---"""
    if len(psw) < 8:
        weakness.append('Too Short!')
    if type_counter == 1:
        weakness.append('Only 1 Type Character ')
    if not has_digit:
        weakness.append('No Digit!')
    if not has_lower:
        weakness.append('No Lower Case!')
    if not has_upper:
        weakness.append('No Upper Case!')
    if not has_symb:
        weakness.append('No Symbol!')

    """---Verification---"""
    if len(psw) < 8 or type_counter == 1:
        strength = 'weak'
        color = 'red'
    elif 8 <= len(psw) < 12 and type_counter >= 2:
        strength = 'Normal'
        color = 'orange'
    elif len(psw) >= 12 and type_counter == 4:
        strength = 'Strong'
        color = 'green'
    else:
        strength = 'Normal'
        color = 'orange'
    if weakness and strength != 'Strong':
        messages = strength +'\nFix' + ','.join(weakness)
    else:
        messages = strength  + "\nGreat Password"
    result_label.config(text = messages, fg = color)
tk.Button(root, text = 'check', command = strength_of_password).pack()
root.mainloop()