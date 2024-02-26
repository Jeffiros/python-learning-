# Type STR
# ใช้ " " ไปโลด แต่ใช้ ' ' ก็ได้อยู่
from temperature import convert_to_celsius
from area_perimeter import  area, semiperimeter


sunny_greeting = "What a beautiful day."
storm_greeting = "Wow, you're dripping wet."
storm2_greeting = "Wow, you\'re dripping wet."
print('personal' + 'penguin')
print(sunny_greeting)
print(storm_greeting)
print(storm2_greeting)
print('I want to be your personal ' + 'penguin' + '!')
puzzle_start = 'I want to be your personal '
punctuation = '!'
noun = 'earthworm'
print(puzzle_start+noun+punctuation)
print('Ha'*5)
print('Bwa' + 'ha'*5)
print(('bwa'+'ha')*5)
print('ba'+'na'*2+'muffin')

# Input/Output and str Formatting
print("Hello")
print(3+7-3)
print("Hello", "there")

def square_return(num) :
    res = num ** 2
    return res
def square_print(num) :
    print("The square of num is", num ** 2)

answer_return = square_return(4) 
answer_print = square_print(4) 

print(answer_return) #show 16 in result
print(answer_print) #show none in result

# practice
# def add(number1, number2) :
#     print(number1+number2)

# result = add(1, 3)
# new_result = result + 1

def add(number1,number2) :
    return number1 + number2

result = add(1, 3)
new_result = result + 1

print(result)
print(new_result)

def add(number1,number2) :
    return number1 + number2
    print("hello") #not showed

result = add(1, 3)

print(result)

def add(number1,number2) :
    print(number1 + number2)
    
result = add(1, 3)

print(result) # shows None

# name = input("what is your name? ")
# location = input("what is your location? ")
# print(name, "lives in", location)

# age = input("How old are you? ")
# print(age)

print('''How
are
you''') #show How are you in seperated line

s = '''How
are
you?'''
print(s)

print('3\t4\t5')

print("Strings are fun!", "Don't you think?")
print("\\n is the newline character in Python")
print("this \n is the newline character in Python")
print("this \\n is the newline character in Python")

# Docstrings and Function help
# using help() 

#Function design Recipe

def area(base, height) : 
    '''(number, number) -> number 
    
    Return the area of a triangle with dimensuions base
    and height.
    
    >>> area(10, 5)
    25.0
    >>> area(2.5, 3)
    3.75
    '''
    return base*height/2

def convert_to_celsius(fahrenheit) :

    '''(number) -> float

    return the number of Celsius degrees equivalent to Farenheit degrees
    >>> convert_to_celsius(32)
    0
    >>> convert_to_celsius(212)
    100
    '''
    return (fahrenheit - 32) * 5 / 9

input_Farenheit = int(input("What is the temperature in Farenheit? "))
Celsius = convert_to_celsius(input_Farenheit)
print(round(Celsius, 2))

def area(base, height) : 
    '''(number, number) -> number 
    
    Return the area of a triangle with dimensuions base
    and height.
    
    >>> area(10, 5)
    25.0
    >>> area(2.5, 3)
    3.75
    '''
    return base*height/2

input_perimeter_side1 = int(input("What is the perimeter side1? "))
input_perimeter_side2 = int(input("What is the perimeter side2? "))
input_perimeter_side3 = int(input("What is the perimeter side3? "))
side1 = input_perimeter_side1
side2 = input_perimeter_side2
side3 = input_perimeter_side3

print(semiperimeter(side1, side2, side3))


print(round((max(area(3.8, 7.0), area(3.5, 6.8))), 1))

def get_oldest(age1, age2):
    '''(int, int) -> int
    Return the oldest of the two ages, age1 and age2
    
    >>> get_oldest(27,22)
    27
    '''
    return max(age1, age2)

age1 = 27
age2 = 22
print(get_oldest(age1, age2))

# print('3\')
# print(''that's okay''')
# print('"once upon a time...", she said.')
# print("he said, "yes!"")

print('hello-' + 'how-are-you')
print('hello'+'-'+'how'+'-'+'are'+'-'+'you')
print('hello','-','how','-')

print('''yesterday
      today
      tomorrow''')

print('''yesterday
      \ntoday
      \ntomorrow''')


# 6
# 13
# 14
# 15
# 18

print('hello','-','how ','-','are','-','you')
     
