"""
    Task 11:
    Write a function that accepts a string as a parameter
    and returns the string reversed.
    Example: reverse_string("hello") → "olleh"

"""

def reverse_string(word):
    return word[::-1]

word = input("Enter any word let me reverse it: ")

print(f"if you reverse {word}, the output is:  {reverse_string(word)}")
