# python as calculator + variables
# run program and fill the blank with number & operator symbol you want.

# operator : Addition | Subtraction | Multiplication | Exponentiation | Division | Integer Division | Modulo(remainder)
# Symbol : + | - | * | ** | / | // | %

# 2 types of Python's numeric types
# int: integer
# float : floating point number, an apporximation to a real number

# Operation always run from left to right such as 3 + 4 - 5 equals 2
# Operation always run from higher precedence to lower precedence such as 3 + 5*2 equals 13
# highest precedence    **
#                       - (Negation)
#                       * / // %
# lowest precedence      + -

base = 20
height = 12
area = base * height/2
print(f"area = {area}") 

a = 8
a = 4
b = 3.2


a + b
print(a+b)

z = 5
y = z + 1
z = 10
print({z}, {y})



def increment(x) :
    return x + 1

def double(x) :
    return 2 * x

x = 5

print(f"result is", increment(x))
print(f"result is", double(x))

# while True:

#     base = float(input("base : "))
#     height = float(input("height : "))

#     def area(base, height) :
#         return base * height / 2

#     print(f"Area equals to : ", area(base, height))


x = 135.4863488
y = round(x, 1)
print(y)

x = 12
y = 5
A = x//y
B = x**y
C = x*y+x-y-x//y
print(f" result of A is {A}\n result of B is {B}\n result of C is {C}") 

a = ['a','b','c']
b = ['d','e']
x = [[i,j] for i in a for j in b ]
print(x)

