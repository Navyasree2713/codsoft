# Contact Management System

contacts = {}


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"✅ Contact '{name}' added successfully!\n")


def view_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
        return
    print("\n📒 Contact List:")
    for name, details in contacts.items():
        print(f"➡ {name} - {details['phone']}")
    print()


def search_contact():
    keyword = input("🔍 Enter name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if keyword.lower() in name.lower() or keyword == details["phone"]:
            print("\n✅ Contact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
            found = True
    if not found:
        print("⚠ Contact not found.\n")


def update_contact():
    name = input("Enter the contact name to update: ").strip()
    if name in contacts:
        print("Leave blank if you don’t want to change the field.")
        phone = input("New phone number: ").strip()
        email = input("New email: ").strip()
        address = input("New address: ").strip()

        if phone: contacts[name]["phone"] = phone
        if email: contacts[name]["email"] = email
        if address: contacts[name]["address"] = address

        print(f"✅ Contact '{name}' updated successfully!\n")
    else:
        print("⚠ Contact not found.\n")


def delete_contact():
    name = input("Enter the contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"🗑 Contact '{name}' deleted successfully!\n")
    else:
        print("⚠ Contact not found.\n")


def menu():
    while True:
        print("===== 📞 Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Try again.\n")


# Run program
menu()