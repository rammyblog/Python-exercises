""""Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person’s email address, add
a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts,
it should retrieve the dictionary from the file and unpickle it"""

import pickle
import os


def main():
    address_book = {}
    if not os.path.exists('name_address_records.dat'):
        contact = open('name_address_Records.dat', 'ab')
        address_book['DEFAULT'] = 'devloper@gmail.com'
        pickle.dump(address_book, contact)
        contact.close()
    print('Howdy User! Trust you are having a great day!')
    print("Friends and Their Birthdays")
    print('---------------------------')
    print('1. Look up an Email Address')
    print('2. Add a new Name And EMail Address')
    print('3. Change an Existing Email Address')
    print('4. Delete a Name And Email Address')
    print('5. Quit the program')
    print()
    choice = int(input())
    if choice == 1:
        look_up()
    elif choice == 2:
        add_new(address_book)
    elif choice == 3:
        change_email()
    elif choice == 4:
        del_address(address_book)
    elif choice == 5:
        exit(0)
    else:
        print('Invalid Option')
        main(address_book)


def look_up():
    search_email = input("Enter The E-Mail Address You Are Looking For ")
    end_of_file = False  # Set a flag as false
    input_file = open('name_address_records.dat', 'rb')  # OPen The File name you are searching for
    while not end_of_file:  # USe a while loop to iterate all the data in file until it reaches the end
        try:
            address_book = pickle.load(input_file)  # LOad The file
            # print(address_book)
            for name, email in address_book.items():  # Iterate through all the keys and values in the dictionary
                if email.lower() == search_email.lower():
                    print('Name: "%s" \nE-mail Address: "%s"' % (name, email))
        except EOFError:
            end_of_file = True
    input_file.close()


def add_new(address_book):
    another = 'y'
    while another.lower() == 'y':
        name = input('Enter Name')
        email = input('Enter Email')
        output_file = open('name_address_records.dat', 'ab')
        address_book[name] = email
        pickle.dump(address_book, output_file)
        another = input("Enter Y to add another Contact or any other key to quit")
    output_file.close()


def change_email():
    search_name = input("Enter Name")
    end_of_file = False  # Set a flag as false
    input_file = open('name_address_records.dat', 'rb')  # OPen The File name you are searching for
    modified_address_book = open('temp.dat', 'wb') # Open another temporary file to write to
    temp_dic = {} # Open another temp dictionary that will hold the key-value pairs of the new dictionary
    while not end_of_file:  # USe a while loop to iterate all the data in file until it reaches the end
        try:
            address_book = pickle.load(input_file)  # Load The file
            for name in address_book:  # Iterate through all the keys in the dictionary
                if name.lower() == search_name.lower():
                    print('Name: "%s" \nE-mail Address: "%s"' % (name, address_book[name]))
                    new_email = input('Enter New EMail')
                    temp_dic[name] = new_email
# Line81-85 will iterate through they whole file, once it come across the name
                # you want to modify it will print the name and email just in-case of multiple occurence
                # Then it will write the new email and name to the temp file
                else:
                    temp_dic[name] = address_book[name]
                    # If the name is not found Write other names to the temp file

        except EOFError:
            end_of_file = True
    pickle.dump(temp_dic, modified_address_book)
    modified_address_book.close()
    input_file.close()
    os.remove('name_address_records.dat')
    os.rename('temp.dat', 'name_address_records.dat')


def del_address(address_book):
    search_name = input("Enter Name")
    end_of_file = False  # Set a flag as false
    input_file = open('name_address_records.dat', 'rb')  # OPen The File name you are searching for
    modified_address_book = open('temp.dat', 'wb')
    temp_dic = {}
    # Found = False
    while not end_of_file:  # USe a while loop to iterate all the data in file until it reaches the end
        try:
            address_book = pickle.load(input_file)  # LOad The file
            for name in address_book:  # Iterate through all the keys in the dictionary
                if name.lower() == search_name.lower():
                    print('Name: "%s" \nE-mail Address: "%s"' % (name, address_book[name]))
                    print("Enter Y to delete or any other key to Not Delete")
                    confirm_delete = input()
                    if confirm_delete.lower() != 'y':
                        temp_dic[name] = address_book[name]
                    elif confirm_delete.lower() == 'y':
                        print(name + "has been deleted")

                else:
                    temp_dic[name] = address_book[name]
            # print(temp_dic)

        except EOFError:
            end_of_file = True
    pickle.dump(temp_dic, modified_address_book)
    modified_address_book.close()
    input_file.close()
    os.remove('name_address_records.dat')
    os.rename('temp.dat', 'name_address_records.dat')


main()
