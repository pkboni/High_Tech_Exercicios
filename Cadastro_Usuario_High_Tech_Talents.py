# Fazer um cadastro de 3 campos e guarda-lo em 
# um dicionário (Console)
# 1-) Entender o problema
# 2-) Planejar a solução
# -Criar um menu no console com 3 opções: 
#   - Sair 
#   - Cadastrar 
#   - Listar
# 3-) Dividir/Planejar Tarefas
#   - Preparar um arquivo Python (Este aqui mesmo)
#   - Criar Loop para o menu principal
#   - Criar "Tela" Cadastrar 
#       -Perguntar campo Nome
#       -Perguntar campo Data Nascimento
#       -Perguntar campo Endereço
#   - Criar "Tela" Listar
#       -Preparar Prints Dicionario
#   - Criar Funcionalidade Sair    
# 4-) Estimar tempo de desenvolvimento (Até o final da aula)

#Exercício 2 de 2: Cadastro

def nome():
    while True:
        Nome = str("")
        Nome = input("Informe o seu primeiro nome: ")
        if Nome.isprintable() and Nome.isalpha() and not Nome.isdigit():
            return Nome
        else:
            print("Entrada invalida! Digite apenas o seu primeiro nome: ")

nome1 = nome()

def sobrenome():
    while True:
        Sobrenome = str("")
        Sobrenome = input("Informe o seu sobrenome: ")
        if Sobrenome.isprintable() and Sobrenome.isalpha() and not Sobrenome.isdigit():
            return Sobrenome
        else:
            print("Entrada invalida! Digite apenas o seu ultimo sobrenome: ")

sobrenome1 = sobrenome()

nome_sobrenome = nome1 + " " + sobrenome1

def bem_vindo(nome_sobrenome):
    print(f"Seja bem-vindo {nome_sobrenome} !\n")

bem_vindo(nome_sobrenome)

lista_usuarios = []

def cadastrar_usuario():
    nome = input("Informe o seu nome completo: ")
    data_nasc = input("Informe a sua data de nascimento: ")
    endereco = input("Forneca o seu endereco: ")

    if nome and data_nasc and endereco:
        confirmador = input(f"Confirma cadastro do contato {nome}? (S/N)")
        if confirmador.upper() == "S":
            registro = {"Nome":nome, "Data_Nascimento":data_nasc, "Endereco":endereco}
            lista_usuarios.append(registro)
        else:
            print("Retornando ao inicio! ")
            cadastrar_usuario()
    else: 
        print("Opcao invalida! ")
        menu_principal()
    menu_principal()


def listar_usuario():
    for item in lista_usuarios:
        print(item)
    return menu_principal()


def sair():
    print("Encerrando o uso do sistema. Obrigado, volte sempre!")
    return exit


opcoes_menu_principal = {
                         '1': cadastrar_usuario,
                         '2': listar_usuario,
                         '3': sair
                         }

def verificar_menu_principal():
    menu_principal()

def menu_principal():
    print("Bem vindo ao sistema de cadastro.\nEscolha uma opcao: ")
    print("1 - Cadastrar usuario.\n2 - Listar usuarios\n3 - Sair do sistema de cadastro ")
    opcao_escolhida = input("Informe a opcao desejada: ")
    if opcao_escolhida in ("1", "2", "3"):
        opcoes_menu_principal[opcao_escolhida]()
    else:
        print("Digite um numero valido. Numeros validos: 1, 2, 3\n")
        verificar_menu_principal()

menu_principal()




#if __name__ == "__main__":
#    menu_principal()

#lista = []
#while True:
#    print("Selecione uma opcao:")
#    print("1 - Cadastrar")
#    print("2 - Listar")
#    print("3 - Sair")
#    opcao = int(input(""))
#    if opcao in [1,2,3]:
#        if opcao == 1: #Cadastrar
#            nome = ""
#            data_nasc = ""
#            endereco = ""
#            while nome == "":
#                nome = input("Coloque o nome: ")
#            while data_nasc == "":
#                data_nasc = input("Coloque a data de nascimento: ")
#            while endereco == "":
#                endereco = input("Coloque o endereco: ")

#            registro = {"Nome":nome, "Data_Nascimento":data_nasc, "Endereco": endereco}
#            lista.append(registro)
#            print("Sucesso! Cadastrado!")
#        elif opcao == 2: #Listar
#            for item in lista:
#                print(item)
            
#        elif opcao == 3:#Sair
#            print("Saindo do sistema...")
#            break
#    else:
#        print("Opcao Invalida!")
