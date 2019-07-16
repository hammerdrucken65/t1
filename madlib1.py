story=("there once was a [TO]"
       " who [TO] on a [TO]"
       " then it [TO] like the [TO] thing that it was")
noun=input("please enter noun: ")
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