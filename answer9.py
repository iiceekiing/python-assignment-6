"""
    Task 9:
    Write a function that accepts a word as a parameter
    and returns the number of vowels (a, e, i, o, u) in the word.
    Example: count_vowels("apple") → 2
"""


def count_vowels(word):
    vowels = "aeioe"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

word = input("Enter any word to count the vowels in it: ")

print(f"there are {count_vowels(word)} vowels in {word}")
