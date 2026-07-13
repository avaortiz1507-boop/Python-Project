def count_vowels(text):
    vowels: str = "aeiouAEIOU"
    count: int = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

input_text: str = input("Enter a string: ").strip()
print(f"The number of vowels in '{input_text}' is: {count_vowels(input_text)}")
#1 prompt user to enter a string
#2 define a function that takes a string as input and counts the number of vowels in it
#3 loop through each character in the string and check if it is a vowel
#4 if it is a vowel, increment the count