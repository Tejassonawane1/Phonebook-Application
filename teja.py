import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Phonebook - Contact Management System")
        self.root.configure(bg="lightblue")  # Set the background color for the entire window
        self.contacts = []

        # Color configurations
        bg_color = "salmon"
        label_color = "black"
        button_bg_color = "black"
        button_fg_color = "white"
        headline_color = "black"

        # Font configurations
        headline_font = ("Algerian", 46, "bold")  # Use Algerian font for the headline
        label_font = ("Helvetica", 22)
        button_font = ("Helvetica", 22, "bold")
        entry_font = ("Helvetica", 22)  # Increased font size for user input to 22
        contacts_text_font = ("Helvetica", 22)  # Increased font size for display contact textbox to 22

        # GUI Components
        self.headline_label = tk.Label(root, text="PHONEBOOK", font=headline_font, bg=bg_color, fg=headline_color)
        self.name_label = tk.Label(root, text="Name:", font=label_font, bg=bg_color, fg=label_color)
        self.name_entry = tk.Entry(root, font=entry_font)

        self.phone_label = tk.Label(root, text="Phone:", font=label_font, bg=bg_color, fg=label_color)
        self.phone_entry = tk.Entry(root, font=entry_font)

        self.email_label = tk.Label(root, text="Email:", font=label_font, bg=bg_color, fg=label_color)
        self.email_entry = tk.Entry(root, font=entry_font)

        # Increased button size with font specifications
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, bg=button_bg_color, fg=button_fg_color, height=2, width=20, font=button_font)

        # Text widget for displaying contacts with increased font size
        self.contacts_text = tk.Text(root, height=10, width=40, wrap=tk.WORD, font=contacts_text_font)
        self.display_button = tk.Button(root, text="Display Contacts", command=self.display_contacts, bg=button_bg_color, fg=button_fg_color, height=2, width=20, font=button_font)

        # Grid Layout
        self.headline_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        self.phone_label.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

        self.email_label.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        self.email_entry.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        self.contacts_text.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")
        self.display_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

        # Configure rows and columns to expand and fill available space
        for i in range(7):  # Number of rows
            self.root.rowconfigure(i, weight=1)

        for i in range(2):  # Number of columns
            self.root.columnconfigure(i, weight=1)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            contact_info = f"Name: {name}\nPhone: {phone}\nEmail: {email}"
            self.contacts.append(contact_info)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill in all the fields.")

    def display_contacts(self):
        self.contacts_text.delete(1.0, tk.END)  # Clear the existing content

        if not self.contacts:
            self.contacts_text.insert(tk.END, "No contacts available.")
        else:
            for contact_info in self.contacts:
                self.contacts_text.insert(tk.END, contact_info + "\n\n")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
