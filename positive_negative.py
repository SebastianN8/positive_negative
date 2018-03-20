#
# positive_negative.py
#
# Created by: Sebastian N
# Created on: March 20
#
# This program proves if an integer is positive, negative or zero.
#

# Function
def positive_negative(number_passed_in):
	# If statement
	if number_passed_in > 0:
		print('Your integer is positive!')
	elif number_passed_in < 0:
		print('Your integer is negative!')
	elif number_passed_in == 0:
		print('Your integer is zero!')
	else:
		print('Invalid input!')


# Variable
the_integer = input("Input and integer here: ")
the_integer_number = int(the_integer)
# Call funtion
the_sign = positive_negative(the_integer_number)
input()