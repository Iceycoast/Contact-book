import json

class Contact:
    def __init__(self, name, phoneno, email):
        self.name = name.strip()
        self.phoneno = phoneno.strip()
        self.email = email.strip()

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phoneno,
            "email": self.email
        }

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename

    def view_all_contacts(self):
        try:
            with open(self.filename, 'r') as f:
                contacts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return "No contacts found."

        if not contacts:
            return "No contacts found."

        result = ""
        for contact in contacts:
            result += f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n\n"
        return result

    def add_contact(self, name, phoneno, email):
        contact = Contact(name, phoneno, email).to_dict() #making a dict of the object

        try:
            with open(self.filename, 'r') as f:
                contacts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            contacts = []

        contacts.append(contact) #the object is appended in the list
        with open(self.filename, 'w') as f:
            json.dump(contacts, f, indent=4)
        return f"\nContact '{contact['name']}' added successfully."

    def search_contact(self, name_to_search):
        name_to_search = name_to_search.strip().lower()

        try:
            with open(self.filename, 'r') as f:
                contacts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return "\nNo Contacts Found."

        for contact in contacts:
            if contact["name"].lower() == name_to_search:
                return (f"\nContact Found\n\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n")

        return "\nContact not found."

    def delete_contact(self, name_to_delete):
        name_to_delete = name_to_delete.strip().lower()

        try:
            with open(self.filename, 'r') as f:
                contacts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return "No contacts to delete."

        updated_contacts = [c for c in contacts if c['name'].lower() != name_to_delete]

        if len(updated_contacts) == len(contacts):
            return "Contact not found."

        with open(self.filename, 'w') as f:
            json.dump(updated_contacts, f, indent=4)
        return f"Contact '{name_to_delete}' deleted successfully."

def run():
    user = ContactBook()
    while True:
        print("\n📒 Welcome to Contact Book")
        print("1. View All Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print("\nALL CONTACTS\n")
            print(user.view_all_contacts())

        elif choice == "2":
            name = input("\nEnter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            print(user.add_contact(name, phone, email))

        elif choice == "3":
            name = input("\nEnter Name to Search: ")
            print(user.search_contact(name))

        elif choice == "4":
            name = input("\nEnter Name to Delete: ")
            print(user.delete_contact(name))

        elif choice == "5":
            print("\nExiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
