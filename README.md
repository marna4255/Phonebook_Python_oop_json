"# Phonebook_Python_oop_json" 

<h1>Contact Manager:</h1>
<p>The Contact Manager is a simple Python program that allows users to manage a list of contacts. Users can add new contacts, view all contacts, delete contacts by name, search for contacts by name, and save the contacts to a JSON file. The program uses a Command-Line Interface (CLI) for interaction.</p>

<h1>Requirements:</h1>
<p>Python 3.x</p>
<p>colorama (for colored output in the terminal)</p>

<h1>Getting Started</h1>
<p>1. Install Python:
    If you don't have Python installed, download and install the latest version of Python 3 from the official website: https://www.python.org/downloads/</p>

<p>2. Install colorama:
    Open your terminal/command prompt.
    Run the following command to install colorama using pip:</p>

   <h3>copy code: pip install colorama</h3>

<p>3. Clone the repository or download the files:
  Clone this repository to your local machine using Git:</p>

    copy code: git clone https://github.com/marna4255/Phonebook_Python_oop_json.git

  <p>Alternatively, you can download the ZIP file from the "Code" button on the repository's GitHub page and extract it to your desired location.</p>


<p>4. Navigate to the project directory:</p>

  <h3>copy code: cd contact-manager</h3>


<p>5.Run the Contact Manager:</p>

  <h3>Copy code: python main.py</h3>


<h1>Usage:</h1>
<p>Upon running the Contact Manager, you will be presented with a menu-driven interface. Use the provided options to manage your contacts:</p>

<p>1. Add new contact: Select option 1, then enter the name and phone number for the new contact.</p>

<p>2. Display all contacts: Select option 2 to view a list of all the contacts you have added.</p>

<p>3. Delete contact by name: Choose option 3 and enter the name of the contact you wish to delete. The contact will be removed from the list.</p>

<p>4. Search contact by name: Select option 4 and enter the name of the contact you want to search for. The program will display the contact's details if found.</p>

<p>5.Exit: To exit the Contact Manager, select option 5.</p>


<p>Data Persistence:
The contact data is stored in a JSON file named 'contacts.json'.
When you exit the program (by selecting option 5), the current list of contacts will be saved to the contacts.json file. The contacts will be loaded from this file the next time you run the program.</p>


<h1>Note:</h1>
<h5><a>If the contacts.json file does not exist</a></h5> <p>when you run the program for the first time, it will create an empty file to store the contacts.
Contributing
Contributions to this project are welcome! If you find any issues or have improvements to suggest, feel free to create a pull request or open an issue on the GitHub repository.</p>
