#Función
def palin(palabra):
	if palabra == palabra[::-1]:
		print('Sí es palíndromo')
	else:
		print('No es palíndromo :(')

def main():
	#Input de la palabra a chequear
    palabra = str(input('Escribe una palabra para chequear si es palíndromo: ')).lower().replace(' ', "")
    palin(palabra)

if __name__ == "__main__":
	main()