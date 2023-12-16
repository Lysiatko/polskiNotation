import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import spacy
import threading

nlp = spacy.load("pl_core_news_sm")

def parse_text():
    try:
        input_text = text_input.get('1.0', tk.END)
        doc = nlp(input_text)
        output_text = ""

        for token in doc:
            prefix_dict = {
                "NOUN": "r", "VERB": "c", "ADJ": "przym", 
                "PRON": "z", "ADV": "przys", "ADP": "przyi", 
                "CONJ": "s", "INTJ": "w", "NUM": "l", 
                "PART": "par"
            }
            prefix = prefix_dict.get(token.pos_, "i")
            output_text += prefix + token.text + " "

        text_output.delete('1.0', tk.END)
        text_output.insert('1.0', output_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_text_change(event=None):
    threading.Thread(target=parse_text, daemon=True).start()

def load_text():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_input.delete('1.0', tk.END)
            text_input.insert('1.0', file.read())

def save_text():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_output.get('1.0', tk.END))

root = tk.Tk()
root.title("językonaprawiaczydło 2.0")

frame_input = tk.Frame(root)
frame_input.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
frame_output = tk.Frame(root)
frame_output.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

text_input = scrolledtext.ScrolledText(frame_input, height=10, width=50)
text_input.pack(expand=True, fill='both')
text_input.bind("<KeyRelease>", on_text_change)

text_output = scrolledtext.ScrolledText(frame_output, height=10, width=50)
text_output.pack(expand=True, fill='both')

# Menu for extra features
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Load Text", command=load_text)
file_menu.add_command(label="Save Output", command=save_text)
menu_bar.add_cascade(label="File", menu=file_menu)

# Start the GUI loop
root.mainloop()
