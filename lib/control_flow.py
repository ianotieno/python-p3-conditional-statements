#!/usr/bin/env python3

def admin_login(username, password):
    if (username.lower() == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "it's a little chilly out there!" 
    elif temperature > 85:
        return "it's too dang hot out there!"
    else:
        return "it's perfect out there!"

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
