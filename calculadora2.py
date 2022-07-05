#Instruções do projeto
#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o #programa mostrará a seguinte lista de operações:
#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair
#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar. 
 

def calculadora(num1, num2, operacao):
	if operacao == 1:
		resultado = num1 + num2
	elif operacao == 2:
		resultado = num1 - num2
	elif operacao == 3:
		resultado = num1 * num2
	elif operacao == 4:
		resultado = num1 / num2
	elif operacao == 0:
		operacao = 0
	
	return resultado

operacao = None
print('Calculadora ativa!\n')
while (operacao != 0) :

	operacao = int(input('Informe a operação:\n1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair\n'))
	
	if operacao == 0 :
		print("Encerrando calculadora...")
		break
	elif operacao >= 5:
		print('\n\nEssa opção não existe!!\n--------------------------------\n')
	else:
		num1 = float(input('Informe o primeiro número: '))
		num2 = float(input('\nInforme o segundo número: '))
		resultado = calculadora(num1, num2, operacao)
		print('O resultado é : '+ str(resultado) + ' !')
		print('--------------------fim-----------------------')
