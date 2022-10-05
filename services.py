#!/usr/bin/python
my_list = ['cloudwatch', 'ec2', 'dynamodb', 'vpc']
Current_list = True
while Current_list:
    next_step = input("Add, Remove, Exit?")
    
    print("Current list", my_list)
    if next_step == "Add":
        new_element= input("Add service to list?")
        my_list.append(new_element)
    
    elif next_step == "Remove":
        remove_element = input("Remove what?")
        if  remove_element in my_list:
                my_list.remove(remove_element)
    print("Current List", my_list)
    if next_step == "Exit":
        break