# !/usr/bin/python3.5
 
# This program executes asks a user for their name and favourite number and stores it in a json file.
# The program should work correctly withour editing the file. If it doesn't try checking if the json file exists but it's empty. if so delete it


import favnum as f


name = f.greet_user()
f.favnum(name)

