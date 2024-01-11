# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:32:18 2024

@author: khanb
"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%2==0:
            return False
    return True

def main():
    try:
        user_input=int(input("Enter a number "))
        if user_input<0:
            print("Enter positive number")
            
        else:
            if is_prime(user_input):
                print(f"{user_input} is a prime number")
            else:
                print(f"{user_input} is not a prime number")
            if user_input == int(user_input):
                print(f"{user_input} is a whole number")  
            else:
                print(f"{user_input} is not a whole number")
    except ValueError:
        print(f"{user_input} is invalid input. Please enter a valid input")
        
if __name__=="__main__":
    main()
