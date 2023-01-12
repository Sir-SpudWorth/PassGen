# A password generator with different options for generating different types

# Import dependencies
import random
import string
import pyperclip
import argparse

# Argument parser
parser = argparse.ArgumentParser(description='Create a random password with different formats. Default is Microsoft Format')
parser.add_argument('-t', '--type', default='M', help='Type of password to generate')
parser.add_argument('-l', '--length', type=int, default=8, help='Length of password')

# Extract data from parser
args = parser.parse_args()

# Create bank of letters, numbers and symbols to choose from
library = string.ascii_letters + string.digits + string.punctuation

# Classes 
# Microsoft Format
def microsoftPass():
    #Choose 1 Uppercase
    password = random.choice(string.ascii_uppercase)
    #Choose 2 Lowercase
    for i in range(2):
        password += random.choice(string.ascii_lowercase)
    #Choose 5 Digits
    for i in range(5):
        password += random.choice(string.digits)
    pyperclip.copy(password)
    print(password)

# Pass Length
def genRanOfLength():
    password = ''
    for i in range(args.length):
        password += random.choice(library)
    pyperclip.copy(password)
    print(password)

# Lowercase
def lowerPass():
    password =''
    for i in range(args.length):
        password += random.choice(string.ascii_lowercase)
    pyperclip.copy(password)
    print(password)

# Main
if args.type == 'M' or args.type == 'm':
    microsoftPass()
elif args.type == 'R' or args.type == 'r':
    genRanOfLength()
elif args.type == 'L' or args.type =='l':
    lowerPass()