#!/bin/python3

import sys

print("Please enter your password to check") # Prompt user for password
text1 = input() # Store password in variable
text2 = b'text1' # Store password in byte variable

with open('rockyou.txt', 'rb') as fp:  # Open rockyou.txt in read binary mode
        lines = fp.readlines() # Read all lines in rockyou.txt
        for row in lines: # Loop through each line in rockyou.txt
            if row.find(text2) == 0: # If the password is found in rockyou.txt
                print("your password has been compromised") #
                break # Break out of the loop
#            else:
#                print("password not found")

