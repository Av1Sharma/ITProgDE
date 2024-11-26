# 
# Assignment: Fractions
# FractionsName.py
# Name: Avi Sharma
# File Created on October 30, 2024
# Purpose: To determine whether a given fraction is proper, improper, or mixed and display the result.
# Honor Code: I have neither given nor received unauthorized aid on this assignment.
#

# Get user input
numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator (not zero): "))

# Validate denominator
while denominator == 0:
    print("Denominator cannot be zero. Please enter a valid denominator.")
    denominator = int(input("Enter a denominator (not zero): "))

# Determine if the fraction is proper or improper
if abs(numerator) < abs(denominator):
    print(f"{numerator} / {denominator} is a proper fraction.")
else:
    # Calculate the whole number and remainder for mixed fraction
    whole_number = (int)(numerator / denominator)
    remainder = abs(numerator) % abs(denominator)
    
    # Display improper fraction results
    if remainder == 0:
        print(f"{numerator} / {denominator} is an improper fraction and it can be reduced to {whole_number}.")
    else:
        if numerator < 0:
            print(f"{numerator} / {denominator} is an improper fraction and its mixed fraction is -({abs(whole_number)} + {remainder} / {abs(denominator)}).")
        else:
            print(f"{numerator} / {denominator} is an improper fraction and its mixed fraction is {whole_number} + {remainder} / {abs(denominator)}.")
