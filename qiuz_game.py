print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
 
print("Okay lets play :)")
score = 0
answer = input ("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 2
else:
    print("incorrect!")

answer = input ("Which province is Durban located? ")
if answer.lower() == "kzn":
    print('correct!')
    score += 2
else:
    print("incorrect!")
    
answer = input ("How many football world cups does brazil have? ")
if answer.lower() == "five":
    print('correct!')
    score += 2
else:
    print("incorrect!")
    
answer = input ("Who was the first black president in South Africa? ")
if answer.lower() == "nelson mandela":
    print('correct!')
    score += 2
else:
    print("incorrect!")

print ("You got " + str(score) + " questions correct!")
print ("You got " + str((score / 4) * 100) + "%.")

    


