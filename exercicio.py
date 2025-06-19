#1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['João', 'Maria', 'Gustavo', 'Halana']
nascimento = [2000, 2025]

# -------------

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

lista_teste = ['Dev FullStack', '3 meses e salario de 20k', 'Pare de ser enganado']
for i in lista_teste:
    print(i)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for i in numeros:
    if i % 2 == 1:
        soma += i
    print(soma) 

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in number:
    number.sort(reverse=True)
    print(number)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

usernumber = int(input('digite aqui seu número para descobrir a tabuada: '))


for i in range(1, 11):
    resultado = usernumber * i
    print(f'{usernumber} x {i} = {resultado}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.

numbers = [21, 32, 23, 14, 35, 56, 67, 18, 29, 170]
somas = 0

try:
    for i in numbers:
        somas += i
    print(f'a soma total resulta em {somas}')

except TypeError:
    print('O valor digitado não é um número')


# 7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

notas = [10, 4, 5, 3, 7, 2]

try: 
    media = sum(notas) / len(notas)
    print(f'a média é {media}')
except ZeroDivisionError:
    print('por favor, insira um valor em notas')