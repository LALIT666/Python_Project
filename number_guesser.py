import random

# r = random.randrange(-5, 11) #upto 11 but not 11 excluding 11 

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range) # it is just going to convert top_of_range in int 

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time. ")
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,top_of_range) #indlude 11 
guessess = 0

while True:
    guessess +=1
    user_guess = input ("Make a guess: ")

    if user_guess.isdigit():
        user_guess= int(user_guess) # it is just going to convert top_of_range in int 

    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!") 
        break
    
    elif user_guess > random_number:
        print("You are the above the number")
    else:
        print("You were below the number!")
    

print("You got it in", guessess,"guessess") # comma laga kar karo toh aacah hota hai 
