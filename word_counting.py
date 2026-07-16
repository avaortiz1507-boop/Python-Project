#1 prompt user to answer a question
import string

text: str = input("What is your favorite season and why?").strip().lower()
#2 validate the text by making all characters lowercase, remove leading and trailing whitespace, and remove basic punctuation (such as commas, periods, and exclamation marks)
translator: dict = str.maketrans('', '', string.punctuation)
cleaned_text: str = text.translate(translator)
#3 after validation, split the text into a list of individual words
words: list = cleaned_text.split()
#4 count the number of words and the average length of each word in the list and print the result
total_words: int = len(words)
print("Number of words:", len(words))

if total_words > 0:
    total_length: int = sum(len(word) for word in words)
    average_length: float = total_length / total_words
    print("Average length of each word:", average_length)
