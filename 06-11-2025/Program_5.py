string = input("Enter a string: ")
vowels = 0
consonants = 0
for i in string:
    if i.lower() in "aeiou":
        vowels = vowels + 1
    else:
        consonants = consonants + 1
print(f"No of vowels = {vowels}")
print(f"No of consonants = {consonants}")
