import random
import string


def gen_password():
    lower = tuple(string.ascii_lowercase)
    upper = tuple(string.ascii_uppercase)
    nums = tuple(string.digits)
    punctuations = tuple(string.punctuation)
    characters = lower + upper + nums + punctuations

    password_list = []

    for i in range(random.randint(8, 16)):
        character_random = random.choice(characters)
        password_list.append(character_random)

    password_list = ''.join(password_list)
    return password_list


def main():
    password = gen_password()
    print(f'Tu contraseña será: {password}')


if __name__ == '__main__':
    main()
