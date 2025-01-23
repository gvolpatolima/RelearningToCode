string = input("Tell me a string and i'll count how many vowels it has")

i = 0
string_length = len(string)
vowel_counter = 0

vowels = ["a","e","i","o","u"]

while i < string_length:
    if string[i] in vowels:
        vowel_counter +=1
        i+=1
    else:
        i+=1

print(vowel_counter)