menu = """
Este es el conversor de monedas

1.- Bs
2.- COP
3.- DOP

Elige una opción: """


choice = int(input(menu))

if choice == 1:
	moneda = "Bolivares"
elif choice == 2:
	moneda = "Pesos Colombianos"
elif choice == 3:
	moneda = "Pesos Dominicanos"
else:
	print("Introduzca una opción valida, por favor!")

def currency():

	monedaLocal = int(input(f"¿Cuantos {moneda} tienes?: "))
	monedaLocal = float(monedaLocal)

	vDolar = int(input("¿Qué valor tiene el dolar actualmente?: "))
	vDolar = float(vDolar)

	USD = monedaLocal / vDolar
	USD = round(USD, 2)
	USD = str(USD)
	print(f"Tienes ${USD}")


if choice >= 1 and choice <= 3:
	currency()

