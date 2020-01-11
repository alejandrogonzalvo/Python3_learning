# !/usr/bin/python3.5

import json

def greet_user():
    """Asks a user for their name and returns it."""

    name = input("\nWhat's your name?  ")

    return name

def favnum(name):
    """Searches for the user favourite number. If not found, asks the new user their favourite number and stores it."""

    filename = 'favnum_list.json' # The file where the information is stored.
    my_dict = {} # The dictionary that will be moving all the info stored on this session and the others.S
    

    try: # Checks if the file exists, and executes the apropiate code according to the situation.
        with open(filename, 'r') as f_obj: 
            my_dict = json.load(f_obj)
        
        if name in my_dict:
            print("\nOh, I remember you, your favourite number was " + my_dict[name] + "!")
            
        else:

            while True:

                try:
                    favnum = int(input("\nIt seems that it's your first time here... Which number is your favourite?  "))

                except ValueError:
                    print("Hey! Thats not a number! Enter a number please:  ")

                else:
                    with open(filename, 'w') as f_obj:
                        my_dict[name] = favnum 
                        json.dump(my_dict,f_obj, indent=4)

                    print("\nThanks, i'll remember it!")
                    break

    except FileNotFoundError:

        while True:

            try:
                favnum = input("Seems you are the first one here! What's your favourite number?   ")

            except ValueError:
                print("Hey! Thats not a number! Enter a number please:  ")
            
            else:
                with open(filename, 'w') as f_obj:
                    my_dict[name] = favnum 
                    json.dump(my_dict,f_obj, indent=4)

                print("\nThanks, i'll remember it!")
                break

