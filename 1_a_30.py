#Exercicio 01
print("Hello World!")

#Exercicio 02
print ('Kathy')

#Exercicio 03
NomeUsuario = input('qual é o seu nome')
print(NomeUsuario)

#Exercicio 04
nome = input('qual é o seu nome? ')
print ('seu nome é ' + nome)

#Exercicio 05
val1 = input('Digite um valor: ')
val2 = input('Digite outro valor: ')
s =  (val1 + val2)
print('A soma de', val1, '+', val2 , 'é igual',  s)

#Exercicio 06
a = 3
b = 5
c = 2*a * 3*b
print(c)

#Exercicio 07
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
soma = num1 + num2 + num3
print ('A soma dos números é:', soma)

#exercicio 08
salarioAtual = float(input('digite o quanto você ganha: '))
porcentagem = float(input('digite a porcentagem do valor que você deseja cacular: '))
calculo = salario*porcentagem
calculo2 = calculo/100
novoSalario = salario + calculo2
print('seu salário atual é de R$', salarioAtual, 'após o aumento de ', porcentagem, 'seu salário será de R$', novoSalario)

#Exercicio 09
num4 = int(input('Digite o primeiro número inteiro: '))
num5 = int(input('Digite o segundo número inteiro: '))
s = num4 + num5
print ('A soma dos números inteiros é igual a: ', s)

#Exercicio 10
metros = float(input('Digite quantos metros deseja: '))
cm = metros*100
mm = metros*1000
print (metros, 'metro(s) é igual a ', cm ,  ' cm que é igual a ', mm, 'mm')

#Exercicio 11
print ('Convertendo dias, horas, minutos e segundos para segundos.')
dias = int(input('Entre com dias: '))
horas = int(input('Entre com horas: '))
minutos = int(input('Entre com minutos: '))
segundos = int(input('Entre com segundos: '))
#c significa a conversão do valor desejado
cDias = dias*86400
cHoras = horas*3600
cMinutos = minutos*60
total = cDias + cHoras +cMinutos + segundos
print ('o total de segundos é: ', total)

#exercicio 12
john = 3
mary = 5
adam = 6
print ( john , ',' , mary , ',' , adam )
totalApples = john + mary + adam
print ( totalApples )

#eEercicio 13
produto = float(input('Digite o preço da mercadoria: '))
desconto = float(input('Digite o porcentual de desconto: '))
calcu = produto*desconto
calcu2 = calcu/100
calcu3 = produto - calcu2
print ('com o desconto de ', desconto , 'O preço final é de: ', calcu3)

#Exercicio 14
distancia = int(input('Qual será a distância a percorrer? '))
velocidade= int(input('Qual será a velocidade média da viagem? '))
cal = distancia / velocidade
print ('tempo de viagem: ', cal)

#Exercicio 15
c = int(input('digite a temperatura que será convertida: '))
f = c * 9/5 + 32
print ('a temperatura convertida é igual a: ', f)

#Exercicio 16
km = int(input('Entre com a quantidade de km: '))
dias = int(input('Entre com a quantidade de dias que o carro foi alugado: '))
pagamento_dias = dias * 60
pagamento_km = km*0.15
pagamento_final = pagamento_dias + pagamento_km
print ('Total a pagar: ', pagamento_final)      

#Exercicio 17
cigarrosDia = int(input('Cigarros fumados por dia: '))
anosFumante = int(input('Você fuma a quantos anos: '))
tempoDeFumante = anosFumante*365
cigarrosConsumidos = tempoDeFumante*cigarrosDia
reducaoVidaMin = cigarrosDia*10
reducaoVidaDias = reducaoVidaMin/1440

#Exercicio 18
milhas = int(input('Entre com milhas: '))
km = int(input('Entre com km: '))
convertendo_milhas = milhas *1.61
convertendo_km = 1.61 * km
print('conversão de milhas para km é igual a: ', convertendo_milhas)
print('conversão de km para milhas é igual a: ',  convertendo_km)

#Exercicio 19
x = int(input('Digite o valor de X: '))
fx = 3*x**3 - 2*x**2 +3*x - 1
print(f"Para x = {x}, y = {fx}")

#Exercicio 20
real1 = float(input('Entre com primeiro número real: '))
real2 = float(input('Entre com segundo número real: '))
adicao= real1 + real2
if adicao > 10:
    print('o valor da soma é ', adicao)
print('fim do programa')

#DECISÃO SIMPLES

#Exercicio 21
num1 = int(input('Entre com o primeiro número: '))
num2 = int(input('Entre com o segundo número: '))
if num1 ==  num2:
   print('Números iguais!')
elif num1 > num2: 
    print('O número maior é: ', num1)   
else:
    num1 < num2
    print ('O número maior é: ', num2)

#Exercicio 22
real1 = int(input('Entre com o primeiro valor real: '))
real2 = int(input('Entre com o segundo valor real: '))
s = real1 + real2
if s > 10:
    print('Maior que 10')
    print('Obrigada por usar nosso programa!')
elif s == 10:
     print('Obrigada por usar nosso programa!')   
else:
    s < 10
    print('Menor que 10')
    print('Obrigada por usar nosso programa!')

#Exercicio 23
    velocidade = float(input('Entre com a velocidade do carro: '))
if velocidade >80:
   km = velocidade - 80
   multa = km*5
   print('Você foi multado em R$', multa)


#Exercicio 24
num1 = float(input('Entre com um número: '))
num2 = float(input('Entre com outro número: '))
num3 = float(input('Entre com outro número: '))

maior_numero = max(num1, num2, num3)
print(f"O maior número é: {maior_numero}")
menor_numero = min(num1, num2, num3)
print(f"O menor número é: {menor_numero}")

              
#Exercicio 25
sal= float(input('Qual é o seu salarío: '))
if sal > 1250.00:
    cal =sal/100
    superiores = sal + cal
    print('Teu salario é de: ', superiores )
else:
    sal <= 1250.00 
    cal2 = sal/0.15
    inferiores = sal +cal2
    print('Teu salario é de: ', inferiores)
    print('fim do programa')
    
#Exercicio 26
produto = str(input('Descrição do produto: '))
qtde = int(input('Quantidade adquirida: '))
preco_unit = int(input('Preço unitário: '))
total = qtde * preco_unit

if qtde <= 5:
   desconto = total * 0.02
   total_a_pagar = total - desconto
   print('o preço da(o)', produto, 'é igual a ', total_a_pagar)
else:
    qtde >6 <= 10 
    desconto1 = total * 0.03
    total_a_pagar1 = total - desconto1
    print('o preço da(o)', produto, 'é igual a ', total_a_pagar1)

if qtde <10: 
    desconto2 = total * 0.05
    total_a_pagar2 = total - desconto2
    print('o preço da(o)', produto, 'é igual a ', total_a_pagar2)
else:
    print('fim do programa')

#Exercicio 27
valor1 = float(input('Entre com um número real: '))
valor2 = float(input('Entre com outro número real'))

valor_total = valor1 + valor2

if valor_total <= 10:
   valor3 = valor_total + 5
   print ('O valor da soma + 5 é igual a: ', valor3)
else:
    valor_total >10 
    valor4 = valor_total -7
    print ('o valor da soma -  7 é igual a: ', valor4)


#Exercico 28
valor = float(input('Entre com um numero real mãop negativo '))

if valor == 5:
   raiz_quadrada = 2.2360679775
   print (raiz_quadrada)
else:
    valor >5
    raiz_cubica = valor **(1/3)
    print(raiz_cubica )

if valor < 5:
    raiz_cubica = valor ** (1/3)
    print(raiz_cubica )
else:
    valor < 0
    print('Fim do programa')

#Exercicio 29
carro = int(input('Quanto tempo você tem o seu carro'))
if carro <= 3:
   print ('Seu carro é novo')
else:
 print ('Seu carro é velho')

 #Exercico 30
distancia=int(input("Entre com a distância da viagem: "))
if distancia<200:
      preco=distancia*0.50
else:
    preco=distancia*0.45
    
print("O valor total da sua viagem é R$ ",preco)