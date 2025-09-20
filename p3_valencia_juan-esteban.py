import csv

contactlist = [
    ("Beyonce Knowles", "bey", "561-1234321"),
    ("Cardi B", "Belcalis", "305-4399521"),
    ("Earl Simmons", "DMX", "305-1010101")
]

def add_contact(name, nickname, number):
    """
    Adds a new contact to the contact list.
    Returns True if added, False if contact with same name exists.
    """
    newcontact = (name, nickname, number)
    for contact in contactlist:
        if name == contact[0]:
            return False
    contactlist.append(newcontact)
    return True

def remove_contact(contactname):
    """
    Removes a contact from the contact list by name.
    """
    try:
        for contact in contactlist:
            if contactname == contact[0]:
                contactlist.pop(contactlist.index(contact))
                return True
        return False
    except Exception as e:
        print(f"Error removing contact: {e}")
        return False

def find_contact(str, searchby="name"):
    """
    Finds and returns a contact by name or nickname.
    Returns None if not found.
    """
    try:
        for contact in contactlist:
            if searchby == "name" and str == contact[0]:
                return contact
            elif searchby == "nickname" and str == contact[1]:
                return contact
        return None
    except Exception as e:
        print(f"Error finding contact: {e}")
        return None

def savetoCSV(contactlist):
    """
    Saves the contact list to a CSV file named 'contactlist.csv'.
    """
    try:
        with open("contactlist.csv", mode="w", newline="") as f1:
            writer = csv.writer(f1)
            for contact in contactlist:
                writer.writerow(contact)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def readCSVcontactlist(CSVname):
    """
    Reads contacts from a CSV file and returns a sorted list of contacts.
    """
    contactlist = []
    try:
        with open(CSVname, "r") as CSV:
            data = csv.reader(CSV)
            for contact in data:
                contactlist.append(tuple(contact))
        return sorted(contactlist)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

def main():
    """
    Main function to test contact list operations.
    """
    print("Initial contact list:", contactlist)

    # Test add_contact
    print("\nAdding new contact...")
    result = add_contact("Alicia Keys", "Alicia", "212-5551234")
    print("Add contact result:", result)
    print("Contact list after adding:", contactlist)

    print("\nTrying to add existing contact...")
    result = add_contact("Beyonce Knowles", "QueenB", "561-9999999")
    print("Add contact result:", result)
    print("Contact list after trying to add existing:", contactlist)

    # Test remove_contact
    print("\nRemoving contact 'Cardi B'...")
    remove_result = remove_contact("Cardi B")
    print("Remove contact result:", remove_result)
    print("Contact list after removal:", contactlist)

    # Test find_contact
    print("\nFinding contact by name 'Earl Simmons'...")
    found = find_contact("Earl Simmons", searchby="name")
    print("Found:", found)

    print("\nFinding contact by nickname 'Alicia'...")
    found = find_contact("Alicia", searchby="nickname")
    print("Found:", found)

    print("\nFinding non-existent contact...")
    found = find_contact("Non Existent", searchby="name")
    print("Found:", found)

    # Test savetoCSV
    print("\nSaving contact list to CSV...")
    savetoCSV(contactlist)
    print("Saved to contactlist.csv")

    # Test readCSVcontactlist
    print("\nReading contact list from CSV...")
    loaded_contacts = readCSVcontactlist("contactlist.csv")
    print("Loaded contacts:", loaded_contacts)

if __name__ == "__main__":
    main()

savetoCSV(contactlist)
