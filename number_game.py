import random
top_of_input = input("type a number: ")

if top_of_input.isdigit():
    top_of_input = int(top_of_input)
    if top_of_input <= 0:
        print("please type a number larger than 0 next time")
        quit()
else:
    print("please a type a number next time")
    quit()
        
random_number = random.randint(0, top_of_input)
guesses = 0 
while True:
    guesses += 1
    user_guess = input("make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time")
        continue

    if user_guess == random_number:
        print("you got it")
        break
    else:
        if user_guess > random_number:
            print("you were above the number!")
        else:
            print("you were below the number")
            
print("you got it in", guesses, "guesses")
