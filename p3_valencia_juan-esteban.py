import csv


contactlist=[("Beyonce Knowles", "bey", "561-1234321"), ("Cardi B",
"Belcalis", "305-4399521"), ("Earl Simmons", "DMX", "305-1010101")]



def add_contact(name,nickname,number):
    newcontact=(name,nickname,number)
    for contact in contactlist:
        if name in contact:
            contact = (newcontact)
            return False
        else:
            contactlist.append(newcontact)
            return True
        

def remove_contact(contactname):
    for contact in contactlist:
        if contactname in  contact:
            contactlist.pop(contactlist.index(contact))


def find_contact(str,searchby="name"):
    for contact in contactlist:
        if searchby == "name" and str in contact:
            return contact
        elif searchby == "nickname" and str in contact:
            return contact
    return None
        
def savetoCSV(contactlist):
    f1 =open("contactlist.csv",mode="w",newline="")
    writer= csv.writer(f1)
    for contact in contactlist:
        writer.writerow(contact)

def readCSVcontactlist(CSVname):
    contactlist = []
    CSV= open(CSVname,"r")
    data=csv.reader(CSV)
    for contact in data:
        contactlist.append(tuple(contact))
    return(sorted(contactlist))



def main():
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
    remove_contact("Cardi B")
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
