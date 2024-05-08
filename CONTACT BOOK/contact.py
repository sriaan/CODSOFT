class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

    def view_contact_list(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("Contact book is empty.")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                results.append(contact)
        if results:
            print("Search results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
                print(f"Contact {name} updated successfully.")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.view_contact_list()
        elif choice == '3':
            query = input("Enter contact name or phone number to search: ")
            contact_book.search_contact(query)
        elif choice == '4':
            name = input("Enter contact name to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == '5':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
