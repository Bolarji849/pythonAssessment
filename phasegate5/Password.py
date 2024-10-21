
import string
import random

lowercase_letters = string.ascii_lowercase

upper_case = string.ascii_uppercase

numbers = string.digits

symbols = string.punctuation



def generate_password():
	password = ""

	for i in range(5):
		password += random.choice(lowercase_letters)
		password += random.choice(upper_case)
		password += random.choice(numbers)
		password += random.choice(symbols)

	return password




def get_lowercase_letters():
	lowercase_letters = string.ascii_lowercase
	return lowercase_letters


def get_upper_letters():
	upper_case  = string.ascii_uppercase

def get_numbers_letters():
	numbers = string.digits


def get_symbols_letters():
	symbols = string.punctuation
