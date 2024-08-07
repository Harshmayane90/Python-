# rock paper scirror
import random
player=input("Enter your choice (rock, paper, scissor): ")
computer = random.choice(['rock', 'paper', 'scissor'])
print(f"Computer choose {computer} and user choose {player}")
if player not in['rock', 'paper', 'scissor']:
        print("Invalid choice! Please enter rock, paper, or scissor.")
while True:
        if player=='rock' and computer=='scissor':
            print("player won")
        elif player=='paper' and computer=='rock':
            print("Player won")
        elif player=='scissor' and computer=='paper':
            print("player won")
        elif computer=='rock' and player=='scissor':
            print("computer won")
        elif computer=='scissor' and player=='paper':
            print("computer won")
        else:
            print("Its A Tie!")
        Play_agian=input("Choose y or n:")
        print("You choose n",Play_agian=='n')       
        break



# # Guess game
# i = 35
# guess = 0
# while  guess <=5:
#     n = int(input("Enter the Number: "))
#     if i<n:
#         print("Your guess is wrong. The entered number is greater.")
#     elif i>n:
#         print("Your guess is wrong. The entered number is smaller.")   
#     else:
#         print("You are right!")
#         break
#     print(f"You have {5 - guess} chances left")
#     guess += 1
#     if guess >5:
#         print("Sorry, you have 0 chances left.")

# # Age calculator
# a=int(input("Enter the current day: "))
# b=int(input("Enter the current month"))
# c=int(input("Enter the current year: "))
# x=int(input("Enter the Birth date : "))
# y=int(input("Enter the Birthday month: "))
# z=int(input("Enter the Birthday year: "))
# print("---------Age calculated------------")
# print(f" Your age is: {c-z}Year,{b-y}Month,{a-x}days")
    

# # #Atm machine
# n=15000
# i=float(input("Enter the amount to be withdraw: "))
# print(f"The cash wishrawed {i}")
# avilable_balance=(n-i)
# print(f"Avilable Balance is: {avilable_balance}")

# if i>n:
#     print("Insuffcient balance")
# else:
#     print("Cash withdrawed")
    
# j=int(input("enter the amount to be deposit: "))
# deposited_amount=(n+j)
# print(f"Avialble balance is: {deposited_amount}")






