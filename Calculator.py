import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("600x600")
        self.root.configure(bg="#2E2E2E")  # Dark background
        self.expression = ""

        # Entry Field
        self.entry = ttk.Entry(root, font=("Arial", 20), justify='right')
        self.entry.grid(row=0, column=0, columnspan=6, ipadx=8, ipady=8, pady=10)
        
        # Buttons Layout
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('C', '(', ')', 'sqrt'),
            ('sin', 'cos', 'tan', 'log'),
            ('exp', 'pow', 'mod', 'abs')
        ]
        
        button_styles = {
            "bg": "#4F4F4F", "fg": "#FFFFFF", "font": ("Arial", 14), "width": 10, "relief": "raised"
        }
        
        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                btn = tk.Button(root, text=button, command=lambda b=button: self.on_button_click(b), **button_styles)
                btn.grid(row=i+1, column=j, pady=5, padx=5)
    
    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
        elif button == "=":
            self.calculate_result()
        elif button == "sqrt":
            self.expression += "math.sqrt("  # Function
        elif button in {"sin", "cos", "tan", "log", "exp", "pow", "mod", "abs"}:
            self.expression += f"math.{button}("  # Function call
        else:
            self.expression += button
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
    
    def calculate_result(self):
        try:
            result = eval(self.expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.expression = str(result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
