# This will be my final project for class
# It's a simple password decoder / breaker

import random
number = int(input("Input a number that is a password: "))
guess = 0
while (guess != number):
   guess = random.randint(0,9999)
   print(guess)
print("Your password is " + str(number))

# This code will run until it finds your password !!!
# ----------------------------------------------------------------------------------------------------------
# This next simple password decoder / breaker has both letters and numbers

# import random
# character = "0123456789abcdefghijklmnopqrstuvwxyz"
# character_list = list(character)
# password = input("Enter your password: ")
# guess = ""
# while (guess != password):
     # guess = random.choices(character_list,k=len(password))
     # print(guess)
     # guess = "".join(guess)
     # print("your password is " + guess)

# I hope you enjoy this Justin try it out :)

# this code was sited from Johnathan Karr on youtube https://www.youtube.com/watch?v=P5Lt8J3_ZnI
# I will separate both programs using --------- so just comment the other one out when using the other so
# there is no conflicts when running one or the other.
