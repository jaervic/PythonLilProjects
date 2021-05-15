import random

def main():
	ram_num = random.randint(1,100)
	num = int(input('Elige un número entre 1 y 100: '))
	while num != ram_num:
		if num < ram_num:
			print('Busca un número más grande')
		
		else:
			print('Busca uno más pequeño')
		num = int(input('Escribe otro número: '))
	print('¡Ganaste!')

if __name__ == '__main__':
	main()