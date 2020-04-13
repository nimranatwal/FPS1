"""

Make a game of rock, paper, scissors against the computer.

Problem
    Tell the user about the game instruction
    Tell user to enter either rock, paper or scissor
    Get the response from the user
    
    Generate a random chouce from (rock, paper, scissor)
    Compare user selection and computer selection
    Display who wins.
    
Extension
    Make sure the user enters a valid entry.
    Add a loop structure to play several times and 
    Make 
"""

print("GAME INSTRUCTIONS: ")
print("")
print("Rock vs Paper -> Paper Wins")
print("Rock vs Scissor -> Rock Wins")
print("Scissor vs Paper -> Rock Wins")

import random
while True:
    
    print("Enter choice \n 1.Rock \n 2. Paper \n 3. Scissor")
    user_choice = input("Enter your choice: ")
    user_choice = user_choice.lower()
    print("User Choice: " + user_choice)
    
    while True:
        if user_choice not in ['rock', 'paper', 'scissor']:
            print("Invalis input, please enter valid input")
        else:
            break
    
    
    comp_choice = random.choice('rock', 'paper', 'scissor')
    print("Computer Choice: " + comp_choice)
    
    result = None
    
    if ((user_choice == 'rock' and comp_choice == 'paper') or 
        (user_choice == 'paper' and comp_choice == 'rock')):
        result = 'paper'
    
    elif((user_choice == 'rock' and comp_choice == 'scissor') or 
        (user_choice == 'scissor' and comp_choice == 'rock')):
        result = 'rock'
    else:
        result = 'scissor'
        
        
    if(comp_choice == user_choice):
        print("Draw")
    elif(result == user_choice):
        print("User Wins")
    else:
        print("Computer Wins")
        
    
    choice = input("Do you want to play again? Enter n for no and y for yes: ")
    
    if(choice == 'n' or choice == 'N'):
        break
        
    else:
        continue

print("Thank you for playing the game")
        