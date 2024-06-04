# problem 1
"""
Problem Statement:

Prompt the user to enter a float number.
Use the round() function to round the number to 2 decimal places.
Print the original number and the rounded number.
Use the len() function to find the length of a string entered by the user and print the result.
"""
# Solution:

# float_no = float(input("Please enter a string number: "))
# rounded = round(float_no, 2)
# print("Original number: ", float_no)
# print("Rounded number: ", rounded)

# string = input("Please enter a string: ")
# string_len = len(string)
# print("The length of the entered string is: ", string_len)


# problem 2
"""
Problem Statement:

Prompt the user to enter a sentence.
Convert the entire sentence to uppercase.
Convert the entire sentence to lowercase.
Capitalize the first word of the sentence.

Print each of these modified sentences.
"""

# Solution:

# sentence = input("Please enter a sentence: ")
# uppercase = sentence.upper()
# lowercase = sentence.lower()
# Capitalize = sentence.capitalize()

# print("Here is the original sentence: ", sentence ,"and the modified sentence in uppercase is: ", uppercase)
# print("Here is the original sentence: ", sentence ,"and the modified sentence in lowercase is: ", lowercase)
# print("Here is the original sentence: ", sentence ,"and the modified sentence in capitalize is: ", Capitalize)


# problem 3
"""
Problem Statement:

Prompt the user to enter a sentence.
Ask user to replace the word
ask user to replace the word with

Print the modified sentence
"""

# Solution:

# sentence = input("Enter a sentence: ")
# word_to_replace = input("Enter the word you want to replace: ")
# replacement_word = input("Enter the word you want to replace it with: ")
# modified_sentence = sentence.replace(word_to_replace, replacement_word)

# print("Modified Sentence: ", modified_sentence)


# problem 4
"""
Write a program that:
Asks the user to enter their age.
Adds 10 to their age.

Prints a message saying "In 10 years, you will be X years old." where X is the new age.
"""

# Solution:

# age = int(input("Enter the age: "))
# add = age + 10
# print("In 10 years, you will be",add,"years old","where",add,"is the new age." )


# problem 5
"""
Write a program that:

Asks the user to enter their full name.
Converts the full name to uppercase and prints it.
Asks the user for their favorite number.
Multiplies the number by 2, converts it to a string, and concatenates it to a message.

Prints the message "Your favorite number multiplied by 2 is X.", where X is the new number.
"""

# Solution:

# full_name = input("Enter your full name: ")
# uppercase = full_name.upper()
# print(uppercase)

# favrt_no = int(input("Enter you favorite number: "))
# new_no = favrt_no*2
# string = str(new_no)
# msg = "The new number in string is: " + string
# print(msg)
# print("Your favorite number multiplied by 2 is",new_no,"where",new_no,"is the new number")


# problem 6
"""
Problem: Create a small program that asks the user for their first name and last name, 
converts them to uppercase, 
replaces spaces with hyphens
and calculates the length of their full name.

print 3 variables i.e
print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))

NOTE: Concepts Covered: input(), string methods (upper, replace), len(), print()
"""

# Solution:

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# full_name = first_name +" "+ last_name
# full_name_upper = full_name.upper()
# modified_sentence = full_name_upper.replace(" ", "-")
# full_name_length = len(first_name+last_name)

# print("Your full name in uppercase is: " + full_name_upper)
# print("Modified sentence: " + modified_sentence)
# print("The length of your full name is: " + str(full_name_length))


# problem 7
"""
Problem: Ask the user to input two numbers. 
Calculate their average 
and print the average rounded to 2 decimal places.

NOTE: Concepts Covered: round(), input(), print(), type casting
"""

# Solution:

# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter another number: "))
# avg = (num1+num2)/2
# rounded = round(avg, 2)
# print("The average is ",avg,"after rounded 2 decimal",rounded)


# problem 8
"""
Problem: Ask the user to input a sentence. 
Replace all spaces with underscores 
and split the sentence into words.

NOTE: Concepts Covered: replace(), split(), input(), print()
"""

# Solution:

# sentence = input("Enter a sentence: ")
# replace = sentence.replace(" ","_")
# words = replace.split("_")

# print("Modified Sentence:", replace)
# print("List of words:", words)
