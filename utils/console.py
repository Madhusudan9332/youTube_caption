import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import sys


class ConsoleWindow:
    def __init__(self, title="Console Output"):
        self.root = tk.Toplevel()
        self.root.title(title)
        self.root.geometry("600x400")

        self.text_widget = ScrolledText(self.root, wrap=tk.WORD, font=("Courier", 10))
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Redirect stdout and stderr
        sys.stdout = self
        sys.stderr = self

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)  # Auto-scroll to the bottom

    def flush(self):
        pass  # Required for compatibility with stdout and stderr

    def close(self):
        # Restore stdout and stderr when closing
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        self.root.destroy()
