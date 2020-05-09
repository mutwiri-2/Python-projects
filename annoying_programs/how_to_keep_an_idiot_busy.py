#! python3

# how_to_keep_an_idiot_busy.py - a program to repeatedly asks the user if they would like to know how to keep an idiot busy until they enter 'no'

import pyinputplus as pyip

while True:
    prompt = "Would you like to know how to keep an idiot busy for hours?\n"
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break
print("Thank you. Have a nice day!")        