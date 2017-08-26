import os

firstName = raw_input('Please Enter First Name:')
lastName = raw_input ('Please Enter Last Name: ')


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

file.close()


print(' ')
print(' ')
print(' ')
print('Passowrd Generated Successfuly!!!')
