import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        # Frame for the contact list
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contact_listbox = tk.Listbox(self.list_frame, yscrollcommand=self.scrollbar.set, width=40, height=20)
        self.contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.config(command=self.contact_listbox.yview)

        self.contact_listbox.bind('<Double-1>', self.view_contact)

        # Frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.pack(fill=tk.X, pady=5)

        self.view_button = tk.Button(self.button_frame, text="View Contact", command=self.view_contact)
        self.view_button.pack(fill=tk.X, pady=5)

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact)
        self.search_button.pack(fill=tk.X, pady=5)

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact)
        self.update_button.pack(fill=tk.X, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(fill=tk.X, pady=5)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.root.quit)
        self.quit_button.pack(fill=tk.X, pady=5)

    def add_contact(self):
        new_contact = self.get_contact_details()
        if new_contact:
            self.contacts.append(new_contact)
            self.update_contact_list()

    def view_contact(self, event=None):
        selected_contact = self.get_selected_contact()
        if selected_contact:
            messagebox.showinfo("Contact Details", self.format_contact(selected_contact))

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts if search_term in contact['name'] or search_term in contact['phone']]
            self.show_search_results(results)

    def update_contact(self):
        selected_contact = self.get_selected_contact()
        if selected_contact:
            updated_contact = self.get_contact_details(selected_contact)
            if updated_contact:
                self.contacts[self.contacts.index(selected_contact)] = updated_contact
                self.update_contact_list()

    def delete_contact(self):
        selected_contact = self.get_selected_contact()
        if selected_contact and messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {selected_contact['name']}?"):
            self.contacts.remove(selected_contact)
            self.update_contact_list()

    def get_contact_details(self, contact=None):
        name = simpledialog.askstring("Contact Name", "Enter name:", initialvalue=contact['name'] if contact else "")
        if not name:
            return None

        phone = simpledialog.askstring("Phone Number", "Enter phone number:", initialvalue=contact['phone'] if contact else "")
        email = simpledialog.askstring("Email", "Enter email:", initialvalue=contact['email'] if contact else "")
        address = simpledialog.askstring("Address", "Enter address:", initialvalue=contact['address'] if contact else "")

        return {'name': name, 'phone': phone, 'email': email, 'address': address}

    def get_selected_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            return self.contacts[selected_index]
        except IndexError:
            messagebox.showwarning("Select Contact", "Please select a contact from the list.")
            return None

    def format_contact(self, contact):
        return f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"

    def show_search_results(self, results):
        result_window = tk.Toplevel(self.root)
        result_window.title("Search Results")

        result_listbox = tk.Listbox(result_window, width=50, height=20)
        result_listbox.pack(padx=10, pady=10)

        for contact in results:
            result_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
