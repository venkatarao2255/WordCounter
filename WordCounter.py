import tkinter as tk

# Fullscreen window
window = tk.Tk()
window.geometry("%dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))
window.title("Full-Screen Word Counter")

# Word count function
def count_words():
    input_text = text_entry.get("1.0", "end-1c")
    words = input_text.split()
    word_count = len(words)
    result_label.config(text=f"Word count: {word_count}")

# Error handling function
def handle_input():
    input_text = text_entry.get("1.0", "end-1c")
    if len(input_text) == 0:
        result_label.config(text="Error: Please enter a sentence or paragraph.")
    else:
        count_words()

# Create input and output boxes
input_frame = tk.Frame(window, bg="white", borderwidth=2, relief="solid")
input_frame.pack(pady=20)
text_entry = tk.Text(input_frame, height=10, width=50, font=("Arial", 16))
text_entry.pack(side="left", padx=10)

# Create a separate frame for the button
button_frame = tk.Frame(window)
button_frame.pack()

compute_button = tk.Button(button_frame, text="Compute", bg="blue", fg="white", font=("Arial", 16), command=handle_input)
compute_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 16), fg="blue")
result_label.pack(pady=20)

# Animations
def blink_label():
    result_label.config(fg="red")
    window.after(500, lambda: result_label.config(fg="blue"))

window.after(0, blink_label)

# Start the Tkinter event loop
window.mainloop()
