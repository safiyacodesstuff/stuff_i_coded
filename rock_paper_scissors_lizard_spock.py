#hi :)

#designing the user interface:
print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")
print("1) ✊ Rock")
print("2) ✋ Paper")
print("3) ✌️ Scissors")
print("4) 🦎 Lizard")
print("5) 🖖 Spock")

#the player picks a number:
player=int(input("Pick a number:"))

#the computer picks a number:
from random import randint
computer=randint(1,5)

print("") #this is just for design haha :)

#determine the winner of the game:
if player<=5:
    
    #the player chose rock:
    if player==1 and computer==1:
        print("You chose: ✊")
        print("The computer chose: ✊")
        print("You both chose Rock, it's a tie!")
    elif player==1 and computer==2:
        print("You chose: ✊")
        print("The computer chose: ✋")
        print("Paper covers Rock, the computer wins!")
    elif player==1 and computer==3:
        print("You chose: ✊")
        print("The computer chose: ✌")
        print("Rock smashes Scissors, you win!")
    elif player==1 and computer==4:
        print("You chose: ✊")
        print("The computer chose: 🦎")
        print("Rock crushes Lizard, you win!")
    elif player==1 and computer==5:
        print("You chose: ✊")
        print("The computer chose: 🖖")
        print("Spock vaporizes Rock, the computer wins!")
    
    #the player chose paper:
    elif player==2 and computer==1:
        print("You chose: ✋")
        print("The computer chose: ✊")
        print("Paper covers Rock, you win!")
    elif player==2 and computer==2:
        print("You chose: ✋")
        print("The computer chose: ✋")
        print("You both chose Paper, it's a tie!")
    elif player==2 and computer==3:
        print("You chose: ✋")
        print("The computer chose: ✌")
        print("Scissors cut Paper, the computer wins!")
    elif player==2 and computer==4:
        print("You chose: ✋")
        print("The computer chose: 🦎")
        print("Lizard eats Paper, the computer wins!")
    elif player==2 and computer==5:
        print("You chose: ✋")
        print("The computer chose: 🖖")
        print("Paper disproves Spock, you win!")
    
    #the player chose scissors:
    elif player==3 and computer==1:
        print("You chose: ✌️")
        print("The computer chose: ✊")
        print("Rock crushes Scissors, the computer wins!")
    elif player==3 and computer==2:
        print("You chose: ✌️")
        print("The computer chose: ✋")
        print("Scissors cut Paper, you win!")
    elif player==3 and computer==3:
        print("You chose: ✌️")
        print("The computer chose: ✌")
        print("You both chose Scissors, it's a tie!")
    elif player==3 and computer==4:
        print("You chose: ✌️")
        print("The computer chose: 🦎")
        print("Scissors decapitate Lizard, you win!")
    elif player==3 and computer==5:
        print("You chose: ✌️")
        print("The computer chose: 🖖")
        print("Spock smashes Scissors, the computer wins!")
    
    #the player chose lizard:
    elif player==4 and computer==1:
        print("You chose: 🦎")
        print("The computer chose: ✊")
        print("Rock crushes Lizard, the computer wins!")
    elif player==4 and computer==2:
        print("You chose: 🦎")
        print("The computer chose: ✋")
        print("Lizard eats Paper, you win!")
    elif player==4 and computer==3:
        print("You chose: 🦎")
        print("The computer chose: ✌")
        print("Scissors decapitate Lizard, the computer wins!")
    elif player==4 and computer==4:
        print("You chose: 🦎")
        print("The computer chose: 🦎")
        print("You both chose Lizard, it's a tie!")
    elif player==4 and computer==5:
        print("You chose: 🦎")
        print("The computer chose: 🖖")
        print("Lizard poisons Spock, you win!")
    
    #the player chose spock:
    elif player==5 and computer==1:
        print("You chose: 🖖")
        print("The computer chose: ✊")
        print("Spock vaporizes Rock, you win!")
    elif player==5 and computer==2:
        print("You chose: 🖖")
        print("The computer chose: ✋")
        print("Paper disproves Spock, the computer wins!")
    elif player==5 and computer==3:
        print("You chose: 🖖")
        print("The computer chose: ✌")
        print("Spock smashes Scissors, you win!")
    elif player==5 and computer==4:
        print("You chose: 🖖")
        print("The computer chose: 🦎")
        print("Lizard poisons Spock, the computer wins!")
    elif player==5 and computer==5:
        print("You chose: 🖖")
        print("The computer chose: 🖖")
        print("You both chose Spock, it's a tie!")

#the player chose a number above 5
else:
    print("Invalid input!")