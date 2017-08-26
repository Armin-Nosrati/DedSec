#imports
import os


#header
firstName = raw_input('Please Enter First Name:')
lastName = raw_input ('Please Enter Last Name: ')

#Codes
file = open ('pass.txt', 'w')
file.write(firstName + '\n')
file.write(lastName + '\n')
file.write(firstName + lastName + '\n')
file.write(lastName + firstName + '\n')

f = 999
while (f < 2000):
	f = f + 1
	file.write(firstName + str(f) + '\n')
f = 999
while (f < 2000):
	f = f + 1
	file.write(lastName + str(f) + '\n')
f = 999
while (f < 2000):
	f = f + 1
	file.write(firstName + lastName + str(f) + '\n')
f = 999
while (f < 2000):
	f = f + 1
	file.write(lastName + firstName + str(f) + '\n')
f = 999
while (f < 2000):
	f = f + 1
	file.write(str(f) + firstName + lastName + '\n')
f = 999
while (f < 2000):
	f = f + 1
	file.write(str(f) + lastName + firstName + '\n')
file.close()

#footer
print(' ')
print(' ')
print(' ')
print('Passowrd Generated Successfuly!!!')
