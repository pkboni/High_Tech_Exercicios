#Exercício Calculadora:

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


menu_operacoes = {'0': sair,
                  '1': soma,
                  '2': subtracao,
                  '3': multiplicacao,
                  '4': divisao,
                  }

def verificar_operador():
    func_operador()

def func_operador():
    operador = input("Informe a operacao desejada: \n0: Sair\n1: Soma\n2: Subtracao\n3: Multiplicacao\n4: Divisao\n ")
    if operador in ("0", "1", "2", "3", "4"):
        menu_operacoes[operador]()
    else:
        print("Entrada invalida. Por favor, digite uma entrada valida: 0, 1, 2, 3, 4, 5\n")
        verificar_operador()

func_operador()