import random                                                   #this is a module

top_of_range = input("Type a number: ")

if top_of_range.isdigit():                                     #check input if it digit for convertion  
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
        print('Please type a number next time.')
        quit()

random_number = random.randint(0, top_of_range)                 #randrange(11) generate no 0-10,(-5,11) generate -5,10, randint includes 11

guesses = 0

while True:
    guesses += 1                                                     #ask user to keep guesing till it correct
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():                                    #check input if it digit for convertion  
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')                #Number i typed has to be number im going to guess
        continue

    if user_guess == random_number:                             #if guessed number equal to random no.
        print("You got It!")
        break                                                   #after u got number right loop end
    elif user_guess > random_number:
        print('You were above the number!')
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")