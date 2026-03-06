contacts = {
    'jim' : {'email' : 'jim@gmail.com', 'phone number' : '+447400101675'},
    'brandon' : {'email' : 'brandon@hotmail.com', 'phone number' : '+447400924711'},
    'greg' : {'email' : 'greg@live.com', 'phone number' : '+447400585581'}
}

while True:
    print("""
    1. Add Contact
    2. View Contact
    3. Update Contact
    4. Delete Contact
    5. Exit""")
    num_task = input("Please input the number that you want to select: ")
    if num_task == '1':
        add_contact_name = str(input('What is the name of the person you want to add to your contacts? ')).lower()
        add_contact_email = str(input(f'What is the email of {add_contact_name}? '))
        add_contact_num = str(input(f'What is the phone number of {add_contact_name}? '))
        contacts[add_contact_name] = {'email' : add_contact_email, 'phone number' : add_contact_num}
        print('Contact added')
    elif num_task == '2':
        view_contact = str(input("Who's contact information would you like to view? ")).lower()
        if view_contact in contacts:
            print(contacts[view_contact])
        else:
            print('That user does not exist')
    elif num_task == '3':
        update_contact_name = str(input("Who's contact would you like to update? ")).lower()
        if update_contact_name in contacts:
            update_contact_value = str(input("Would you like to change email or phone number? "))
            if update_contact_value != 'email' and update_contact_value != 'phone number':
                print('Invalid, please input "email" or "phone number"')
            else:
                updated_value = str(input(f"What would you like to change {update_contact_value} to? "))
                contacts[update_contact_name][update_contact_value] = updated_value
                print('Contact updated')
        else:
            print('That user does not exist')
    elif num_task == '4':
        delete_contact_name = str(input("Who's contact would you like to delete? ")).lower()
        if delete_contact_name in contacts:
            del contacts[delete_contact_name]
            print('Contact deleted')
        else:
            print('That user does not exist')
    elif num_task == '5':
        break
for key, value in contacts.items():
    print(key, "|", value)
