# !/usr/bin/python3.5


import time as t
import random as r


class Player():
    """A representation of a controllable player that moves in a 2d world(eagle view, like pokemon)"""

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

    # We define the methods which will be used for both the dog and the player to change their coordinates.    
    def up(self):
        self.y_pos += 1

    def down(self):
        self.y_pos -= 1

    def left(self):
        self.x_pos -= 1

    def right(self):
        self.x_pos += 1


class Dog():
    """A representation of a dog that moves in a 2d world(eagle view, like pokemon)"""

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

        # We define what the initial position of the dog will be, ensuring i won't be zero making the game end instantly
        while self.x_pos == 0:
            self.x_pos = r.randint(-10,10)

        while self.y_pos == 0:
            self.y_pos = r.randint(-10,10)

    def up(self):
        self.y_pos += 1

    def down(self):
        self.y_pos -= 1

    def left(self):
        self.x_pos -= 1

    def right(self):
        self.x_pos += 1
        

# We create an object for the player and the dog with the properties we've defined before
player = Player()
dog = Dog()

#Introduction and instructions to the game
print("You are a blind person who just woke up. The first thing you should do is trying to find your guide dog.\n")
t.sleep(2)
print("Use awsd to move left/up/down/right, respectively.\n")
t.sleep(2)
print("Have in mind that your last dog died in an accident and your new dog is just just getting used to its new work, so he might run away from time to time\n")
t.sleep(4)
print("Good Luck!\n")
t.sleep(2)

c = 0 # This variable will increase each time the while loops, and it will make the dog move and be reseted to zero when it arrives 2. It's a bit messy tu put it in here, advice accepted.   

# As you're blind, this will print a line of text simulating your hearing to guess the dog's position
while player.x_pos != dog.x_pos or player.y_pos != dog.y_pos:
    
    if player.x_pos < dog.x_pos and player.y_pos < dog.y_pos:
        print("You can hear your dog barking from the northeast")

    elif player.x_pos == dog.x_pos and player.y_pos < dog.y_pos:
        print("You can hear your dog barking from the north")
    
    elif player.x_pos > dog.x_pos and player.y_pos < dog.y_pos:
        print("You can hear your dog barking from the northwest")

    elif player.x_pos < dog.x_pos and player.y_pos == dog.y_pos:
        print("You can hear your dog barking from the east")

    elif player.x_pos > dog.x_pos and player.y_pos == dog.y_pos:
        print("You can hear your dog barking from the west")

    elif player.x_pos < dog.x_pos and player.y_pos > dog.y_pos:
        print("You can hear your dog barking from the southeast")

    elif player.x_pos == dog.x_pos and player.y_pos > dog.y_pos:
        print("You can hear your dog barking from the south")

    elif player.x_pos > dog.x_pos and player.y_pos > dog.y_pos:
        print("You can hear your dog barking from the southwest")

    else:
        print("Wow, this dialogue is theorically impossible to activate. I dont know what you just done, but contact the developer inmediately and tell him please ^^")

    #This will pause the loop until the player makes a movement, process the movement and continue the loop until it reutrns to this same point.
    
    while True:
        
        m = input()

        if m == 'a':
            player.left()
            break

        elif m == 'w':
            player.up()
            break
        elif m == 's':
            player.down()
            break
        elif m == 'd':
            player.right()
            break

        else:
            print("\nYou somehow forgot how to coordinate your legs. Try telling your dog to make you a coffe when you find it.")
        
    c += 1 

    #This ends producing the dog a random movement every 2 turns.
    if c == 2:
        d = r.randint(0,3)

        if d == 0:
            dog.left()

        if d == 1:
            dog.up()
    
        if d == 2:
            dog.down()

        if d == 3:
            dog.right()

        c = 0

#Endgame and congratulations message
print('\nAs you walk towards the sound, you can finally feel your dog jumping at your legs')
t.sleep(4)
print('\nCongratulations! You won!')
t.sleep(5)




