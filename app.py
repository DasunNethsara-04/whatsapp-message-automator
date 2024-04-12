# imports
from pynput.keyboard import Key, Controller
import pywhatkit
import pyautogui
import time

# global variables
message = "Test Message from Python"
time_hour = 9
time_minute = 16

phone_nums: list = []

def get_phone_numbers() -> list:
    """Get phone numbers from the user"""
    global phone_nums
    with open("./phoneNums.txt", 'r') as file:
        phone_nums = file.read().split("\n")
    return phone_nums

def send_message(numbers: list) -> None:
    for num in numbers:
        # pywhatkit.sendwhatmsg(num, message, )
        pass

if __name__ == "__main__":
    phone_nums = get_phone_numbers()
    send_message(phone_nums)