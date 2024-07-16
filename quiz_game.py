print("welcome to the quiz game ")
play = input("Do you want to play? ")
if play.lower()  != "yes":
    quit()
score = 0
print("okay lets play ")
answer = input("what does the Cpu stand for ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")
answer = input("what does the ayw stand for ")
if answer.lower() == "as you wish":
    print("correct")
    score += 1
else:
    print("incorrect")
answer = input("what does the cal stand for ")
if answer.lower() == "calender":
    print("correct")
    score += 1
else:
    print("incorrect")
print("you got " + str(score) + " questions correct")
