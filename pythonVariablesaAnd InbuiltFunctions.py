
#VARIABLES
#Variables store data in a computer memory.
# A variable refers to a memory address in which data is stored. 
# Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more 
# descriptive name (firstname, lastname, age, country) is highly recommended.

#Built in functions
#In Python we have lots of built-in functions. Built-in functions are globally available for your use
# that mean you can make use of the built-in functions without importing or configuring. Some of the most commonly used Python built-in functions are the following: print(), len(), type(), int(), float(), str(), input(), list(), dict(), 
#min(), max(), sum(), sorted(), open(), file(), help(), and dir(). 

#Example
from __future__ import division
from itertools import product


first_name = 'Munduru'
last_name = 'Joana'
country = 'Kenya'
city = 'Niarobi'
age = 22
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Munduru',
   'lastname':'Joana',
   'country':'Uganda',
   'city':'Niarobi'
   }
   

#Let us use the print() and len() built-in functions.
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#Declaring Multiple Variable in a Line
first_name, last_name, country, age, is_married = 'Munduru', 'joana', 22, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Getting user input using the input() built-in function.
full_name = input('What is your name: ')
age = input('How old are you? ')

print(full_name)
print(age)

#EXERCISE
#Declare a first name variable and assign a value to it
firstName = 'Candiru'
#Declare a last name variable and assign a value to it
lastName = 'Candiru'
#Declare a full name variable and assign a value to it
fullName = 'Candiri juliet'
#Declare a country variable and assign a value to it
country = 'Uganda'
#Declare a city variable and assign a value to it
city = 'Kampala'
#Declare an age variable and assign a value to it
myAge = 23
#Declare a year variable and assign a value to it
myYear = '2003'
#Declare a variable is_married and assign a value to it
isMarried = False
#Declare a variable is_true and assign a value to it
isTrue = True
#Declare a variable is_light_on and assign a value to it
isLight = False
#Declare multiple variable on one line
firstName, lastName, country, city, myAge ='Candiru' ,'juliet','Uganda', 'Kampala', 23


#Check the data type of all your variables using type() built-in function
print(type(fullName))
print(type(myAge))
print(type(isTrue))
print(type([1, 2, 3, 4]))
print(type(1 + 1j))
print(type({'name':'Asabeneh','age':250, 'is_married':250}))
print(type(12.4))
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4]))) 


#Using the len() built-in function, find the length of your first name
print(len(firstName))

#Compare the length of your first name and your last name
print(len(firstName) == len(lastName))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total) 

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one =num_two
print(diff)

#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)

#Divide num_one by num_two and assign the value to a variable division
division = num_one/num_two
print(division)

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

#Find floor division of num_one by num_two and assign the value to a 
# variable floor_division
floor_division = num_one // num_two
print(floor_division)

#The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable 
# name of area_of_circle
pie = 3.14
area_of_circle = 3.14 * 30 * 30
print(area_of_circle)

#Calculate the circumference of a circle and assign the value to a 
# variable name of circum_of_circle
circum_of_circle = 2 * pie * 30
print(circum_of_circle)

#Take radius as user input and calculate the area.
#Use the built-in input function to get first name, last name, country and 
#age from a user and store the value to their corresponding variable names
