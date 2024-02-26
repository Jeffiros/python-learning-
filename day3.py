from area_perimeter import area_hero

def g(x):
    y = 10
    y = 2
    return y+x

def f():
    y = 1
    return g(y)

print(f())

# Type Bool #

# less than <
# greater than >
# equal to ==
# greater than or equal to >=
# less than or equal to <=
# not equal to !=

# not 1st priority
# and 2nd
# or 3rd

# expression | not expression
# True            False
# False           True

# grade = 80
# grade >= 50
# >>> False

# expr1   |  expr2    |   expr1 and expr2
# True        True            True
# True        False           False
# False       True            False
# False       False           False

# grade1 = 80
# grade2 = 70
# (grade1 >= 50) and grade2 >= 50)
# >>> True
# grade1 = 40
# (grade1 >= 50) and (grade2 >= 50)
# >>> False

# expr1   |  expr2    |   expr1 or expr2
# True        True            True
# True        False           True
# False       True            True
# False       False           False

# grade1 = 30
# grade2 = 70
# (grade1 >= 50) or grade2 >= 50)
# >>> True
# grade2 = 40
# (grade1 >= 50) or (grade2 >= 50)
# >>> False
# not grade >= 50 or grade2 >= 50
# >>> True

# conversion btw int str float #
str(3)
print(str(3))
three = str(3)
three * 10
print(three*10)
int(three*5)
print(int(three*5))
three*5
print(three*5)
str(4.65)
print(str(4.65))
int('456')
print(int('456'))
float('456')
print(float('456'))
float(str(45))
print(float(str(45)))

# import: Using Non-Built-in Functions #

print(area_hero(10.5, 6, 9.3))

def area(sidelength):

    return area_hero(sidelength, sidelength, sidelength)

print(area(5))

# if statement #

def report_status(scheduled_time, estimated_time):
    ''' (number, number) -> str

    Return the flight statud (on time, early, delayed)
    for a flight that was scheduled to arrive at scheduled_time
    , but is now estimated to arrive at estimated_time.

    pre-condition: 0.0 <= scheduled_time < 24
    and 0.0 <= estimated_time < 24

    >>> report_status(14.3,14.3)
    'on time'
    >>> report_status(12.5,11.5)
    'early'
    >>> report_status(9.0,9.5)
    'delayed'
    '''

    if scheduled_time == estimated_time:
        return 'on time'
    elif scheduled_time > estimated_time:
        return 'early'
    else:
        return 'delayed'
    
scheduled_time = int(input("What's the scheduled_time? "))
estimated_time = int(input("What's the estimated time? "))

print(report_status(scheduled_time, estimated_time))

# No If required #

def is_even(num):
    ''' (int) -> bool
    Return whether num is even.

    >>> is_even(4)
    True
    >>> is_even(7)
    False
    '''
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

    return num % 2 == 0

num = int(input("Input the number: "))
print(is_even(num))

def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'
        
print(traffic_report('yellow'))

def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'
        
print(traffic_report('orange'))

def grade_report(grade):
    if grade >= 80:
        return 'excellent'
    elif grade >= 50:
        return 'pass'
    
print(grade_report(40))
print(grade_report(70))
print(grade_report(50))
print(grade_report(80))

