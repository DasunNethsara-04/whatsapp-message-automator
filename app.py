# imports
import pywhatkit

phone_nums: list = []


with open("./phoneNums.txt", 'r') as file:
    phone_nums = file.read().split("\n")

print(phone_nums)