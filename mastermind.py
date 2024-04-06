import random

# get_next_guess checks if the number that has been put in by the user is a valid one 
def get_next_guess():
    number = int(input(""))
    while number < 1111 or number > 9999:
        print("Invalid input! Please try again:")
        number = int(input(""))
    return(number)

# split_digits splits up the digits into individual items of a list
def split_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return digits[::-1]

# compare_numbers compares the two numbers to find the correct number of black and white markers
def compare_numbers(random_number, user_input):
    numberOfDigitsRN = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # this list will save the frequency of occuring digits in random_number (the RN in numberOfDigitsRN stands for random number)
    for i in range(4):
        numberOfDigitsRN[random_number[i]]+=1 # for every digit that is in random_number, the corresponding list index will go up by 1 --- e.g.: if random_number = [8, 8, 1, 2] then NumberOfDigitsRN = [0, 1, 1, 0, 0, 0, 0, 0, 2, 0]
        
    numberOfDigitsUI = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # see above (The UI in numberOfDigitsUI stands for user input)
    for i in range(4):
        numberOfDigitsUI[user_input[i]]+=1 # see above
        
    numberOfWhiteMarkers = 0
    for i in range(10):
        numberOfWhiteMarkers += min(numberOfDigitsRN[i], numberOfDigitsUI[i]) # finds the number of white markers by comparing both lists item by item, saving the minimum for every match it finds and then adding them up --- e.g.: if NumberOfDigitsRN = [0, 1, 1, 0, 0, 0, 0, 0, 2, 0] and NumberOfDigitsUI = [0, 2, 0, 0, 1, 0, 0, 0, 1, 0] then the minimum of each index would look as follows: [0, 1, 1, 0, 1, 0, 0, 0, 1, 0] } now that is summed up and we get numberOfWhiteMarkers = 4 

    numberOfBlackMarkers = 0 # finds the number of black markers by comparing both lists item by item and increasing the counter by 1 for every match that is found
    for i in range (4):
        if random_number[i] == user_input[i]:
            numberOfBlackMarkers += 1

    numberOfWhiteMarkers_final =  numberOfWhiteMarkers - numberOfBlackMarkers # determines the true amount of white markers by subtracting the black ones from the white ones (a digit can't be marked as both black and white)
    return(numberOfWhiteMarkers_final + numberOfBlackMarkers*10) # the function returns a number that can later be used to access the amount of black and white markers seperately without having to run the function multiple times

random_number = []
for i in range(4): # here we determine the random number the user has to guess and store its digits as a list
    random_number.append(random.randint(1,9))
secret_number = int("".join(map(str, random_number))) # this joins the list items into an integer to later display a whole number to the user as opposed to the list

# this marks the actual beginning of the game
print("Welcome to Mastermind! Let's find out if you are one!")
print("Before you enter your first guess, please note that your number can only consist of 4 digits and cannot contain any zeros.")
print("Now, please enter your first guess: ")
guess = get_next_guess()
counter = 1
user_input = split_digits(guess)

if secret_number == guess:
    print("Congratulations, you guessed it! And on your first guess too! That's very impressive!")
    print("You definitely are a Mastermind!")
    
while random_number != user_input:
    if counter == 10:
        print("You did not guess the number correctly :(")
        print("The right answer was", secret_number)
        print("Better luck next time!")
        quit()
        
    results = compare_numbers(random_number, user_input)
    print("Number of correctly placed digits:", results//10) # we devide results by 10 to undo the very last step of the compare_numbers function
    print("Number of digits that are in the number, but not in their correct place yet:", results%10) # we calculate results modulo 10 to undo the very last step of compare_numbers
    counter += 1
    print("----- Try #", counter, "-----")
    print("Enter your next guess: ")
    guess = get_next_guess()
    user_input = split_digits(guess)            
        
print("Congratulations, you guessed it! You must be a true Mastermind!")