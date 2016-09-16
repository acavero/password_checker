import sys


def countLowCaseCharacters(password):
	lowercase = 0;
	for character in password:
		if character in 'abcdefghijklmonñpqrstuvwxyz':
			lowercase = lowercase + 1
	return lowercase
    
def countCapitalCaseCharacters(password):
	capitalCase = 0;
	for character in password:
		if character in 'ABCDEFGHIJKLMONÑPQRSTUVWXYZ':
			capitalCase = capitalCase + 1
	return capitalCase

def countNumbers(password):
	numbers = 0;
	for character in password:
		if character in '0123456789':
			numbers = numbers + 1
	return numbers

with open('password.txt','r') as file:		
	fileLine = file.read().splitlines()
	for line in fileLine:
		userName, password = line.split(':')
		passLength = len(password)
		lowerCase = countLowCaseCharacters(password)
		capitalCase = countCapitalCaseCharacters(password)
		numbersInPass = countNumbers(password)
		print ('User: ' + userName)
		print ('Pass: ' + password)
		print ('Pass length: ' + str(passLength))
		print ('Lower Case characters: ' + str(lowerCase))
		print ('Capital Case characters: ' + str(capitalCase))
		print ('Numbers: ' + str(numbersInPass))
		print ('-----------------------------------------------')


