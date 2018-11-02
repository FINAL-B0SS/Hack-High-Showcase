# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TheRedLetter.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maljean <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/31 16:00:28 by maljean           #+#    #+#              #
#    Updated: 2018/11/01 17:04:27 by maljean          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def page7():
    print ("Blam! Dead")

def page6():
    print("""You decide to run away. In the distance you\nhear a car. Its headlights are getting closer.\nYou take a left turn into a dark alleyway and\nend up behind a small boat house. You see\nthe car speed past you and you decide to\nflank it.

You run onto the main road and lose it. It\nonly took you ten minutes to find the police\nstation nearest to you. 

Once you arrive you quickly tell your story.\nThirty minutes later the police sergeant\nreturns looking happy with himself. He tells\nyou that you were the bait in a drug bust\nand now you are a key person in the crime\nof the year.""")

def page5():
    print ("""You decide to stand your ground. The car is\ngetting dangerously close to you. Five\nseconds feels like it has been an hour.\n

The car is getting nearer and you are\nregretting your decision. You can now see\nthe red hood of the car coming towards\nyou.

Just as you get ready for the numbing pain\nof the car hitting you it screeches to a stop.\nA suited man comes out of the car and he is\nholding a hand gun. “Where is the money?”\nthe man shouts at you.""")
    page7()

def page4():
    print ("""You decide to go down to the docks to\nconfront the person who wrote the red\nletter. 

11:59 pm and there is no one there. Where\nis he? You think to yourself, did he forget? Is\nit a prank? 

Then you hear a car rumble in the distance.\nA pair of bright yellow headlights pop into\nexistence and they are heading towards you\nand the noise is getting louder.""")
    answer = input("a. Stand your ground\nb. Run away as fast as you can\n")
    if answer == "a":
        page6()
    elif answer == "b":
        page7()

def page3():
    print ("""You are too curious not to answer your\nmail. So you grab it out of your mailbox and\nopen it and find seven words. 

‘Meet me on the docks at twelve’ 

You are not that sure whether to go or not\nbecause it seems like a stereotypical set up\nfor a camp fire story.""")
    page4()

def page2():
    print ("""You decide that it is too suspicious and you\nchoose to go inside. Half way up the drive\nyou slip and fall head first on a rock. 

No one knows what happened to your\nbody. Did the writer of the letter take it?

THE END""")

print ("""After a long hard day at your boring office job you arrive at\nhome. Before you walk into your house you see a letter in\nyour mailbox, an unusual occurrence as bill day is Thursday\nnot Monday.

You go up to the mailbox and see that there is a little red letter... quite suspicious. """)
answer = input("a. Open mail\nb. Go inside\n")
if answer == "a":
    page3()
elif answer == "b":
    page2()
