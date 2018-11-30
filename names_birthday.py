""""Storing Names and Birthdays in a Dictionary
In this section we look at a program that keeps your friends’ names and birthdays in a dictionary.
Each entry in the dictionary uses a friend’s name as the key and that friend’s birthday as the value.
You can use the program to look up your friends’ birthdays by entering
their names.
The program displays a menu that allows the user to make one of the following choices:
1. Look up a birthday
2. Add a new birthday
3. Change a birthday
4. Delete a birthday
5. Quit the program
The program initially starts with an empty dictionary, so you have to choose item 2 from
the menu to add a new entry. Once you have added a few entries, you can choose item 1 to
look up a specific person’s birthday, item 3 to change an existing birthday in the dictionary,
item 4 to delete a birthday from the dictionary, or item 5 to quit the program.Program 10-2
 shows the program code. The program is divided into six functions: main,
get_menu_choice, look_up, add, change, and delete. Rather than presenting the entire
program at once, let’s first examine the global constants and the main function:"""


def main(dictionary):
    print('Howdy User! Trust you are having a great day!')
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print()
    choice = int(input())
    if choice == 1:
        look_up(dictionary)
    elif choice == 2:
        add_new(dictionary)
    elif choice == 3:
        change_birth(dictionary)
    elif choice == 4:
        del_birth(dictionary)
    elif choice == 5:
        exit(0)
    else:
        print('Invalid Option')
        main(dictionary)


def look_up(dictionary):
    another = 'y'
    while another.lower() == 'y':
        print('Input the name you want to lookup ')
        name = input()
        print(dictionary.get(name, 'Not Found'))
        print()
        print('Enter Y to Search Another or any other key to go Back to Main Menu')
        another = input()

    main(dictionary)


def add_new(dictionary):
    another = 'y'
    while another.lower() == 'y':
        print('Enter Name')
        name = input()
        print('Enter Birthday')
        birthday = input()
        if name not in dictionary:
            dictionary[name] = birthday
        else:
            print('Name already exists!')
            add_new(dictionary)
        another = input("Enter Y to add another or any other key to go back to main menu")
    main(dictionary)


def change_birth(dictionary):
    another = 'y'
    while another.lower() == 'y':
        print('Enter Name Of the Friend You Want to Modify the Birthday')
        name = input()
        if name in dictionary:
            print('Enter Birthday')
            birthday = input()
            dictionary[name] = birthday
        else:
            print('Record Not Found!!')
            change_birth(dictionary)
        another = input("Enter Y to Change another or any other key to go back to main menu")
    main(dictionary)


def del_birth(dictionary):
    another = 'y'
    while another.lower() == 'y':
        print('Enter Name Of the Friend You Want to Modify the Birthday')
        name = input()
        if name in dictionary:
            print('Enter Birthday')
            del dictionary[name]
        else:
            print('Record Not Found!!')
            del_birth(dictionary)
        another = input("Enter Y to Delete Another or any other key to go back to main menu")
    main(dictionary)


main(dictionary={})
