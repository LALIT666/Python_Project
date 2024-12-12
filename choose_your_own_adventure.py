#iss game ko jitna marji bada kar sakatae ho ..


name = input("type your name : ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ").lower()
    if answer == "swim":
        print("You swim across and were eaten by an alligator")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost your life and the game as well!! 😂🤣")
    
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back? (cross/back) ").lower()

    if answer == "back":
        print("You go back and lose.")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them or not? (yes/no) ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you an elixir, and you WIN!")
        elif answer == "no":
            print("You decide not to talk to the stranger. They get offended and kill you. You lose!")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thankyou for trying my game" + name )
