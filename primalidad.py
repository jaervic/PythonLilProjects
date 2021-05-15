def primo(num):
	counter: 0
	for i in range(1, num + 1):
		if i == 1 or i == num:
			continue
		if num % i == 0:
			counter += 1
			break
	if counter == 0:
		return True
	else:
		return False
def main():
	num = int(input('Escribe un número: '))
	if primo(num):
		print('es primo.')
	else:
		print('no es primo.')
if __name__ == '__main__':
	main()