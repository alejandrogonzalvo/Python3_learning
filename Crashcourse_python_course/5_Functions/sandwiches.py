# !/usr/bin/python3.5


def make_sandwich(bread_type, *ingredients):
    if ingredients:

        print('\nyour ' + bread_type + ' bread sandwich with:')
        for ingredient in ingredients:
            print('- '+ ingredient)
        print('is on the grill!')
    
    else:
         print('\nyour ' + bread_type + ' bread vegan sandwich is on the grill!')

