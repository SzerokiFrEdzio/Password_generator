#imports
import random
import string
#source
char = list(string.ascii_letters + string.digits + '!@#$%^&*()')
#function
def random_password():
    len = int(input('Enter length of password: '))
    random.shuffle(char)
    #password
    password = []
    for i in range(len):
        password.append(random.choice(char))
    random.shuffle(password)
    print(''.join(password))
#run

random_password()
