import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from utils.console import ConsoleWindow
from datetime import datetime
import threading
import time
import os

# Simulated process for demonstration
def simulate_long_process():
    for i in range(1, 11):
        print(f"Processing item {i}...")
        time.sleep(1)
    print("Process completed!")


# Global variables
input_file = None
append_file = None


def browse_input_file():
    """Browse and select an input file."""
    input_file_type = input_type_var.get()
    filetypes = [("Excel Files", "*.xlsx")] if input_file_type == "xlsx" else [("CSV Files", "*.csv")]

    input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=filetypes)

    if input_file_path:
        global input_file
        input_file = input_file_path
        file_label.config(text=f"Selected File: {os.path.basename(input_file)}")


def browse_append_file():
    """Browse and select an append file."""
    output_file_type = output_type_var.get()
    filetypes = [("Excel Files", "*.xlsx")] if output_file_type == "xlsx" else [("CSV Files", "*.csv")]

    append_file_path = filedialog.askopenfilename(title="Select Append File", filetypes=filetypes)

    if append_file_path:
        global append_file
        append_file = append_file_path
        append_label.config(text=f"Append File: {os.path.basename(append_file)}")


def start_process():
    """Start the main processing logic."""
    # Start the process in a separate thread to avoid freezing the GUI
    print("Starting the process...")
    threading.Thread(target=simulate_long_process).start()


def stop_process():
    """Stop the ongoing process."""
    print("Stopping the process...")
    # You can implement additional logic here to stop threads/processes


def main():
    global input_file, file_label, append_label, input_type_var, output_type_var, pause_button

    # Create the main GUI window
    root = tk.Tk()
    root.title("YouTube Transcript Downloader")
    root.geometry("600x500")

    # Input File Type Selection
    tk.Label(root, text="Select Input File Type:", font=("Arial", 12)).pack(pady=10)
    input_type_var = tk.StringVar(value="xlsx")
    ttk.Combobox(root, textvariable=input_type_var, values=["xlsx", "csv"], state="readonly").pack(pady=5)

    # Output File Format Selection
    tk.Label(root, text="Select Output File Format:", font=("Arial", 12)).pack(pady=10)
    output_type_var = tk.StringVar(value="xlsx")
    ttk.Combobox(root, textvariable=output_type_var, values=["xlsx", "csv"], state="readonly").pack(pady=5)

    # Input and Append File Selection
    file_frame = tk.Frame(root)
    file_frame.pack(pady=10)

    tk.Button(file_frame, text="Browse Input File", command=browse_input_file, font=("Arial", 12), bg="blue", fg="white").grid(row=0, column=0, padx=5)
    tk.Button(file_frame, text="Append Output File", command=browse_append_file, font=("Arial", 12), bg="purple", fg="white").grid(row=0, column=1, padx=5)

    file_label = tk.Label(root, text="No file selected", font=("Arial", 10))
    file_label.pack(pady=5)

    append_label = tk.Label(root, text="No append file selected", font=("Arial", 10))
    append_label.pack(pady=5)

    # Buttons for Start, Pause, and Stop
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Start Button
    tk.Button(button_frame, text="Start Process", command=start_process, font=("Arial", 12), bg="green", fg="white").grid(row=0, column=0, padx=5)

    # Stop Button
    tk.Button(button_frame, text="Stop", command=stop_process, font=("Arial", 12), bg="red", fg="white").grid(row=0, column=1, padx=5)

    # Console Button
    tk.Button(root, text="Open Console", font=("Arial", 12), bg="gray", fg="white", command=ConsoleWindow).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
