# print(len(''))
# s = 'pineapple'
# print(s[5:])
# print(s[4:9])
# print(s[-5:])
# print(s[-5:-1])

# vehicle = 'car'

# print(vehicle[-1]+vehicle[1]+vehicle[:1]+'e'+vehicle)

# print('abc123'.isalnum())
# print('apple'.upper().islower())
# print('apple'.upper().isupper())
# print('12.34'.isalnum())

# s = '1abc'
# result = s.isalpha() or s.isnumeric()
# print(result)
# result2 = s.isalpha() and s.isnumeric()
# print(result2)
# result3 = s.isupper() or s.islower()
# print(result3)
# result4 = s.lower() or s.upper() or s.isdigit()
# print(result4)

# digits = '0123456789'
# result = 100

# for digit in digits:
#     result = result - int(digit)

# print(result)

# digits = '0123456789'
# result = 0

# for digit in digits:
#     result = digit

# print(result)

# digits = '0123456789'
# result = ''

# for digit in digits:
#     result = result + digit * 2

# print(result)

# message = 'Happy 29th!'
# new_message = ''

# for char in message:
#     if char.isdigit():
#         new_message = new_message + str((int(char) + 1) % 10)
#     else:
#         new_message = new_message + char

# print(new_message)

# # message = 'Happy 29th!'
# # new_message = ''

# # for char in message:
# #     new_message = new_message + str((int(char) + 1) % 10)

# # print(new_message)

# message = 'Happy 29th!'
# new_message = ''

# for char in message:
#     if char.isdigit():
#         new_message = new_message + str((int(char) + 1) % 10)
#     new_message = new_message + char

# print(new_message)

# message = 'Happy 29th!'
# new_message = ''

# for char in message:
#     if not char.isdigit():
#         new_message = new_message + char
#     else:
#         new_message = new_message + str((int(char) + 1) % 10)

# print(new_message)

def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that 
    appear at least once in s2. The characters in the result        
    will appear in the same order as they appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a' 
    >>> common_chars('abb', 'ab')
    'abb' 
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    '''
    res = ''
    for ch in s1:
        if ch in s2:
            res = res + ch
    return res

s1 = 'abracadabra'
s2 = 'ra'

print(common_chars(s1,s2))