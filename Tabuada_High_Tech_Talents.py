#Exercício 1 de 2: Tabuada

def nome():
    while True:
        usuario = ""
        usuario = input("Por favor, digite o seu nome: ")
        if usuario.isnumeric() or usuario == "":
            print("Entrada invalida. Por favor, digite seu nome! ", usuario)
        else:
            return usuario

usuario = nome()

def boas_vindas(usuario):
    print(f"Seja Bem-vindo {usuario}.\n")
    return

boas_vindas(usuario)

_soma = lambda x, y: x + y
_subtracao = lambda x, y: x - y
_multiplicacao = lambda x, y: x * y
_divisao = lambda x ,y: x / y
_tabuada = [lambda x: f"{x} * 0 = " + str(x * 0),
            lambda x: f"{x} * 1 = " + str(x * 1),
            lambda x: f"{x} * 2 = " + str(x * 2),
            lambda x: f"{x} * 3 = " + str(x * 3),
            lambda x: f"{x} * 4 = " + str(x * 4),
            lambda x: f"{x} * 5 = " + str(x * 5),
            lambda x: f"{x} * 6 = " + str(x * 6),
            lambda x: f"{x} * 7 = " + str(x * 7),
            lambda x: f"{x} * 8 = " + str(x * 8),
            lambda x: f"{x} * 9 = " + str(x * 9),
            lambda x: f"{x} * 10 = " + str(x * 10)]

def verificar_tabuada():
    tabuada()

def tabuada():
    numero = input("Digite um numero inteiro para gerar a tabuada:\n")
    if not numero.isdigit():
        print("Entrada invalida! Digite um numero inteiro, por favor:\n")
        verificar_tabuada()
    else:
        for n in _tabuada:
            print(n(int(numero)))
        print("\n")
        func_operador()

def soma():
    numero1 = float(input("Informe o primeiro numero:\n"))
    numero2 = float(input("Informe o segundo numero:\n"))
    resultado = _soma(numero1, numero2)
    print("O resultado da soma:", resultado,"\n")
    func_operador()

def subtracao():
    numero1 = float(input("Informe o primeiro numero:\n"))
    numero2 = float(input("Informe o segundo numero:\n"))
    resultado = _subtracao(numero1, numero2)
    print("O resultado da subtracao:", resultado,"\n")
    func_operador()

def multiplicacao():
    numero1 = float(input("Informe o primeiro numero:\n"))
    numero2 = float(input("Informe o segundo numero:\n"))
    resultado = _multiplicacao(numero1, numero2)
    print("O resultado da multiplicacao:", resultado,"\n")
    func_operador()

def divisao():
    numero1 = float(input("Informe o primeiro numero:\n"))
    numero2 = float(input("Informe o segundo numero:\n"))
    resultado = _divisao(numero1, numero2)
    print("O resultado da divisao:", resultado,"\n")
    func_operador()

def sair():
    print("Encerrando. Obrigado por usar o programa! ")
    exit


menu_operacoes = {'0': tabuada,
                  '1': soma,
                  '2': subtracao,
                  '3': multiplicacao,
                  '4': divisao,
                  '5': sair
                  }

def verificar_operador():
    func_operador()

def func_operador():
    operador = input("Informe a operacao desejada:\n0: Tabuada\n1: Soma\n2: Subtracao\n3: Multiplicacao\n4: Divisao\n5: Sair\n ")
    if operador in ("0", "1", "2", "3", "4", "5"):
        menu_operacoes[operador]()
    else:
        print("Entrada invalida. Por favor, digite uma entrada valida: 0, 1, 2, 3, 4, 5\n")
        verificar_operador()

func_operador()

