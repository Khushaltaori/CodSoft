# Simple Contact Book Application

# List to store contact dictionaries
contacts = []

# Add a new contact
def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(" Contact added!")

# View all contacts
def view_contacts():
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts to show.")
        return
    for index, c in enumerate(contacts, 1):
        print(f"{index}. {c['name']} - {c['phone']}")

# Search contact by name or phone
def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name or phone to search: ").lower()
    for c in contacts:
        if query in c['name'].lower() or query in c['phone']:
            print("\n🔍 Contact Found:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            return
    print(" Contact not found.")

# Update existing contact
def update_contact():
    print("\n--- Update Contact ---")
    query = input("Enter name or phone to update: ").lower()
    for c in contacts:
        if query in c['name'].lower() or query in c['phone']:
            print("Leave field blank to keep unchanged.")
            c['name'] = input("New Name: ") or c['name']
            c['phone'] = input("New Phone: ") or c['phone']
            c['email'] = input("New Email: ") or c['email']
            c['address'] = input("New Address: ") or c['address']
            print(" Contact updated!")
            return
    print(" Contact not found.")

# Delete a contact
def delete_contact():
    print("\n--- Delete Contact ---")
    query = input("Enter name or phone to delete: ").lower()
    for i, c in enumerate(contacts):
        if query in c['name'].lower() or query in c['phone']:
            confirm = input(f"Are you sure you want to delete {c['name']}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(i)
                print(" Contact deleted.")
            return
    print("Contact not found.")

# Show menu and get user choice
def main_menu():
    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the app
main_menu()
