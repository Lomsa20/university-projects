from string import digits, ascii_uppercase, ascii_lowercase, punctuation
import tkinter as tk

root = tk.Tk()
root.geometry('350x460')
root.title('Password Strength Checker')
root.resizable(False, False)

# Theme State (False = Light, True = Dark)
is_dark = False

# Color Palettes
themes = {
    'light': {
        'bg': '#f8f9fa', 'fg': '#212529', 'card': '#ffffff',
        'entry_bg': '#ffffff', 'entry_fg': '#212529', 'border': '#ced4da'
    },
    'dark': {
        'bg': '#121212', 'fg': '#e0e0e0', 'card': '#1e1e1e',
        'entry_bg': '#2d2d2d', 'entry_fg': '#ffffff', 'border': '#333333'
    }
}


def toggle_theme():
    global is_dark
    is_dark = not is_dark
    apply_current_theme()


def apply_current_theme():
    t = themes['dark' if is_dark else 'light']
    root.config(bg=t['bg'])

    for widget in root.winfo_children():
        w_type = widget.winfo_class()
        if w_type == 'Frame':
            widget.config(bg=t['card'])
            for sub in widget.winfo_children():
                try:
                    sub.config(bg=t['card'], fg=t['fg'])
                except:
                    pass
        elif w_type in ('Label', 'Checkbutton', 'Button'):
            if widget == theme_btn:
                widget.config(bg=t['entry_bg'], fg=t['fg'])
            elif widget == check_btn:
                widget.config(bg='#007bff', fg='#ffffff')
            else:
                widget.config(bg=t['bg'], fg=t['fg'])

    psw_entry.config(bg=t['entry_bg'], fg=t['entry_fg'], insertbackground=t['fg'])
    theme_btn.config(text="☀️ Light Mode" if is_dark else "🌙 Dark Mode")


# --- UI Layout ---

# Top Bar for Theme Toggle
top_frame = tk.Frame(root)
top_frame.pack(fill='x', padx=15, pady=10)

theme_btn = tk.Button(top_frame, text="🌙 Dark Mode", font=('Segoe UI', 9), command=toggle_theme, relief='flat',
                      cursor='hand2')
theme_btn.pack(side='right')

# Main Container Card
card_frame = tk.Frame(root, bd=1, relief='solid')
card_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))

# Label
tk.Label(card_frame, text='Enter Password', font=('Segoe UI', 11, 'bold')).pack(anchor='w', padx=15, pady=(15, 5))

# Entry
psw_entry = tk.Entry(card_frame, show='*', font=('Segoe UI', 11), relief='solid', bd=1)
psw_entry.pack(fill='x', padx=15, pady=5, ipady=4)
# Note: Live typing trigger removed so the Check button has a distinct purpose!

# Show Password Checkbutton
show_var = tk.BooleanVar()


def show_password():
    if show_var.get():
        psw_entry.config(show='')
    else:
        psw_entry.config(show='*')


tk.Checkbutton(card_frame, text='Show Password', variable=show_var, command=show_password, font=('Segoe UI', 9),
               cursor='hand2').pack(anchor='w', padx=15, pady=5)


# Check Button (Now the primary action trigger)
def strength_of_password():
    psw = psw_entry.get()
    t = themes['dark' if is_dark else 'light']

    if not psw:
        result_label.config(text='⚠️ Please enter a password first!', fg='#ffa502')
        return

    has_digit = any(c in digits for c in psw)
    has_lower = any(c in ascii_lowercase for c in psw)
    has_upper = any(c in ascii_uppercase for c in psw)
    has_symb = any(c in punctuation for c in psw)

    type_counter = sum([has_digit, has_lower, has_upper, has_symb])
    weakness = []

    if len(psw) < 8:
        weakness.append('• Too Short (< 8 chars)')
    if type_counter == 1:
        weakness.append('• Only 1 Character Type')
    if not has_digit:
        weakness.append('• Missing Digit')
    if not has_lower:
        weakness.append('• Missing Lowercase')
    if not has_upper:
        weakness.append('• Missing Uppercase')
    if not has_symb:
        weakness.append('• Missing Symbol')

    if len(psw) < 8 or type_counter == 1:
        strength = 'Weak ❌'
        color = '#ff4d4d'
    elif 8 <= len(psw) < 12 and type_counter >= 2:
        strength = 'Normal ⚠️'
        color = '#ffa502'
    elif len(psw) >= 12 and type_counter == 4:
        strength = 'Strong 🔒'
        color = '#2ed573'
    else:
        strength = 'Normal ⚠️'
        color = '#ffa502'

    if weakness and strength != 'Strong 🔒':
        messages = f"Strength: {strength}\n\nFix Recommendations:\n" + "\n".join(weakness)
    else:
        messages = f"Strength: {strength}\n\n✨ Great Password!"

    result_label.config(text=messages, fg=color)


check_btn = tk.Button(card_frame, text='Check Strength', font=('Segoe UI', 10, 'bold'), command=strength_of_password,
                      relief='flat', cursor='hand2', pady=6)
check_btn.pack(fill='x', padx=15, pady=10)

# Result Label
result_label = tk.Label(card_frame, text='Awaiting analysis...', font=('Segoe UI', 9), justify='left')
result_label.pack(anchor='w', padx=15, pady=10)

# Initialize theme colors on start
apply_current_theme()

root.mainloop()