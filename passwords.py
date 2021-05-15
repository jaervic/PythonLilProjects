import random
import string

def gen_password():

	lowercase = tuple(string.ascii_lowercase)
	uppercase = tuple(string.ascii_uppercase)
	nums = tuple(string.digits)
	characters = tuple(string.punctuation)
	alldigits_list = lowercase + uppercase + nums + characters
	password = []
	quantity = int(input('Escoja cuantos caracteres quiere: '))
	for i in range(quantity):
		password_random = random.choice(alldigits_list)
		password.append(password_random)
	password = ''.join(password)
	return password

def main():
	password = gen_password()
	print(f'Your password is: {password}')

if __name__ == '__main__':
	main()