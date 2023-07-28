



class Phonebook:
    contacts = []

    def __init__(self):
        pass
    
    """add a new contact to contacts list"""
    def add_new_contact(self):
        self.contacts.append({"name":input("Please enter contact name?"), "phone": int(input("Please enter contact phone number?"))})
        print("Contact successfully added")
    
    """print all the contacts """
    def display_all_contacts(self):
        print(self.contacts) 

    """delete contact by name"""
    def delete_contact(self):
        contact_to_search = input("Which name whould you like to delete?")
        for contact in self.contacts:
            if contact["name"] == contact_to_search:
                self.contacts.remove(contact)
                print(f"The following details have been deleted.")
                print(f"name: {contact['name']}, phone number: {contact['phone']}")
                # with open(DATA_FILE,"w") as file_save:
                #       json.dump(self.contacts,file_save,indent=4)
                return
        print(f"{contact_to_search} NOT FOUND") 

    """search contact by name"""
    def search_contact(self):
        contact_to_search = input("Which name whould you like to search?")
        for contact in self.contacts:
            if contact["name"] == contact_to_search:
                print(f"Found! name: {contact['name']}, phone number: {contact['phone']}")
                return
        print(f"{contact_to_search} NOT FOUND") 

    def __str__(self):
        res = ""
        for contact in self.contacts:
            res += contact.__str__() + "\n"
        return res
    

