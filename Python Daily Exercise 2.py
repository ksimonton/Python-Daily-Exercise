#Katelyn Simonton - Python Daily Exercise 2 - 2/21/2018

# 2. Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. Clue input()

name = input("What is your name? ")
age = input("How old are you? ")
hundred_years = 100 - int(age)
year_of_age = 2018 + int(hundred_years)
print (str(name) + ", you'll be 100 years old in " + str(year_of_age))