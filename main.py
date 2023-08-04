error = 0

first_number = input('Primeiro número: ')
operacao = input('Operação: ')
second_number = input('Segundo número: ')

try:
	first_number = int(first_number)
	second_number = int(second_number)
except ValueError as e:
	error = 1

if error > 0:
	print("Número inválido")
else:
	if operacao in ['+', '-', '/', '*']:
		if operacao == '+':
			resultado = first_number + second_number
		elif operacao == '-':
			resultado = first_number - second_number
		elif operacao == '/':
			resultado = first_number / second_number
		else:
			resultado = first_number * second_number
		print(f'{first_number} {operacao} {second_number} = {resultado}')
	else:
		print('Operação invalida.')
