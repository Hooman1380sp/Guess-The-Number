from random import randint
from termcolor import colored


print("--- start ---") 

number_system = randint(1, 15)

opportunity = 5

print(f"Your opportunities: {opportunity}")
while opportunity > 0:
    number_user = int(input("Enter your number: "))
    if number_user == number_system:
        print(colored("Your answer is correct!", "green"))
        continuation = input(colored("Do you want to continue? (y - n)   "   , "yellow"))
        if continuation == "y":
            opportunity = 5
            number_system = randint(1, 15)
            print(f"Your opportunities: {opportunity}")
        elif continuation == "n":
            print("--- Finished ---")
            break
    else:
        opportunity -= 1
        print(colored(f"Your answer is incorrect!  Your opportunities: {opportunity}", "red"))
        if ((number_user - (1 or 2 or 3) or number_user + (1 or 2 or 3)) == number_system) and (opportunity > 0):
            print("You are near!")
        if opportunity == 0:
            print("--- Finished ---")