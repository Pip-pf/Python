def add_contact(contacts):
    add_contact_name = input('What is the name of the person you want to add to your contacts? ').strip().lower()
    if add_contact_name == "":
        print('You cannot add an empty name to contacts')
        return
    elif add_contact_name in contacts:
        print('Contact already exists')
        return
    add_contact_email = input(f'What is the email of {add_contact_name.title()}? ').lower()
    add_contact_num = input(f'What is the phone number of {add_contact_name.title()}? ')
    contacts[add_contact_name] = {'email' : add_contact_email, 'phone number' : add_contact_num}
    print('Contact added')
        
def view_contact(contacts):
    view_contact = input("Who's contact information would you like to view? ").strip().lower()
    if view_contact in contacts:
        print(view_contact.title(), '|', contacts[view_contact]['email'], '|', contacts[view_contact]['phone number'])
    else:
        print('That user does not exist')

def update_contact(contacts):
    update_contact_name = input("Who's contact would you like to update? ").strip().lower()
    if update_contact_name in contacts:
        update_contact_value = input("Would you like to change email or phone number? ")
        while update_contact_value not in ['email', 'phone number']:
            update_contact_value = input('Invalid, please input "email" or "phone number": ')
        else:
            updated_value = input(f"What would you like to change {update_contact_value} to? ")
            contacts[update_contact_name][update_contact_value] = updated_value
            print('Contact updated')
    else:
        print('That user is not in contacts')

def view_all_contacts(contacts):
    for key, value in contacts.items():
        print(key, '|', value['email'], '|', value['phone number'])
    
def delete_contact(contacts):
    delete_contact_name = input("Who's contact would you like to delete? ").strip().lower()
    if delete_contact_name in contacts:
        del contacts[delete_contact_name]
        print('Contact deleted')
    else:
        print('That user does not exist')

def exit_contact(contacts):
    global menu_loop
    menu_loop = False
    
menu_loop = True
contacts = {
    'jim' : {'email' : 'jim@gmail.com', 'phone number' : '+447400101675'},
    'brandon' : {'email' : 'brandon@hotmail.com', 'phone number' : '+447400924711'},
    'greg' : {'email' : 'greg@live.com', 'phone number' : '+447400585581'}
}  
function_dict = {
    '1' : add_contact,
    '2' : view_contact,
    '3' : update_contact,
    '4' : delete_contact,
    '5' : view_all_contacts,
    '6' : exit_contact
}

while menu_loop:
    print("""
    1. Add Contact
    2. View Contact
    3. Update Contact
    4. Delete Contact
    5. View All Contacts
    6. Exit""")
    num_task = input("Please input the number that you want to select: ")
    if num_task in function_dict:
        function_dict[num_task](contacts)
    else:
        print('Invalid input')
