# 1. WAP to demonstrate while loop with else statement.
def while_else_demo():
    i = 1
    while i <= 5:
        print(i)
        i += 1
    else:
        print("Loop completed.")

while_else_demo()

# 2. Print 1st 5 even numbers (use break statement).
def first_five_even():
    num = 2
    count = 0
    while True:
        if count == 5:
            break
        print(num)
        num += 2
        count += 1

first_five_even()

# 3. Print 1st 4 even numbers (use continue statement).
def first_four_even():
    num = 0
    count = 0
    while count < 4:
        num += 1
        if num % 2 != 0:
            continue
        print(num)
        count += 1

first_four_even()

# 4. WAP to demonstrate Pass statements.
def pass_demo():
    for i in range(5):
        if i == 2:
            pass  # Placeholder statement
        else:
            print(i)

pass_demo()

# 5. Write a Python program to calculate the length of a string.
def string_length():
    s = input("Enter a string: ")
    print("Length of the string:", len(s))

string_length()

# 6. Write a Python program to count the number of characters (character frequency) in a string.
def char_frequency():
    s = input("Enter a string: ")
    frequency = {char: s.count(char) for char in set(s)}
    print("Character Frequency:", frequency)

char_frequency()

# 7. Get a string made of the first 2 and the last 2 chars from a given string.
def first_last_two_chars():
    s = input("Enter a string: ")
    print(s[:2] + s[-2:] if len(s) >= 2 else "")

first_last_two_chars()

# 8. Replace all occurrences of first char with '$', except the first char itself.
def replace_first_char():
    s = input("Enter a string: ")
    first_char = s[0]
    modified_string = first_char + s[1:].replace(first_char, '$')
    print("Modified String:", modified_string)

replace_first_char()

# 9. Get a single string from two given strings, separated by a space, swapping the first two characters.
def swap_first_two_chars():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    if len(str1) >= 2 and len(str2) >= 2:
        swapped = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
        print("Swapped String:", swapped)
    else:
        print("Strings should be at least 2 characters long.")

swap_first_two_chars()

# 10. Modify a string: add 'ing' if length >= 3, else add 'ly' if ends with 'ing'.
def modify_string():
    s = input("Enter a string: ")
    if len(s) < 3:
        print(s)
    elif s.endswith("ing"):
        print(s + "ly")
    else:
        print(s + "ing")

modify_string()
