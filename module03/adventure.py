import time

invalidText = "Sorry, I don't quite understand. Please select the available options. "
def ending(num):
    if num == 1:
        time.sleep(0.5)
        print("The masked individual agrees to drive you home. The drive home is mainly professional, the only things said regarding directions and various landmarks. You finally make it home thanks to the stranger, and get to bed.")
        print("<----ENDING 1---->")
    elif num == 2:
        time.sleep(0.5)
        print("You scream and run away as fast as you can, you end up tripping and falling with everything going black. You wake up in the hospital in your town. Either whoever found you knew where you were from, lived in the same area, or this happened to be the nearest hospital. Alternatively, you could have dreamt all that happened.")
        print("<----ENDING 2---->")
    elif num == 3:
        time.sleep(0.5)
        print("You sneak into the cabin through the window, trying to be as quiet as possible. It was in vain, however. The lights flash on, and an 8-foot tall person stands before you. Said person is in rugged, mildly dilapidated clothes and a haniwa mask. You're promplty tackled to the ground, and the masked person calls the police while you're pinned. Shortly after, you're driven to custody by cops. Conveniently, the jail you're sent to happens to be in the same town you live in.")
        print("<----ENDING 3---->")
    elif num == 4:
        time.sleep(0.5)
        print("You wait for about five minutes, and a pair of people soon approach the car. The two ask you why you're by their car, and you explain that you need to get home. They look at each other, and come to an agreement. You're driven home, and you make two new friends.")
        print("<----ENDING 4---->")
    elif num == 5:
        time.sleep(0.5)
        print("You waste no time, getting in the car and driving out of the forest. You eventually get back on the road, and make your way home. The next day, you get a news report of someone's car being stolen in a nearby forest... That can't be a coincidence. Given you're home and all, you quietly return the car you stole and manage to not get arrested.")
        print("<----ENDING 5---->")
    elif num == 6:
        time.sleep(0.5)
        print("You go deep into the cave, glad to have a light with you. You soon come across a lantern by two miners, they seem to be gathering iron and gold. They ask you if you want to mine with them. Given you don't have anything else to do, and this is your only confirmed ticket out of here, you say yes. The three of you spend the next few hours mining while singing. None of you are singing very well, but you still all have fun gathering ore. Once the hours pass, they offer to drive you home after they stop by the recycling center. You gladly accept, and you are home the next day with two new friends and a new job.")
        print("<----ENDING 6---->")
    elif num == 7:
        time.sleep(0.5)
        print("You yell ''HELLO'' into the cave's mouth, and get a different voice call back. They tell you to wait there, and you are greeted by two miners. They ask you if you're lost, which you confirm. They nod and drive you home, and everything is back to normal.")
        print("<----ENDING 7--->")
    elif num == 8:
        time.sleep(0.5)
        print("You hold out your thumb for anyone who drives by. Someone finally pulls up to let you in, and after a short conversation they bring you home. You get back home knowing you made a new friend.")
        print("<----ENDING 8--->")
    elif num == 9:
        time.sleep(0.5)
        print("You start the long trek in a straight line, cars occasionally passing by. Eventually, you find a rest stop. You walk into the conveniece store and tell the clerk there of your situation. The clerk shrugs and offers to take you home after her shift. You make it back home with a new friend.")
        print("<----ENDING 9--->")
    elif num == 10:
        time.sleep(0.5)
        print("You find that after an even longer walk, the town you live in is just a little ways away. You simply never went this way or never recognized anything here. You eventually make it home after what feels like two hours total of walking. You're sore, but you're now safe.")
        print("<----ENDING 10--->")
    elif num == 11:
        time.sleep(0.5)
        print("You walk past the gate and into the building. Before you can talk to anyone, a guard approaches you with a stern look. He tells you that you're tresspassing. You explain that you don't know where you are, and you need a drive home. He calls the police, getting you a ride home from them. You didn't go to jail, thankfully.")
        print("<----ENDING 11--->")
    elif num == 12:
        time.sleep(0.5)
        print("You find a car in the parking lot. This is definitely illegal, but you're already tresspassing and you're a little desperate. You take the car and drive home. Not wanting to be an idiot, you park the car somewhere nearby instead of in your driveway. The next day, you're greeted by two cops. You say you don't know anything, clearly lying. Unfortunately, the car had a camera in it, and you're sent to prison for theft.")
        print("<----ENDING 12--->")

while True:
    xChoice = input("You wake up in a pitch black forest, no recollection of how you ended up in such a place. Before you is a box of MATCHES and a FLASHLIGHT You pick up the metal flashlight, and the box of matches. For now, you put the matches in your pocket, and push the button to turn the flashlight on. As the area in front of you illuminates, you realize after pocketing the matches that you're in clothes that aren't your own: As you turn the flashlight on yourself, you see that you're in a gray jumpsuit and heavy boots. You appear to be in the center of a dirt pathway. Directions leading LEFT and RIGHT. Additionally, there appears to be a direction FORWARD that leads to the distant mouth of a cave. Which direction will you go? ")

    # DIRECTIONS OPTIONS ------------------------------------------------
    if xChoice.upper() == "LEFT":
        time.sleep(0.5)
        while True:
            cabinChoice = input("After what feels like 10 minutes, you find a cabin with only one candle lit on the porch. At the door you find a sign that asks you to knock in rather crude handwriting. Do you KNOCK, or SNEAK inside? ")
            # CABIN OPTIONS ------------------------------------------------------
            if cabinChoice.upper() == "KNOCK":
                time.sleep(0.5)
                while True:
                    inCabinChoice = input("You shakily knock on the door, and after a while, you hear footsteps for the door that soon opens, as you see the person, you immediately question whether or not you should run. The 8-foot tall person at the door is in rugged, mildly dilapidated clothes and a haniwa mask. The person stares at you, waiting for you to speak. Do you SPEAK, or do you RUN? ")
                    # CABIN MAN OPTIONS ------------------------------------------------------
                    if inCabinChoice.upper() == "SPEAK":
                        ending(1)
                        break
                    elif inCabinChoice.upper() == "RUN":
                        ending(2)
                        break
                    else:
                        print(invalidText)
            elif cabinChoice.upper() == "SNEAK":
                ending(3)
                break
            else:
                print(invalidText)
        # CAR OPTIONS ------------------------------------------------------
    elif xChoice.upper() == "RIGHT":
        time.sleep(0.5)
        while True:
            carChoice = input("You begin walking to the right, and soon find a car with the engine still running. The keys are in the ignition, and the door is open slightly. Do you WAIT for the owner of the car, or DRIVE out of the forest? ")
            if carChoice.upper() == "WAIT":
                ending(4)
                break
            elif carChoice.upper() == "DRIVE":
                ending(5)
                break
            else:
                print(invalidText)
        # CAVE OPTIONS ------------------------------------------------------
    elif xChoice.upper() == "FORWARD":
        time.sleep(0.5)
        while True:
            caveChoice = input("You trek past the trees, and find the mouth of a cave. Inside the cave, you hear a rhythmic, metallic clang from deep within. Do you ENTER, CALL to see if you get a response, or LEAVE to go past it? ")
            if caveChoice.upper() == "ENTER":
                ending(6)
                break
            elif caveChoice.upper() == "CALL":
                ending(7)
                break
            elif caveChoice.upper() == "LEAVE":
                time.sleep(0.5)
            # ROAD OPTIONS ------------------------------------------
            while True:
                roadChoice = input("You go past it, realizing a cave is probably not the place to explore without proper equipment. You keep walking through the forest and find some road. You have a few ideas: You can either HITCHHIKE, walk LEFT alongside the road, or walk RIGHT alongside the road. ")
                if roadChoice.upper() == "HITCHHIKE":
                    ending(8)
                    break
                elif roadChoice.upper() == "LEFT":
                    ending(9)
                    break
                elif roadChoice.upper() == "RIGHT":
                    time.sleep(0.5)
                # FACTORY OPTIONS -----------------------------------
                while True:
                    factoryChoice = input("You start your walk down the right side of the road, and eventually come across some sort of industrial building. It's not the best look to be by a factory in the dead of night. Do you keep WALKing, ENTER the facility in hopes of finding someone, or do you SNEAK in to find another way of getting home? ")
                    if factoryChoice.upper() == "WALK":
                        ending(10)
                        break
                    elif factoryChoice.upper() == "ENTER":
                        ending(11)
                        break
                    elif factoryChoice.upper() == "SNEAK":
                        ending(12)
                        break
                    else:
                        print(invalidText)
                else:
                    print(invalidText)
            else:
                print(invalidText)
    else:
        print(invalidText)