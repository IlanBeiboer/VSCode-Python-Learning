import random

print('Fakka drerries welkom bij de wachtwoord generator')

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*().,?"

number = int(input("Who many passwords do you want: "))

length = int(input("Password length: "))

print('\nhere are your passwords:')

for password in range(number):
    passwords = ''
    for c in range(length):
        passwords = passwords + random.choice(chars)
    print(passwords)
