import random

# save Ascki in variables
rock_ascki = """
👊
"""
peper_ascki = """
✋
"""
scissors_ascki ="""
✌
"""



print("Welcome to the Rock, Peper, Scissors game:")
confirm = input("Press Enter to continue or type (Help) for the rules: ").lower()
if confirm == "help" :
    print("""
******** Rules *********
1) You choose and the computer chooses
2) Rock smashes Scissors -> Rock wins
3) Scissors cut Peper ->Scissors win
4) Peper covers Rock -> Peper wins                  
""")
    
user_choice = input("Enter your choice (rock, peper, scissors): ").lower()
if user_choice in ['rock','peper','scissors'] :

    # Display user choice in Asckii
    if user_choice == 'rock' :
        print(f"\nYou choice:\n{rock_ascki}")
    elif user_choice == 'peper' :
        print(f"\nYou choice:\n{peper_ascki}")
    else :
        print(f"\nYou choice:\n{scissors_ascki}")
else :
     print("invalid choice. Please run the progrm again and choose rock, pepre, or scisors")  

# computer choice
computer_choice = random.choice(['rock','peper','scissors'])
if computer_choice == 'rock' :
        print(f"\nComputer choice:\n{rock_ascki}")
elif computer_choice == 'peper' :
        print(f"\nComputer choice:\n{peper_ascki}")
else :
        print(f"\nComputer:\n{scissors_ascki}")

     
# Detrnine the winner
if(
user_choice == "rock"  and computer_choice == "scissors"  
or
user_choice == "scissors"  and computer_choice == "peper"
or     
user_choice == "peper"  and computer_choice == "rock"    
) :
    print(f"You win! {user_choice} beats {computer_choice}")

elif computer_choice == user_choice :
    print("It's a tie!")
else :
    print(f"You lose! {user_choice} beats {computer_choice}")

