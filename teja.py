import tkinter as tk
from tkinter import messagebox


def create_widgets(self):
    title_label = tk.Label(self,text="PHONEBOOK APPLICATION",bg="#333",fg="white",font=("Arial",18))
    title.label.pack(fill=tk.X)
                           
def add_contact():
    name = entry_name.get()
    number = entry_number.get()
    
    if name and number:
        contacts[name] = number
        update_contact_list()
        messagebox.showinfo("Success", f"Contact '{name}' added successfully! 🤐")
    else:
        messagebox.showerror("Error", "Please enter both agent name and number.")

def display_contacts():
    if contacts:
        for name, number in contacts.items():
            text.insert(tk.END, f"Contact Name: {name}, Contact Number: {number}\n")
    else:
        text.insert(tk.END, "No agents available.")

def update_contact_list():
    text.delete(1.0, tk.END)
    display_contacts()

def secret_feature():
    messagebox.showinfo("Top-Secret Feature", "You've activated the Top-Secret feature! 🕶️🚁")

def covert_operation():
    messagebox.showinfo("Covert Operation", "Covert operation initiated. Stay vigilant! 🌐🕵️")

# Create a Tkinter window
root = tk.Tk()
root.title("Classified Phonebook App 🕵️‍♀️")

# Set background color
root.configure(bg='#333333')

# Create a dictionary to store contacts
contacts = {}

# Create GUI elements with custom colors
label_name = tk.Label(root, text="Contact Name:", fg="white", bg="#333333")
label_name.pack()

entry_name = tk.Entry(root, bg="#666666", fg="white")
entry_name.pack()

label_number = tk.Label(root, text="Contact Number:", fg="white", bg="#333333")
label_number.pack()

entry_number = tk.Entry(root, bg="#666666", fg="white")
entry_number.pack()

button_add = tk.Button(root, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white")
button_add.pack()

button_display = tk.Button(root, text="Display Contact", command=display_contacts, bg="#2196F3", fg="white")
button_display.pack()

button_secret = tk.Button(root, text="Activate Top-Secret Feature", command=secret_feature, bg="#FFD700", fg="black")
button_secret.pack()

button_covert = tk.Button(root, text="Covert Operation", command=covert_operation, bg="#FF4500", fg="white")
button_covert.pack()

text = tk.Text(root, height=10, width=40, bg="#333333", fg="white")
text.pack()

# Start the GUI application
root.mainloop()


