import random

print("Hi, what is the interval you would like to guess today?")
low = int(input("Pick a lower bound: "))
high = int(input("Pick a high bound: "))

print("You will choose choose a number from", low, "to", high)
p = 0

chosen_number = random.randint(low,high)
while p < 1:
    guess = int(input("Pick a number from that interval "))
    if guess < low or guess > high:
        print("Out of Bounds")
    elif guess < chosen_number:
        print("Pick a higher number")
    elif guess > chosen_number:
        print("Pick a lower number")
    elif guess == chosen_number:
        print("You've won!")
        p += 1
