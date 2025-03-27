name = input("Hey! Please type your name: ")
print("Hello " + name + " Welcome to the game!")

should_we_play = input("Do you want to play the game? ").lower()

if   should_we_play == "y" or should_we_play == "yes":
    print("Great! Let's start.")
    
    direction = input("What direction do you want to go left or right? ").lower()
    if direction == "left":
        print("Okay We've went left and fell off the ground, game over and try again.")
    elif direction == "right":
        print("Okay We've went right")
        choice = input("You now see a bridge, do you want to swim under it or cross it? (swim/cross) "
            ).lower()
        if choice == "swim":
            print("Opps! You've been eaten by the crocodiles and died in the game!")
        elif choice == "cross":
            print("Congratulations! You've crossed the bridge and passed on to the new chapter of  game!")
        else:
            print("Sorry not a valid choice, You didn't enter. Play again.")
    else:
        print("Sorry not a valid direction, You didn't enter. Play again.")
else:
    print("Goodbye!")
    exit()
    