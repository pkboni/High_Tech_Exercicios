#---------------------------------------------------------------------------#
##Execricio 1: Fa�a um Programa que mostre a mensagem "Alo mundo" na tela
#print("Alo mundo ")

#---------------------------------------------------------------------------#
##Execricio 2: Fa�a um Programa que pe�a um n�mero e ent�o mostre a mensagem O n�mero informado foi [n�mero]
#def new_func():
#    numero = input("Informe um numero: ")
#    return numero

#numero = new_func()
#print("O numero informado foi:", numero)

#---------------------------------------------------------------------------#
#Execricio 3: Fa�a um Programa que pe�a dois n�meros e imprima a soma.
num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")
def new_func1(num1, num2):
    print("A soma dos numeros:", int(num1) + int(num2))

new_func1(num1, num2)

#---------------------------------------------------------------------------#
#Execricio 4: Fa�a um Programa que pe�a as 4 notas bimestrais e mostre a m�dia.
#nota1 = float(input("informe a nota do primeiro bimestre: "))
#nota2 = float(input("informe a nota do segundoo bimestre: "))
#nota3 = float(input("informe a nota do terceiro bimestre: "))
#nota4 = float(input("informe a nota do quarto bimestre: "))

#def media(nota1, nota2, nota3, nota4):
#    media1 = (nota1 + nota2 + nota3 + nota4)/4.0
#    print(f'A media e: {media1:.2f}')

#media(nota1, nota2, nota3, nota4)

#---------------------------------------------------------------------------#
#Execricio 5: Fa�a um Programa que converta metros para cent�metros
#xmetros = input("Informe a medida em metros: ")
#def new_func(xmetros):
#    print(f'{(float(xmetros)*100):.2f}', "centimetros")

#new_func(xmetros)


#---------------------------------------------------------------------------#
#Execricio 6: Fa�a um Programa que pe�a o raio de um c�rculo, calcule e mostre sua �rea.
#import math
#raio = float(input("Digite o raio do circulo: \n"))

#def area_circulo(raio):
#    area = (math.pi)*(raio**2)
#    print(f'A area do circulo: {area:.2f}')

#area_circulo(raio)

#---------------------------------------------------------------------------#
#Execricio 7: Fa�a um Programa que calcule a �rea de um quadrado, em seguida mostre o dobro desta �rea para o usu�rio.
#lado = float(input("Digite a medida do lado do quadrado: \n"))
#def area_quadrado(lado):
#    print(f'A area do quadrado: {(lado**2):.2f}')

#area_quadrado(lado)

#---------------------------------------------------------------------------#
#Execricio 8: Fa�a um Programa que pergunte quanto voc� ganha por hora e o n�mero de horas trabalhadas no m�s. 
#Calcule e mostre o total do seu sal�rio no referido m�s.
#valor_hora = float(input("Quanto voce ganha por hora:\n"))
#horas_mes = float(input("Quantas horas voce trabalha por mes:\n"))

#def salario_mes(valor_hora, horas_mes):
#    sal_mes = valor_hora*horas_mes
#    print(f'O salario do mes: {sal_mes:.2f}')

#salario_mes(valor_hora, horas_mes)

#---------------------------------------------------------------------------#
#Execricio 9: Fa�a um Programa que pe�a a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9)
#graus_fahrenheit = float(input("Informe a temperatura em Fahrenheit:\n"))

#def conversor(graus_fahrenheit):
#    graus_celsius = 5*((graus_fahrenheit - 32)/9)
#    return graus_celsius

#resultado_celsius = conversor(graus_fahrenheit)
#print(f'A temperatura em graus celsius: {resultado_celsius:.2f}')


#---------------------------------------------------------------------------#
##Execricio 10: Fa�a um Programa que pe�a a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#gr_cel = float(input("Digite a temperatura e graus Celsius:\n"))

#def converte(gr_cel):
#    print(f'A temperatura em graus Fahrenheit: {(gr_cel*1.8) + 32:.2f}')

#converte(gr_cel)


