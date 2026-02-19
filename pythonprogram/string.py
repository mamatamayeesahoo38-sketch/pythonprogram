s = input("Enter a string: ")

alpha = upper = lower = vowel = cons = digit = space = symbol = 0

vowels = "aeiouAEIOU"

for ch in s:
    if ch.isalpha():
        alpha += 1
        if ch.isupper():
            upper += 1
        else:
            lower += 1
        if ch in vowels:
            vowel += 1
        else:
            cons += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
    else:
        symbol += 1

words = len(s.split())

print("Alphabets:", alpha)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Vowels:", vowel)
print("Consonants:", cons)
print("Digits:", digit)
print("Spaces:", space)
print("Symbols:", symbol)
print("Words:", words)