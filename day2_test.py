# Type STR
# ใช้ " " ไปโลด แต่ใช้ ' ' ก็ได้อยู่
from temperature import convert_to_celsius
import temperature
import os

temperature.convert_to_celsius


input_Farenheit = int(input("What is the temperature in Farenheit? "))
Celsius = convert_to_celsius(input_Farenheit)
print(round(Celsius, 2))
