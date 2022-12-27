from tkinter import *


# tk gui setup

root = Tk()
root.geometry('300x300')
root.title('DataFlair-Mad Libs Generator')
Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()
Label(root, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)

"""
Mad Libs Thingy Maboober
--------
"""
# Madlibs subject 1


def madlibs1():
    animal = input("Enter an animal name: ")
    profession = input("Enter a profession name: ")
    clothes = input("Enter a clothing brand name: ")
    r_thing = input("Enter a random object: ")
    name = input("Enter your name: ")
    place = input("Enter a random place: ")
    verb = input("Enter a random verb: ")
    food = input("Enter a random food: ")
    print(f"""There was a {animal} who worked as a {profession}.
          They were known for their unique sense of style, often wearing {clothes} and carrying around a {r_thing} wherever they went.
          One day, {name} decided to take a trip to {place} and decided to bring some {food} along for the journey.
          Along the way, they encountered many exciting adventures and {verb} their way through each challenge.
          It was an unforgettable trip that they would never forget.
          """)


madlibs1()


def madlibs2():
    adjective = input("Enter an adjactive: ")
    color = input("Enter a color: ")
    thing = input("Enter a random thing: ")
    place = input("Enter a random place: ")
    person = input("Enter a random person's name: ")
    adjective1 = input("Enter a random adjactive: ")
    insect = input("Enter a random insect: ")
    verb = input("Enter a random verb: ")
    food = input("Enter a random food: ")
    madlibs_paragraph = f"I was feeling very {adjective} when I walked into the {color} {thing} at the {place}. The {person} there was so {adjective1} and greeted me with a smile. As I browsed the shelves, I noticed a {insect} flying around, collecting {food}. It was so cute watching it {verb} from flower to flower."
    print(madlibs_paragraph)


def madlibs3():
    adjective = input("Enter an adjective: ")
    color = input("Enter a color: ")
    thing = input("Enter a thing: ")
    place = input("Enter a place: ")
    person = input("Enter a person: ")
    adjective1 = input("Enter another adjective: ")
    insect = input("Enter an insect: ")
    food = input("Enter a food: ")
    verb = input("Enter a verb: ")
    madlibs_paragraph = f"The {adjective} {color} {thing} sat quietly in the {place}, waiting for the {person} to arrive. When they finally arrived, they were greeted with a warm and {adjective1} hug from the {insect}. The {insect} then proceeded to offer the {person} some delicious {food} and asked them to join in a game of {verb}."
    print(madlibs_paragraph)


Button(root, text='The Big Trip', font='arial 15',
       command=madlibs1, bg='ghost white').place(x=60, y=120)
Button(root, text='The Anxious Wait', font='arial 15',
       command=madlibs3, bg='ghost white').place(x=70, y=180)
Button(root, text='The Adventure', font='arial 15',
       command=madlibs2, bg='ghost white').place(x=80, y=240)
root.mainloop()
