import random 
user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    options = [ "rock","paper","scissors" ] # list 
    options[0]
    if user_input not in options:
        continue # continue agae ka code run hone nahi deta wo wapas bhej deta hai matlab ki iss case me wo code ko phir is user ke pass input lene ke liye bhej dega 
    
    random_number = random.randint(0,2)
    #rock: 0 , paper: 1 ,scissor: 2
    computer_pick = options[random_number]
    print("Computer picked",computer_pick + ".")

    #condition 1 
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        

    #condition 2
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        

    #condition 3
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    
    #conditon 4
    elif user_input == computer_pick:
        print("Computer picks the same",user_input,computer_pick)
        
    else:
        print("You lost!")
        computer_wins += 1
    


print("You won",user_wins,"times.")
print("the computer won",computer_wins,"times.")
print("Good bye!")