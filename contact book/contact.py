import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root, width=40)
        self.name_entry.pack()

        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root, width=40)
        self.phone_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root, width=40)
        self.email_entry.pack()

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(root, width=40)
        self.address_entry.pack()

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.pack()
        self.search_entry = tk.Entry(root, width=40)
        self.search_entry.pack()

        self.search_button = tk.Button(root, text="Search", command=self.search_contacts)
        self.search_button.pack()

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

        self.contacts_listbox = tk.Listbox(root, width=80)
        self.contacts_listbox.pack()


    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone_number:
            self.contacts.append({"Name": name, "Phone Number": phone_number, "Email": email, "Address": address})
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone Number are required fields.")

    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"Name: {contact['Name']}, Phone Number: {contact['Phone Number']}, Email: {contact['Email']}, Address:{contact['Address']} " )

    def search_contacts(self):
        search_term = self.search_entry.get().lower()
        self.contacts_listbox.delete(0, tk.END)

        for contact in self.contacts:
            if search_term in contact['Name'].lower() or search_term in contact['Phone Number']:
                self.contacts_listbox.insert(tk.END, f"Name: {contact['Name']}, Phone Number: {contact['Phone Number']}")

    def update_contact(self):
        index = self.contacts_listbox.curselection()
        if index:
            index = index[0]  # Get the index of the selected contact
            selected_contact = self.contacts[index]  # Retrieve the selected contact details

            name = self.name_entry.get()
            phone_number = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            # Update the selected contact's details if the corresponding entry fields are not empty
            selected_contact['Name'] = name if name else selected_contact['Name']
            selected_contact['Phone Number'] = phone_number if phone_number else selected_contact['Phone Number']
            selected_contact['Email'] = email if email else selected_contact['Email']
            selected_contact['Address'] = address if address else selected_contact['Address']

            # Update the contacts list in the specific index
            self.contacts[index] = selected_contact

            # Clear entry fields and show info message
            self.clear_entries()
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        index = self.contacts_listbox.curselection()
        if index:
            index = index[0]
            deleted_contact = self.contacts.pop(index)
            self.clear_entries()
            messagebox.showinfo("Success", f"Contact for {deleted_contact['Name']} deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Book")
    app = ContactBookApp(root)
    root.mainloop()