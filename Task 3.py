import json
import os

# Define the file to store contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    
    contacts[name] = {'Phone': phone, 'Email': email}
    print(f"Contact {name} added successfully.")
    save_contacts(contacts)

# View all contacts
def view_contacts(contacts):
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
    else:
        print("No contacts available.")

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the contact name to edit: ")
    if name in contacts:
        print(f"Editing contact: {name}")
        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email address: ")
        contacts[name] = {'Phone': new_phone, 'Email': new_email}
        print(f"Contact {name} updated successfully.")
        save_contacts(contacts)
    else:
        print(f"Contact {name} not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
        save_contacts(contacts)
    else:
        print(f"Contact {name} not found.")

# Main program menu
def main():
    print("Welcome to the Contact Manager!")
    contacts = load_contacts()

    while True:
        print("\nMenu:")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the program
if __name__ == "__main__":
    main()