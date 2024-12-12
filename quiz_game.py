print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")  # user se input leta hai 

if playing.lower() != "yes":  # unser ke input ko lower case me convert karta hai and .upper() upper case me 
    quit()

print("Okay! Let's play :)")
score = 0

# Question 1
answer = input("What is the full form of CPU? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("What is the full form of GPU? ").lower()
if answer == "graphics processing unit":  
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What is the full form of RAM? ").lower()
if answer == "random access memory":  
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Display the final score
print("You got " + str(score) + " question(s) correct!")
print("You scored " + str((score / 3) * 100) + "%.")  
