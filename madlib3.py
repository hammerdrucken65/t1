validStory=False
while validStory==False:
    print("in while loop")
    storyVersion=input("would you like story 1, 2 or 3? : ")
    try:
        storyVersion=int(storyVersion)
        print("yay")
    except:
        print("bad input")
        continue
    if storyVersion==1:
        story=("there once was a [TO]"
               " who [TO] on a [TO]"
               " then it [TO] like the [TO] thing that it was")
        noun=input("please enter a noun: ")
        verb=input("please enter verb: ")
        noun2=input("please enter noun: ")
        verb2=input("please enter verb: ")
        adjective=input("please enter adjective: ")
        story=story.replace("[TO]", noun, 1)
        story=story.replace("[TO]", verb, 1)
        story=story.replace("[TO]", noun2, 1)
        story=story.replace("[TO]", verb2, 1)
        story=story.replace("[TO]", adjective, 1)
        print(story)
        validStory=True
    elif storyVersion==2:
        story=("a long [BEN] ago, in a [BEN] [BEN] [BEN] away, I was on a [BEN] with princess [BEN]"
               " we were [BEN]ing through space, when the Empire started bording us! we were quite [BEN]."
               " as our [BEN] were [BEN] the [BEN], [BEN][BEN]-[BEN][BEN] and I decided that it would be a good idea to walk [BEN]ly across the [BEN]"
               " then R2-D2 got in an [BEN], and we flew to a [BEN] were we ended up getting [BEN]ed")
        noun=input("please enter noun: ")
        noun2=input("please enter noun: ")
        adverb=input("please enter adverb: ")
        adverb2=input("please enter adverb: ")
        noun3=input("please enter noun: ")
        properNoun=input("please enter proper noun: ")
        verb=input("please enter verb: ")
        emotion=input("please enter emotion: ")
        pluralNoun=input("please enter plural noun: ")
        verb2=input("please enter verb: ")
        pluralNoun2=input("please enter plural noun: ")
        letter=input("please enter letter: ")
        number=input("please enter number: ")
        letter2=input("please enter letter: ")
        number2=input("please enter number: ")
        adjective=input("please enter ajective: ")
        noun4=input("please enter noun: ")
        noun5=input("please enter noun: ")
        place=input("please enter place: ")
        verb3=input("please enter verb: ")
        story=story.replace("[BEN]", noun, 1)
        story=story.replace("[BEN]", noun2, 1)
        story=story.replace("[BEN]", adverb, 1)
        story=story.replace("[BEN]", adverb2,1)
        story=story.replace("[BEN]", noun3, 1)
        story=story.replace("[BEN]", properNoun, 1)
        story=story.replace("[BEN]", verb, 1)
        story=story.replace("[BEN]", emotion, 1)
        story=story.replace("[BEN]", pluralNoun2, 1)
        story=story.replace("[BEN]", verb2, 1)
        story=story.replace("[BEN]", pluralNoun2, 1)
        story=story.replace("[BEN]", letter, 1)
        story=story.replace("[BEN]", number, 1)
        story=story.replace("[BEN]", letter2, 1)
        story=story.replace("[BEN]", number2, 1)
        story=story.replace("[BEN]", adjective, 1)
        story=story.replace("[BEN]", noun4, 1)
        story=story.replace("[BEN]", noun5, 1)
        story=story.replace("[BEN]", place, 1)
        story=story.replace("[BEN]", verb3, 1)
        print(story)
        validStory=True
    elif storyVersion==3:
        story=("my [MEEP] [MEEP]ed the [MEEP]")
        noun=input("please enter noun: ")
        verb=input("please enter verb: ")
        noun2=input("please enter noun: ")
        story=story.replace("[MEEP]", noun, 1)
        story=story.replace("[MEEP]" , verb, 1)
        story=story.replace("[MEEP]" , noun2, 1)
        print(story)
        validStory=True
    else:
        print("you are a bad person")
        validStory=False
print("end")