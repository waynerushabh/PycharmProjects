# Collection problems
# Dictionaries 4
# CRUD Project

# PhoneBook

phonebook = {}
while True:
    print()
    print("*********************")
    print("  *** PhoneBook ***  ")
    print("*********************")
    print("1. View All Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("*********************")
    print()

    option = input("Enter option (1-6) = ")
    print()
    if option.isdecimal():
        if int(option) == 1:
            contacts = phonebook.items()
            if contacts:
                print("** All Contacts **")
                str0 = "Name"
                str1 = "Number"
                print(str0.rjust(10), " : ", str1)
                print("***************************")
                for name in phonebook:
                    mob_no = phonebook[name]
                    print(str(name).rjust(10), " : ", mob_no)
                print("***************************")
            else:
                print("PhoneBook is Empty.")
                print("*********************")
        elif int(option) == 2:
            name = input("Add Name : ")
            mob_no = int(input("Add Number : "))
            if name not in phonebook:
                phonebook[name] = mob_no
                print(f'Contact {name} Saved Successfully.')
                print("** All Contacts **")
                str0 = "Name"
                str1 = "Number"
                print(str0.rjust(10), " : ", str1)
                print("***************************")
                for name in phonebook:
                    mob_no = phonebook[name]
                    print(str(name).rjust(10), " : ", mob_no)
                print("***************************")
            else:
                print("Contact exists. Try option->\'4. Update Contact\' option.")
                print("*********************")
        elif int(option) == 3:
            contacts = phonebook.items()
            if contacts:
                search_string = input("Enter Contact Name or Number to Search : ")
                print("** Search Results **")
                search_name = list(phonebook.keys())
                search_numbers = list(phonebook.values())
                if search_string in search_name:
                    mob_no = phonebook[search_string]
                    print(f'{search_string} : {mob_no}')
                else:
                    if int(search_string) in search_numbers:
                        print(search_name[search_numbers.index(int(search_string))], " : ", search_string)
                    else:
                        print(f'Contact {search_string} Not Found.')
                        print("*********************")
            else:
                print("PhoneBook is Empty.")
        elif int(option) == 4:
            contacts = phonebook.items()
            if contacts:
                print("** All Contacts **")
                str0 = "Name"
                str1 = "Number"
                print(str0.rjust(10), " : ", str1)
                print("***************************")
                for name in phonebook:
                    mob_no = phonebook[name]
                    print(str(name).rjust(10), " : ", mob_no)
                print("***************************")
                name = input("Edit Contact : ")
                if name in phonebook:
                    print(f'Old details -> {name} : {phonebook[name]}')
                    new_name = input("Enter new name : ")
                    mob_no = input("Enter new number : ")
                    del phonebook[name]
                    phonebook[new_name] = mob_no
                    print(f'Contact {new_name} Updated Successfully.')
                    print("*********************")
                else:
                    print(f'Contact {name} Not Found.')
                    print("** All Contacts **")
                    str0 = "Name"
                    str1 = "Number"
                    print(str0.rjust(10), " : ", str1)
                    print("***************************")
                    for name in phonebook:
                        mob_no = phonebook[name]
                        print(str(name).rjust(10), " : ", mob_no)
                    print("***************************")
            else:
                print("PhoneBook is Empty.")
                print("*********************")
        elif int(option) == 5:
            contacts = phonebook.items()
            if contacts:
                print("** All Contacts **")
                str0 = "Name"
                str1 = "Number"
                print(str0.rjust(10), " : ", str1)
                print("***************************")
                for name in phonebook:
                    mob_no = phonebook[name]
                    print(str(name).rjust(10), " : ", mob_no)
                print("***************************")
                name = input("Enter Contact to Delete : ")
                if name in phonebook:
                    print(f'Are you sure you want to delete {name} ?')
                    ans = input("Confirm with Yes/No -> (y/ any other key) : ")
                    if ans == 'y' or 'Y':
                        del phonebook[name]
                        print(f'Contact {name} Deleted.')
                        print("*********************")
                    else:
                        print("Deletion Canceled.")
                        print("*********************")
                else:
                    print(f'Contact {name} Not Found.')
                    print("*********************")
            else:
                print("PhoneBook is Empty.")
                print("*********************")
        elif int(option) == 6:
            print("*********************")
            print("Exiting .")
            print("Exiting . .")
            print("Exiting . . .")
            print("*********************")
            break
        else:
            print("***************************")
            print("Wrong input. Try again with a valid option number between 1-6.")
            print("***************************")
    else:
        print("***************************")
        print("Wrong input. Try again with a valid option number between 1-6.")
        print("***************************")
