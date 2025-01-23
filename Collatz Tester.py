import time
print("Hello to the collatz tester, you will find the one sequence that goes to infinity today!")

chosen_number = int(input("Choose a number to start "))
print("Your tester will start in 2 seconds")
time.sleep(2)
collatz = 0

if chosen_number % 2 == 0:
    collatz = chosen_number / 2
else:
    collatz = 3*chosen_number + 1
print (collatz)
while collatz != 1:
    if collatz % 2 == 0:
        collatz = collatz / 2
    else:
        collatz = 3 * collatz + 1
    print(int(collatz))

