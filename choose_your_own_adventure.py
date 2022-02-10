#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on an old and dusty road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across? Type 'walk' to walk around and 'swim' to swim across")
    if answer == "swim":
        print("You swam across the river and got eaten by a crocodile. Oh no.")
    elif answer == "walk":
        print("You walked for too long, ran out of food and unfortunately lost the game")
    else:
        print("Wasn't a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or swing across like Tarzan ('cross'/'swing')?")
    
    if answer == "swing":
        print("You have the confidence of Tarzan and create a rope out of vines. You know you can do this. You tie the rope on a branch and bravely jump out into the abyss. Unfortunately you had not been working out your arms recently and your life flashed before your eyes as your hands slipped from the vines. Game over.")
    elif answer == "cross":
        answer = input("You cross the bridge safely and meet a stranger. Do you talk to them (yes/no)? ")
        if answer == "yes":
            print("You talked to the stranger and they give you the treasure box you were looking for! You WIN!")
        elif answer == "no":
            print("You walk past the man and into the forrest. Unfortunately, there is no food in the forrest. You lose.")
        else:
            print("Wasn't a valid option. You lose.")
    else:
        print("Wasn't a valid option. You lose.")
else:
    print('You were too indecisive! You lose.')

print("Thank you for playing", name)


# In[ ]:




