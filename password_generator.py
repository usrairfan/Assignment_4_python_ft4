import random
print('Welcome To Password Generator')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount of passwords to generate: ')
number = int(number)

lenght = input('Your Password lenght: ')
lenght = int (lenght)

print ('\n here are your passwords:')
for pwd in range(number):
    passwords =''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)