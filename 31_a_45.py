#Programação com decisão encadeada

#Exercicio 31
"""
salario = float(input("Digite o salário do colaborador: R$ "))

if salario < 500:
    reajuste = salario * 0.15
elif salario <= 1000:
    reajuste = salario * 0.10
else:
    reajuste = salario * 0.05

novo_salario = salario + reajuste

print("Reajuste: R$", reajuste)
print("Novo salário: R$", novo_salario)



#Exercicio 32
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

maior = max(a, b, c)
print("Maior valor: ", maior)

#Exercicio 33 -reutilizando o 32-
menor = min(a, b, c)
print("Menor valor: ", menor)

#Programação com seleção

#Exercicio 34

categoria = int(input("Digite a categoria do produto (1 a 5): "))

if categoria == 1:
    preco = 10.00
elif categoria == 2:
    preco = 15.00
elif categoria == 3:
    preco = 19.00
elif categoria == 4:
    preco = 23.00
elif categoria == 5:
    preco = 27.00
else:
    print("Categoria inválida!")
    preco = None

if preco is not None:
    print("O preço do produto da categoria", categoria, " é: R$", preco)

    
#Exercicio 35
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação deseja realizar? (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado da soma: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado da subtração: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado da multiplicação: {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida!")
else:
    print("Operação inválida! Use apenas +, -, * ou /")

#Exercicio 36
valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite seu salário mensal: R$ "))
anos = int(input("Em quantos anos deseja pagar? "))

meses = anos * 12
prestacao = valor_casa / meses

limite = salario * 0.30

print(f"Prestação mensal: R$ {prestacao:.2f}")
if prestacao <= limite:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado! A prestação excede 30% do seu salário.")


#Exercicio37
kwh = float(input("Digite a quantidade de kWh consumida: "))
tipo = input("Digite o tipo de instalação (R = Residencial, C = Comercial, I = Industrial): ").upper()

if tipo == 'R':
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == 'C':
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == 'I':
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print("Tipo de instalação inválido!")
    preco = None

if preco is not None:
    total = kwh * preco
    print(f"Preço por kWh: R$ {preco:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")
""" 
#Programação com uso de operadores lógicos

#Exercicio38
print("--- Comparador de Pesos ---")
peso1 = float(input("Digite o primeiro peso (em kg): "))
peso2 = float(input("Digite o segundo peso (em kg): "))
peso3 = float(input("Digite o terceiro peso (em kg): "))

maior_peso = peso1 

if (peso2 > maior_peso) and (peso2 >= peso3):
    maior_peso = peso2
    
if not(peso3 < peso1 or peso3 < peso2):
    maior_peso = peso3


print(f"\nO maior peso fornecido foi: {maior_peso} kg")

#Exercicio39
valor = int(input("Digite um número inteiro: "))

if (valor % 2 == 0) or (valor % 3 == 0):
    print (valor)

#Exercicio40
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))
E = int(input("Digite o valor de E: "))

maior = A
menor = A

if B > maior:
    maior = B
if C > maior:
    maior = C
if D > maior:
    maior = D
if E > maior:
    maior = E

if B < menor:
    menor = B
if C < menor:
    menor = C
if D < menor:
    menor = D
if E < menor:
    menor = E

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
 

#Exercicio 41
P1 = float(input("Digite a nota da P1: "))
P2 = float(input("Digite a nota da P2: "))

peso1 = float(input("Digite o peso da P1: "))
peso2 = float(input("Digite o peso da P2: "))


media = (P1 * peso1 + P2 * peso2) / (peso1 + peso2)

if media >= 7.5:
    print(f"Média: {media:.2f} - Aluno aprovado!")
else:
    print(f"Média: {media:.2f} - Aluno precisa fazer a P3.")
    
    P3 = float(input("Digite a nota da P3: "))
    peso3 = float(input("Digite o peso da P3: "))

    media_final = (P1 * peso1 + P2 * peso2 + P3 * peso3) / (peso1 + peso2 + peso3)

    if media_final > 6:
        print(f"Média final: {media_final:.2f} - Aluno aprovado com P3!")
    else:
        print(f"Média final: {media_final:.2f} - Aluno em dependência (DP).")

#Exercicio42

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()


preco_alcool = 2.90
preco_gasolina = 3.30


if tipo == 'A':
    preco = preco_alcool
    if litros <= 20:
        desconto = 0.03  # 3%
    else:
        desconto = 0.05  # 5%
elif tipo == 'G':
    preco = preco_gasolina
    if litros <= 20:
        desconto = 0.04  # 4%
    else:
        desconto = 0.06  # 6%
else:
    print("Tipo de combustível inválido.")
    desconto = 0
    preco = 0


valor_bruto = litros * preco
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto


if tipo in ['A', 'G']:
    print(f"\nTipo de combustível: {'Álcool' if tipo == 'A' else 'Gasolina'}")
    print(f"Litros vendidos: {litros:.2f}")
    print(f"Preço por litro: R$ {preco:.2f}")
    print(f"Desconto aplicado: {desconto * 100:.0f}%")
    print(f"Valor a ser pago: R$ {valor_final:.2f}")

#Exercico43
time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")

gols1 = int(input(f"Digite o número de gols do {time1}: "))
gols2 = int(input(f"Digite o número de gols do {time2}: "))

if gols1 > gols2:
    print(f"O vencedor é: {time1} ")
elif gols2 > gols1:
    print(f"o vencedor é: {time2}")
else: 
    print("EMPATE")

#Exercicio44
codigo = input("Digite o código do empregado: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_ingresso = int(input("Digite o ano de ingresso na empresa: "))

ano_atual = 2025
idade = ano_atual - ano_nascimento
tempo_trabalho = ano_atual - ano_ingresso

if idade >= 65 or tempo_trabalho >= 35 or (idade >= 60 and tempo_trabalho >= 25):
    status = "Requerer aposentadoria"
else:
    status = "Não requerer"

print(f"\nEmpregado código: {codigo}")
print(f"Idade: {idade} anos")
print(f"Tempo de trabalho: {tempo_trabalho} anos")
print(f"Situação: {status}")

#Exercicio45
A = float(input("Digite o lado A: "))
B = float(input("Digite o lado B: "))
C = float(input("Digite o lado C: "))

if A < B + C and B < A + C and C < A + B:
    if A == B and B == C:
        tipo = "Triângulo equilátero"
    elif A == B or B == C or A == C:
        tipo = "Triângulo isósceles"
    else:
        tipo = "Triângulo escaleno"
else:
    tipo = "Os lados não formam um triângulo"

print(f"\nResultado: {tipo}")