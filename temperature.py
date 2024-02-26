def convert_to_celsius(fahrenheit) :

    '''(number) -> number

    return the number of Celsius degrees equivalent to Farenheit degrees
    >>> convert_to_celsius(32)
    0
    >>> convert_to_celsius(212)
    100
    '''
    return (fahrenheit - 32) * 5 / 9


# if __name__ == "__main__":
#     input_Farenheit = int(input("What is the temperature in Farenheit? "))
#     Celsius = convert_to_celsius(input_Farenheit)
#     print(round(Celsius, 2))

