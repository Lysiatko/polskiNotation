import tkinter as tk
from tkinter import scrolledtext
import spacy

nlp = spacy.load("pl_core_news_sm")

def parse_text():
    input_text = text_input.get('1.0', tk.END)
    doc = nlp(input_text)
    output_text = ""

    for token in doc:
        if token.pos_ == "NOUN":
            prefix = "r"
        elif token.pos_ == "VERB":
            prefix = "c"
        elif token.pos_ == "ADJ":
            prefix = "przym"
        elif token.pos_ == "PRON":
            prefix = "z"
        elif token.pos_ == "ADV":
            prefix = "przys"
        elif token.pos_ == "ADP":
            prefix = "przyi"
        elif token.pos_ == "CONJ":
            prefix = "spój"
        elif token.pos_ == "INTJ":
            prefix = "wykrz"
        elif token.pos_ == "NUM":
            prefix = "licz"
        elif token.pos_ == "PART":
            prefix = "par"
        else:
           prefix = "i"
        output_text += prefix + token.text + " "

    text_output.delete('1.0', tk.END)
    text_output.insert('1.0', output_text)

root = tk.Tk()
root.title("Językonaprawiaczydło")

text_input = scrolledtext.ScrolledText(root, height=10, width=50)
text_input.pack()

convert_button = tk.Button(root, text="Napraw", command=parse_text)
convert_button.pack()

text_output = scrolledtext.ScrolledText(root, height=10, width=50)
text_output.pack()

root.mainloop()
