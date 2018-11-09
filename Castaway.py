# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Castaway.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maljean <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/01 16:38:37 by maljean           #+#    #+#              #
#    Updated: 2018/11/09 14:57:14 by maljean          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

flares = 1
pistols = 1
bullets = 3
compass = 0

def exitCave():
    clear()
    stock()
    print("""You go back to the mouth of the cave. Now what?""")
    if input("a. Go into the jungle.\nb. Wade into the stream.\n") == "a":
        goIntoTheJungle()
    else:
        wadeStream()

def pickUp():
    clear()
    global compass
    compass += 1
    stock()
    print("""
You pick up the object and carry on. It turns out to be a compass -- maybe it will be useful later. Meanwhile, the tunnel goes round in a circle, and you find yourself back at the mouth of the cave. You are beginning to lose heart.\n""")
    answer = input("a. Shoot yourself.\nb. Go into the jungle.\nc. Wade into the stream.\n")
    if answer == "a":
        clear()
        print("""You shoot yourself in despair. Immediately afterwards, a rescue helicopter arrives on the island, and takes your body back to be buried.

It's all over!\n""")
    elif answer == "b":
        goIntoTheJungle()
    elif answer == "c":
        wadeStream()

def leaveIt():
    clear()
    stock()
    print ("""The tunnel goes round in a circle, and you find yourself back at the mouth of the cave. You are beginning to lose heart.""")
    answer = input("a. Shoot yourself.\nb. Go into the jungle.\nc. Wade into the stream.\n")
    if answer == "a":
        clear()
        print("""You shoot yourself in despair. Immediately afterwards, a rescue helicopter arrives on the island, and takes your body back to be buried.

It's all over!\n""")
    elif answer == "b":
        goIntoTheJungle()
    elif answer == "c":
        wadeStream()

def contCave():
    clear()
    stock()
    print("""You continue into the cave. You stumble and fall, and your leg touches something hard.\n""")
    if input("a. Pick it up and carry on.\nb. Leave it and carry on.\n") == "a":
        pickUp()
    else:
        leaveIt()

def fork():
    clear()
    stock()
    print ("""You go down the tunnel. You can hardly see anything in the dark. What do you do?\n""")
    if input("a. Go back out of the cave.\nb. Continue into the cave.\n") == "a":
        exitCave()
    else:
        contCave()

def enterCave():
    clear()
    stock()
    print ("""You go into the cave. It's very dark. There are two tunnels, left and right. Which one do you take?\n""")
    if input("a. Take the left fork.\nb. Take the right fork.\n") == "a":
        fork()
    else:
        fork()

def giveUp():
    clear()
    stock()
    print ("""You give up trying to attract the attention of the ship, and come down from the hill. What next?\n""")
    if input("a. Go into the jungle.\nb. Start swimming out to sea.\n") == "a":
        clear()
        continueJungle()
    else:
        backToBeach()

def firePistol():
    clear()
    global bullets
    bullets -= 1
    stock()
    print("You fire the pistol, hoping the noise will attract the attention of the crew on the ship. Unfortunately, it doesn't.\n")
    if input("a. Fire a rescue flare to attract the ship's attention.\nb. Give up trying to attract the ship's attention.\n") == "a":
        if flares <= 0:
            giveUp()
        fireFlare()
    else:
        giveUp()

def fireFlare():
    clear()
    global flares
    flares -= 1
    stock()
    print("""You fire the flare into the sky. Unfortunately, it's a very bright, sunny day, and the flare is almost invisible in the blazing sun. The ship continues moving away from you.\n""")
    if input("a. Give up trying to attract the ship's attention.\nb. Fire the pistol to attract the ship's attention.\n") == "a":
        giveUp()
    else:
        if bullets <= 0:
            giveUp()
        firePistol()

def climbHill():
    clear()
    stock()
    print("""You climb to the top of the hill. It takes a while, but when you reach the top, you can see the whole island spread out before you. You can also see, on the distant horizon, a small ship. It is heading away from you.\n""")
    if input("a. Fire the rescue flare to attract the ship's attention.\nb. Fire the pistol to attract the ship's attention.\n") == "a" :
        if flares <= 0:
            giveUp()
        fireFlare()
    else:
        if bullets <= 0:
            giveUp()
        firePistol()

def backToBeach():
    clear()
    print ("You start swimming out to sea, hoping to be picked up by a ship. After eight hours, you are still swimming, and then...you are eaten by ravenous sharks. It's all over!\n")

def swimToBank():
    clear()
    stock()
    print ("""You try to swim against the current, but it's no use -- you are swept out to sea.\n""")
    if input("a. Swim out to sea in the hope of being picked up by a boat\n") == "a":
        backToBeach()
    else:
        print("""You try to swim back to the island, but the current is too strong. You are swept out to sea. And then....you are eaten by ravenous sharks.
        It's all over!\n""")

def exitWater():
    clear()
    stock()
    print ("""You climb out of the water. You're right near the place where you first landed on the island.\n""")
    if input("a. Go into the jungle.\nb. Climb the hill.\n") == "a":
        clear()
        continueJungle()
    else:
        climbHill()

def guessIt():
    clear()
    stock()
    print ("""You do your best to find your way to the shipping lane, but you get hopelessly lost. After several days, you are in total despair.""")
    if input("a. Shoot yourself.\nb. Don't shoot yourself.\n") == "a":
        clear()
        print ("""You shoot yourself in despair. Immediately afterwards, a rescue helicopter arrives on the island, and takes your body back to be buried.

It's all over!\n""")
    else:
        clear()
        print ("""You slowly starve to death. Eventually, you don't even have enough energy to shoot yourself. You wish you had, but it's too late. Never mind.

It's all over!\n""")

def sailBoat():
    clear()
    stock()
    global compass
    print("""You steer your boatsailboat.gif out to sea. You know that there is a shipping lane to the north west.\n""")
    if compass > 0:
        if input("a. Steer north-west using the compass.\nb. Guess where north west is and try to steer in that direction.\n") == "a":
            clear()
            print ("""You use the compass to steer your boat to the north-west. Eventually, you reach the shipping lanes, and a boat full of migrants picks you up and takes you directly to the West Coast of Canada, where you start a new adventure! Well done -- you've saved yourself.

You made it!\n""")
        else:
            guessIt()
    else:
        input("a. Guess where north west is and try to steer in that direction.\n")
        guessIt()

def relax():
    clear()
    stock()
    print ("""You coast along in the water, and eventually you are swept into a little bay. You find a rowing boat there.\n""")
    if input("a. Climb out of the water.\nb. Sail the boat out to sea.\n") == "a":
        exitWater()
    else:
        sailBoat()

def wadeStream():
    clear()
    stock()
    print ("""You wade into the stream. Unfortunately, the water is running very fast, and you are swept off your feet and carried away.\n""")
    if input("a. Swim as hard as you can to reach the bank.\nb. Relax and let the water take you where it wants to go.\n") == "a":
        swimToBank()
    else:
        relax()

def continueJungle():
    stock()
    print ("""You continue moving through the jungle. Soon, you hear the sound of running water, and you see a stream emerging from a cave.\n""")
    if input("a. Wade across the stream.\nb. Go into the cave.\n") == "a":
        wadeStream()
    else:
        enterCave()

def stickLizard():
    clear()
    print ("""You pick up a large stick, and hit the lizard firmly on the head. He grunts, then turns and shuffles away into the bushes.\n""")
    continueJungle()

def scareLizard():
    global bullets
    bullets -= 1
    clear()
    print("""You fire your pistol into the air. The lizard is afraid of the noise, and it turns around and shuffles back into the jungle. You hear it receding into the distance.""")
    continueJungle()

def shootAgain():
    clear()
    print ("""You shoot the lizard again. This enrages him mightilty, and he attacks and kills you!""")

def runFromLizard():
    clear()
    stock()
    print ("""You turn and run away from the lizard. However, the lizard comes after you. You are unable to run fast enough to escape. What do you do?\n""")
    answer = input("a. Run back to the beach and start swimming out to sea.\nb. Shoot the lizard again.")
    if answer == "a":
        backToBeach()
    else:
        shootAgain()

def climbTree():
    clear()
    stock()
    print("""You climb up a tree to escape the lizard. For about fifteen minutes, he paces around the bottom of the tree, sniffing and roaring, but then he gives up and shuffles away. You hear him moving away into the jungle.\n""")
    continueJungle()

def shootLizard():
    global bullets
    bullets -= 1
    clear()
    stock()
    print ("""You fire at the lizard with your pistol. Your shot hits him in the neck, and he starts bleeding, but he is not killed -- he just gets more angry and comes towards you.\n""")
    answer = input("a. Shoot the lizard again.\nb. Turn and run away from the lizard.\nc. Climb a tree to get out of the animal's way.\n")
    if answer == "a":
        clear()
        shootAgain()
    elif answer == "b":
        runFromLizard()
    else:
        climbTree()

def goTowardsTheAnimalNoises():
    clear()
    stock()
    print ("""You advance towards the noises. Suddenly, a huge lizard the emerges from the bushes. It is bigger than you -- it looks like a komodo dragon. It looks at you hungrily. What should you do?\n""")
    answer = input("""a. Pick up a large stick and hit the lizard.\nb. Fire your pistol to scare the lizard away.\nc. Shoot the lizard with your pistol.\n""")
    if answer == "a":
        stickLizard()
    elif answer == "b":
        if bullets == 0:
            clear()
            print("You're out of bullets, the lizard kills you")
        else:
            scareLizard()
    else:
        if bullets == 0:
            clear()
            print("You're out of bullets, the lizard kills you")
        else:
            shootLizard()

def confrontAnimal():
    clear()
    stock()
    print("""You stop, with your back to a large tree, and wait for the animal to emerge from the bushes. It soon appears. It is a huge lizard, about two metres long -- possibly a Komodo dragon. It glares at you hungrily.\n""")
    answer = input("""a. Pick up a large stick and hit the lizard.\nb. Fire your pistol to scare the lizard away.\nc. Shoot the lizard with your pistol.\n""")
    if answer == "a":
        stickLizard()
    elif answer == "b":
        if bullets == 0:
            clear()
            print("You're out of bullets, the lizard kills you")
        else:
            scareLizard()
    else:
        if bullets == 0:
            clear()
            print("You're out of bullets, the lizard kills you")
        else:
            shootLizard()

def moveAwayFromTheAnimalNoises():
    clear()
    stock()
    print ("""You turn away into the jungle to escape from the animal. However, after a little while you realize that the noises are still getting closer. The animal is following you!\n""")
    if input("a. Climb a tree to get out of the animal's way.\nb. Wait to confront the animal.\n") == "a":
        climbTree()
    else:
        confrontAnimal()

def goIntoTheJungle():
    clear()
    stock()
    print ("""You set off into the jungle. It's hard to make progress, but you struggle on slowly. Ahead, you can hear the sound of a large animal moving around\n""")
    if input("a. Go towards the animal noises.\nb. Move away from the animal noises.\n") == "a":
        goTowardsTheAnimalNoises()
    else:
        moveAwayFromTheAnimalNoises()

def stock():
    print("You have:\nFlares: {}\nPistols: {}\nBullets: {}".format(str(flares),str(pistols),str(bullets)))
    global compass
    if compass > 0:
        print ("compass: {}\n".format(str(compass)))
    else:
        print ("\n")

print ("""Can you survive shipwreck on a desert island?

You are the only survivor from the wreck of a cruise ship, which sank without warning during a severe tropical storm. You have managed to swim to shore on a desert island.
You managed to salvage several items from the ship:

1 Rescue flare
1 Pistol
3 Bullets

They may be useful to you.\n""") 

print ("""There is no sign of anyone. To your left is a high hill, and to your right is a dense jungle. What do you do?""")
if input("a. Go into the jungle.\nb. Climb the hill.\n") == "a":
    goIntoTheJungle()
else:
    climbHill()
