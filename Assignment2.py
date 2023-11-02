# Program that checks whether an alphabet is a consonant or vowel
alphabet = input("Enter a single alphabet: ")

# Convert the input to lowercase to handle both uppercase and lowercase input
alphabet = alphabet.lower()

# Check if the input is a single alphabet
if len(alphabet) == 1 and alphabet.isalpha():
    # Check if the input is a vowel
    if alphabet in 'aeiou':
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("Please enter a valid single alphabet.")

