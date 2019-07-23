def getans(quest,max):
    inp = False
    while inp==False:
        storyPart = input(quest)
        try:
            storyPart = int(storyPart)
        except:
            print("bad input")
            continue
        if storyPart <= max:
            inp = True
        else:
            print("bad input")
    return storyPart



storyPart = False
while storyPart==False:
    print("once opon a time, there was a __")
    storyPart = getans("would you like to be: 1: a knight 2: a princess 3: a dragon : ",3)

    if storyPart==1:
        print("one day, as he was riding along the road, he saw a __")
        storyPart = getans("what did he see? 1: a troll 2: an enemy knight 3: a messenger : ",3)
        if storyPart==1:
            print("when he saw the troll, he immediately lowered his lance, and __")
            storyPart = getans("did he 1: win 2: die : ",2)
            if storyPart==1:
                print("then with a mighty blow, he struck the troll down. the end.")
                storyPart = True
            elif storyPart==2:
                print("then with a mighty blow, the troll struck him down. the end.")
                storyPart = True
        elif storyPart==2:
            print("when the enemy knight saw him, he shouted 'halt, you shal not pass until you pay me or fight me' the knight then __")
            storyPart = getans("did he 1: pay him 2: fight",2)
            if storyPart==1:
                print("he payed, and the enemy knight let him pass. then all of a sudden, the knight felt a sharp pain between his shoulders, and died.")
                storyPart = True
            elif storyPart==2:
                print("they fought, and the enemy knight in the end killed the knight with a striking blow to the head. the end.")
                storyPart = True

        elif storyPart==3:
            print("when he saw the messenger, he shouted 'where are you going?' he answered 'I have been looking for you. lord Andrake is under attack' then the knight __")
            storyPart = getans("did the knight 1: identify the messenger as an enemy 2: go immediately with the messenger 3: go to get backup",3)
            if storyPart==1:
                print("the knight suddenly drew his dagger and stabbed the messenger in the heart, but the messenger was wearing armor, and he stabbed the knight in the throat. the end")
                storyPart = True
            elif storyPart==2:
                print("they rode and rode and finally arrived at the castle and as they rode in, the chanselor ran down to them and brought them to the king, and the king shot the knight in the face")
                storyPart = True
            elif storyPart==3:
                print("as the knight turned to go to the castle, he felt a sharp pain between his shoulders, and he died. the end.")
                storyPart = True

    if storyPart==2:
        print("one day as she was playing in the court yard, a __ came and took her away to a faraway castle")
        storyPart = getans("what was taken by 1: a wizard 2: a witch 3: a dragon",3)
        if storyPart==1:
            print("then the wizard told her 'you are to stay here and make me rope' and so she made ropes for years until she desided to __")
            storyPart = getans("what did she do 1: stop making ropes 2: tie the ropes together to make them long enough to clime out her window 3: strangle the wizard in his sleep",3)
            if storyPart==1:
                print("when the wizard came and saw that she had stopped, he said 'why did you stop? please don't' then he __")
                storyPart = getans("what did the wizard do 1: he turned into a ball of energy 2: he made a fireball 3: he turned into a man in a yellow suit, covered in lightning",3)
                if storyPart==1:
                    print("then he transformed back into a wizard and said 'do not stop until I say you may.'then she continued to make ropes until the wizard brought a skeleton to her room and said 'your parents have sent a knight. this is all that remains' more and more knights came, and each ended the same way. then one night she heard a creak come from her door, and she saw a knight. he waved to her to come with him, and he gave her a sword. then they crept down the stairs until they reached a floor, and they __")
                    storyPart = getans("did they 1: get speared by giant spikes that magically erupted from the floor 2: get incinerated by magical fire 3: get teleported to an alternate universe were they starved 4: explode 5: get their hearts ripped to shreds by the man in the yellow suit",5)
                    if storyPart==1:
                        print("they then walked across a booby trapped area and they were speared by giant spikes. the end")
                        storyPart = True
                    elif storyPart==2:
                        print("they then walked across a booby trapped area and they were incinerated by fire")
                        storyPart = True
                    elif storyPart==3:
                        print("they then walked across a booby trapped area and they were teleported to alternate universes and died")
                        storyPart = True
                    elif storyPart==4:
                        print("they then walked across a booby trapped area and they were exploded")
                        storyPart = True
                    elif storyPart==5:
                        print("they then started walking towards the next staircase and then suddenly saw a flash of red and they saw a man in a yellow suit, and he shoved his hands into their chests, ripping thier hearts apart. the end.")
                        storyPart = True
                elif storyPart==2:
                    print("then he transformed back into a wizard and said 'do not stop until I say you may.'then she continued to make ropes until the wizard brought a charred suit of armor that clearly had a body in it. he said 'this is what will happen to all who try to take you. if you wish to save dozens of lives, you will tell your parents not to send any more knights'. then she __")
                    storyPart = getans("did she 1: write to her parents in hope that they would listen, and she could save the lives of many knights 2: refuse in hopes that one of the knights would be able to save her 3: agree, but actually give instructions on how to get her",3)
                    if storyPart==1:
                        print("her parents did not listen. many more knights came, each meeting the same end as the first. finally one day, the wizard came to her room, and said 'you are to be sent back to your parents.' then she was escorted to a horse carriage where she was__")
                        storyPart = getans("was she 1: killed by a spike that came out of the back of her seat 2: incinerated by a flame that came from her seat 3:killed by getting her heart ripped to shreds by the man in the yellow suit 4: killed by falling through a portal and hitting her parents parents floor",4)
                        if storyPart==1:
                            print("as she sat down, all of a sudden, a spike shot out of her seat and through her heart. the end.")
                            storyPart = True
                        elif storyPart==2:
                            print("as she sat down, all of a sudden, a giant flame incinerated her. the end.")
                            storyPart = True
                        elif storyPart==3:
                            print("when she sat down, the wizard disapeared, and half a second later, the man in the yellow suit shoved his hand into her heart. the end.")
                            storyPart = True
                        elif storyPart==4:
                            print("as she sat down a portal opened below her, and she fell through, and she fell, and fell then she saw a light in the dark, and she fell into it and she fell broken onto her parents' court room floor. the end")
                            storyPart = True
                    elif storyPart==2:
                        print("many more knights came, each dying one way or another. then one day, an army came, and for several days the wizard and the princess's parents' army fought. then, on the ninth day, the wizard took the princess to the highest tower and shouted down 'leave now, and never come back, or I will __'")
                        storyPart = getans("what did the wizard threaten to do 1: drop her 2: cut of her head 3: inject her with liquid evil 4: rip her heart out")
                        if storyPart==1:
                            storyPart = getans("did her parents 1: stand down 2: laugh and say'you don't have the streangth! none ever have.'")
                            if storyPart==1:
                                print("the king said'fine. you win.' then the wizard dropped her. the end.")
                                storyPart = True
                            elif storyPart==2:
                                print("then he dropped her. the end")
                                storyPart = True
                        elif storyPart==2
                            storyPart = getans("did her parents 1: stand down 2: laugh and say'you don't have the streangth! none ever have.'")
