# contador = 0
# while contador < 200:
# 	contador += 1
# 	if contador == 1:
# 		print(f'Me cojo a tu mamá {contador} vez')
# 	else:
# 		print(f'Me cojo a tu mamá {contador} veces')

# for contador in range(1, 1001):
# 	print(contador)

def main():
	fruta = str(input('Dime una fruta: '))
	for letra in fruta:
		print(letra.upper())

if __name__ == '__main__':
	main()