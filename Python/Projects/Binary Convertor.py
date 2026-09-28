import tkinter as tk
from tkinter import messagebox

# Your original colors
light_blue = "#B3D1ED"
red = '#B20700'
pink = '#FACCCF'
yellow = '#FBEDA4'
dark_text = '#222222'


def text_to_binary(text):
    try:
        return ' '.join(format(ord(c), '08b') for c in text)
    except Exception:
        return ''


def binary_to_text(binary_text):
    try:
        binary_values = binary_text.strip().split()
        return ''.join(chr(int(b, 2)) for b in binary_values)
    except Exception:
        return "⚠️ Invalid Binary input (use spaces between 8-bit bytes)"


class BinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Text ⇄ Binary Code Studio')
        self.root.geometry('550x525')
        self.root.resizable(False, False)
        self.root.configure(background=yellow)

        self.create_widgets()
        self.center_window()

    def create_widgets(self):
        # Main Container Frame
        main_frame = tk.Frame(self.root, bg=yellow)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Title Header
        title_label = tk.Label(main_frame, text="⚡ Text & Binary Converter", font=('Segoe UI', 15, 'bold'),
                               bg=yellow, fg=dark_text)
        title_label.pack(anchor='w', pady=(0, 10))

        # --- INPUT SECTION ---
        tk.Label(main_frame, text="Input Text / Binary:", font=('Segoe UI', 10, 'bold'),
                 bg=yellow, fg=dark_text).pack(anchor='w', pady=(5, 2))

        self.input_text = tk.Text(main_frame, font=('Consolas', 11), bg=pink, fg=dark_text,
                                  insertbackground=dark_text, relief='solid', bd=1, height=5, wrap='word')
        self.input_text.pack(fill='x', pady=(0, 10))
        self.input_text.bind("<KeyRelease>", self.auto_convert)

        # --- BUTTON CONTROLS ---
        btn_frame = tk.Frame(main_frame, bg=yellow)
        btn_frame.pack(fill='x', pady=5)

        t2b_btn = tk.Button(btn_frame, text="Text ➔ Binary", font=('Segoe UI', 9, 'bold'),
                            bg=light_blue, fg=dark_text, relief='raised', cursor='hand2',
                            padx=12, pady=6, command=self.do_text_to_binary)
        t2b_btn.pack(side='left', padx=(0, 8))

        b2t_btn = tk.Button(btn_frame, text="Binary ➔ Text", font=('Segoe UI', 9, 'bold'),
                            bg=light_blue, fg=dark_text, relief='raised', cursor='hand2',
                            padx=12, pady=6, command=self.do_binary_to_text)
        b2t_btn.pack(side='left', padx=(0, 8))

        clear_btn = tk.Button(btn_frame, text="Clear", font=('Segoe UI', 9, 'bold'),
                              bg=pink, fg=red, relief='raised', cursor='hand2',
                              padx=12, pady=6, command=self.clear_all)
        clear_btn.pack(side='right')

        # --- OUTPUT SECTION ---
        output_header_frame = tk.Frame(main_frame, bg=yellow)
        output_header_frame.pack(fill='x', pady=(15, 2))

        tk.Label(output_header_frame, text="Conversion Output:", font=('Segoe UI', 10, 'bold'),
                 bg=yellow, fg=dark_text).pack(side='left')

        copy_btn = tk.Button(output_header_frame, text="📋 Copy Output", font=('Segoe UI', 8, 'bold'),
                             bg=light_blue, fg=dark_text, relief='raised', cursor='hand2',
                             command=self.copy_to_clipboard)
        copy_btn.pack(side='right')

        self.output_text = tk.Text(main_frame, font=('Consolas', 11), bg=pink, fg=dark_text,
                                   insertbackground=dark_text, relief='solid', bd=1, height=5, wrap='word')
        self.output_text.pack(fill='x', pady=(0, 5))
        self.output_text.config(state='disabled')  # Read-only by default

    def do_text_to_binary(self):
        content = self.input_text.get("1.0", "end-1c")
        result = text_to_binary(content)
        self.set_output(result)

    def do_binary_to_text(self):
        content = self.input_text.get("1.0", "end-1c")
        result = binary_to_text(content)
        self.set_output(result)

    def auto_convert(self, event=None):
        content = self.input_text.get("1.0", "end-1c").strip()
        if not content:
            self.set_output("")
            return

        if all(c in '01 ' for c in content):
            result = binary_to_text(content)
        else:
            result = text_to_binary(content)
        self.set_output(result)

    def set_output(self, text):
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", text)
        self.output_text.config(state='disabled')

    def clear_all(self):
        self.input_text.delete("1.0", "end")
        self.set_output("")

    def copy_to_clipboard(self):
        output_content = self.output_text.get("1.0", "end-1c")
        if output_content:
            self.root.clipboard_clear()
            self.root.clipboard_append(output_content)
            messagebox.showinfo("Success", "Output copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No output to copy!")

    def center_window(self):
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = int((sw / 2) - (w / 2))
        y = int((sh / 2) - (h / 2))
        self.root.geometry(f'{w}x{h}+{x}+{y}')


if __name__ == '__main__':
    root = tk.Tk()
    app = BinaryConverterApp(root)
    root.mainloop()