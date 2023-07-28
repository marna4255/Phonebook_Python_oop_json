from helper import DATA_FILE, load, save
from Phonebook import Phonebook
from colorama import Fore,Style


"""menu for user"""
def menu():
    print()
    print(Fore.LIGHTCYAN_EX + "Welcome to Contacts Manager!" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + "what would you like to do?" + Style.RESET_ALL)
    print("1 - Add new contact")
    print("2 - Display all contacts")
    print("3 - Delete contact by name")
    print("4 - Search contact by name")
    print("5 - Exit")
    return int(input(Fore.GREEN + "Please enter your selection: " + Style.RESET_ALL))



def main():
    my_phonebook = Phonebook()
    my_phonebook.contacts = load(DATA_FILE)
    user_selection = menu()
    while user_selection != 5:
        if user_selection == 1: my_phonebook.add_new_contact()
        if user_selection == 2: my_phonebook.display_all_contacts()
        if user_selection == 3: my_phonebook.delete_contact()
        if user_selection == 4: my_phonebook.search_contact()
        user_selection = menu()
    print(Fore.MAGENTA + "Thank you for using my software. Bye!")
    save(my_phonebook.contacts) 
    

if __name__ == "__main__":
    main()