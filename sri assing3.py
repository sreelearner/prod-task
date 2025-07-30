import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    print("---------------------")


def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name in contacts:
        print("Leave field blank to keep current value.")
        phone = input(f"New phone number (current: {contacts[name]['phone']}): ").strip()
        email = input(f"New email address (current: {contacts[name]['email']}): ").strip()

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email

        print("Contact updated.")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save & Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
