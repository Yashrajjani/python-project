#number guessing game

import random
print("hello dear user\n welcome in number guessing game\n lets start this game\n")
print("you have only 7 chances\n")
low = int(input("enter the lower bound\n"))
high = int(input("enter your upper bound\n"))
num = random.randint(low,high)
chances = 7
guesscount = 0

while(guesscount<=chances):
    guesscount+=1
    guess = int(input("enter your guessing number between low and high point\n"))

    if(guess == num):
        print("whoo you got it correct...\n congratultions you win this game\n")
        break
    elif(guess>num):
        print("oops your guess is higher than number\n try reducing the number\n")

    elif(guess<num):
        print("oops your guess is lower than number \n try increasing the number\n ")

    elif(guesscount>=num and guess !=num):
        print("sorry the correct number is {num} \n youre unable to predict in 7 chances\n you loose this game")

