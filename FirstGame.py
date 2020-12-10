print("Welcome to my first game!")
name = input("What is your name? ")
health = 10


def health_check():
    print("Your health is", health),
    if health == 0:
        print("the game is now over, you have died.")
        quit()
    elif health == 15:
        print("You have won the game so far, come back later for a longer story.")
        quit()


print("Hello", name, "lets begin.")
print("You will begin with", health, "health.")
print("You begin your adventure at an impass.")
decision_1 = input("Would you like to go with Honey Biscuit, or with Zeus? (HB/Z) ")
if decision_1 == "HB":
    print("Honey Biscuit takes you down the path of sunshine and rainbows.")
    print("As you are walking, you suddenly see a bird, how do you react?")
    decision_2HB = input("Do you attack the bird, or run away? (attack/run) ")
    if decision_2HB == "attack":
        print("Between you and Honey Biscuit you deal significant damage, and the bird dropped an item.")
        print("You pick up the item and find it's a shield! This shield gives you an additional 5 health.")
        health += 5
        health_check()
    else:
        print("As you run away from the bird, it outpaces you and manages to leave a package on your head.")
        print("This package is a lovely one, as it deals 3 damage to you")
        health -= 3
        health_check()
elif decision_1 == "Z":
    print("Zeus takes you down a path into a cave.")
    print("When you enter the cave, Zeus starts hopping about, until you realize there is a rabbit she is chasing.")
    print("As you help her find this rabbit, you spot two pathways, one is to Litter Boxia, the other is to Laser Pointe")
    decision_2Z = input("Do you go to Litter Boxia, or Laser Pointe (LB/LR)")
    if decision_2Z == "LB":
        print("As you head to Litter Boxia the overwhelming stench of bad cat litter overwhelms you, you lose 10 health.")
        health -= 10
        health_check()
    else:
        print("Laser Pointe turns out to be a town full of parties! You gain a helmet that gives you 5 health.")
        health += 5
        health_check()
else:
    print("Didn't recognize input, goodbye.")
    quit()
