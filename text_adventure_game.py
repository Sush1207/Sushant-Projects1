# text_adventure_game.py

def introduction():
    print("Welcome to the Magical Quest!")
    print("You are a brave adventurer on a quest to find the legendary Crystal of Power.")
    print("Your journey begins now.")

def choose_path():
    print("You find yourself at a crossroads.")
    print("1. Take the left path.")
    print("2. Take the right path.")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def left_path():
    print("You chose the left path and encounter a mystical forest.")
    print("After navigating through the forest, you find a hidden cave.")
    choice = input("Enter the cave or continue through the forest? (cave/forest): ")

    if choice.lower() == 'cave':
        print("Congratulations! You found the Crystal of Power. You are victorious!")
    else:
        print("You journey deeper into the forest but get lost. The adventure ends here.")

def right_path():
    print("You chose the right path and come across a raging river.")
    print("You decide to build a makeshift raft and cross the river.")
    print("The river leads you to a magical meadow where the Crystal of Power awaits!")
    print("Congratulations! You are victorious!")

def main():
    introduction()
    path = choose_path()

    if path == '1':
        left_path()
    elif path == '2':
        right_path()
    else:
        print("Invalid choice. The adventure ends here.")

def play_game():
    while True:
        main()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_game()
