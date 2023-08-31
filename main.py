import random
import csv

# ------------------------------------------------------------
# "THE BEERWARE LICENSE" (Revision 42):
# tommyop02 wrote this code. As long as you retain this
# notice, you can do whatever you want with this stuff. If we
# meet someday, and you think this stuff is worth it, you can
# buy me a beer in return.
# ------------------------------------------------------------

# Welcome message

print("Welcome to the Voucher Codes Generator. This simple script lets you generate "
      "randomized, of your desired length")

# Obtain user input

number_of_codes = int(input('Enter Number of Codes :'))
number_of_characters = int(input('Enter Number of Characters for the codes :'))
appendix = input("Enter desired appendix, no trailing spaces please : ")


# Define character range allowed. This can also be turned into user input request with the
# following code:

# alphanumeric_range = input("Enter all the characters, i.e. numbers and letters, you wish to "
#                               "utilize for this code")

alphanumeric_range = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Define codes_list as an array

codes_list = []


# Generate the codes based on quantity requested and character length

for i in range(number_of_codes):
    code = appendix + "-" + "".join(random.choice(alphanumeric_range) for i in range(number_of_characters))
    codes_list.append(code)

# Save list of codes as a .csv file. Please note it will save in the working directory
# and overwrite any other file with the same name

with open('codesActual.csv', 'w') as file:
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    wr.writerow(codes_list)

print('Codes saved as codesActual.csv file!')
print("Thank you for using the Voucher Codes Generator!")
