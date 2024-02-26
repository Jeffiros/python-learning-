# More str operators #

# solution = 'cat'
# solution == 'cat'
# >>> True
# solution != 'cat'
# >>> False

# solution = 'dog'
# solution == 'cat'
# >>> False
# solution != 'cat'
# >>> True

# 'abracadabra' < 'ace'
# >>> True
# 'abracadabra' > 'ace'
# >>> False

# 'a' <= 'a'
# >>> True
# 'A' <= 'B'
# >>> True
# 'a' != 'A'
# >>> True
# 'a' < 'A'
# >>> False
# 'a' > 'A'
# >>> True
# ',' < '3'
# >>> True
# 's' == 3
# >>> False

# 'cad' in 'abracadabra'
# >>> True
# 'c' in 'aeiou'
# >>> False
# 'zoo' in 'ooze'
# >>> False
# '' in 'abc'
# >>> True
# '' in ''
# >>> True

# len('')
# >>> 0
# len('abracadabra')
# >>> 11

print(len("hello world!"))

# Str: Indexing and slicing #

s = 'Learn to Program'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

print(s[15])
print(s[-1])

print(s[-16])
print(s[-15])
print(s[-14])
print(s[-13])
print(s[-12])
print(s[-11])

print(s[0:5])
print(s[6:8])
print(s[9:16])
print(s[9:len(s)])
print(s[9:])
print(s[:8])
print(s[:])

s = 'Call Me Maybe'
print(len(s))

s = 'Learn to Program'
s = s[:5] + 'ed' + s[5:]
print(s)

# str methods: functionss inside objects #

queen_of_hearts = 'Off with their heads!'
print(queen_of_hearts.count('heads'))
print(queen_of_hearts.find('heads'))
print(queen_of_hearts.find('heads', 7))
print(queen_of_hearts.find('sdaeh'))
print(queen_of_hearts.find('Heads'))

print("computer".capitalize())
print("Computer".capitalize())

s = "  i'm feeling spaced out. "
print(s)
print(s.lstrip())
print(s.rstrip())
print(s.strip())

white_queen = "Jam tomorrow and jam yesterday - but never jam today."
print(white_queen.count('jam'))
print(white_queen.lower().count("jam"))
# print(white_queen.upper().count("jam"))

# For loop over str #

s = 'Hi there!'
for char in s :
    print(char)

for vowel in 'aeiou' :
    print ("I'd like to buy a", vowel)

def count_vowels(s):

    ''' (str) -> int

    Return the number of vowels in s. Do not treat the 
    letter y as a vowel.

    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0
    '''
    num_vowels = 0
    for char in s :
        if char in 'aeiouAEIOU' :
            num_vowels = num_vowels + 1

    return num_vowels


print(count_vowels('Happy Anniversary!'))
print(count_vowels('xyz'))
print(count_vowels(''))

def collect_vowels(s) :

    ''' (str) -> str
    
    Return the vowels from s. Do not treat the
    letter y as a vowel.

    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('xyz')
    ''
    '''

    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU' :
            vowels = vowels + char
           
    return vowels

print(collect_vowels('Happy Anniversary!'))
print(collect_vowels('xyz'))
print(collect_vowels(''))

# IDLE's Debugger #





