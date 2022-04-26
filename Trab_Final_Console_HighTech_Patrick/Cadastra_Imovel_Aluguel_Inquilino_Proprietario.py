#-------------------IMPORTAÇÃO DE BIBLIOTECAS--------------------------------
import os
import platform
import psycopg2   

#-----------------FUNÇÃO PARA CONECTAR AO BANCO DE DADOS----------------------
def conect_db():
  conect = psycopg2.connect(user = 'postgres', password='12486W&a', host='localhost', port='5432', database='Trab_Final')
  return conect

#----------------------------FUNÇÃO PARA LIMPAR TELA--------------------------
def limpar_tela(): 
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")

#------------------FUNÇÃO PARA SAIR DO SISTEMA---------------------------------
def sair(): 
  print("Obrigado por utilizar o sistema!")
  os._exit(0)

#--------FUNÇÃO PARA MENSAGEM DO MENU PRINCIPAL--------------------------------
def mensagem_menu_principal():
  limpar_tela()
  print("**************************************************")
  print("* BEM-VINDO AO SISTEMA DE CADASTRO *")
  print("*------------------------------------------------*") 
  print("* ESCOLHA UMA DAS OPÇÕES DISPONÍVEIS *")
  print("* 0 - SAIR DO SISTEMA *")
  print("* 1 - CADASTRAR UM PROPRIETARIO *")
  print("* 2 - ALTERAR UM PROPRIETARIO *")
  print("* 3 - LISTAR PROPRIETARIOS *")
  print("* 4 - DELETAR PROPRIETARIO *")
  print("* 5 - CADASTRAR IMÓVEL *")
  print("* 6 - ALTERAR UM IMÓVEL *")
  print("* 7 - LISTAR IMÓVEIS *")
  print("* 8 - DELETAR IMÓVEL *")
  print("* 9 - CADASTRAR UM INQUILINO *")
  print("* 10 - ALTERAR UM INQUILINO *")
  print("* 11 - LISTAR INQUILINOS *")
  print("* 12 - DELETAR INQUILINO *")
  print("* 13 - CADASTRAR CORRETOR *")
  print("* 14 - ALTERAR CORRETOR *")
  print("* 15 - LISTAR CORRETORES *")
  print("* 16 - DELETAR CORRETOR *")
  print("* 17 - CADASTRAR CONTRATO *")
  print("* 18 - ALTERAR UM CONTRATO *")
  print("* 19 - LISTAR CONTRATOS *")
  print("* 20 - DELETAR CONTRATO *")
  print("**************************************************")

  #--------------------------------FUNÇÃO DO MENU PRINCIPAL----------------------
def menu_principal():
  try:
    mensagem_menu_principal()
    opcao = input("Informe a opção desejada: ")
    acoes_menu_principal[opcao]()
  except:
    print("Opção inválida.")
    input("Pressione uma tecla para voltar ao menu principal...")
    menu_principal()

################################### PROPRIETARIO ####################################################
#####################################################################################################

#------------FUNÇÃO PARA MENSAGEM DO MENU ALTERAR CADASTRADO PROPRIETARIO----------------------------
def mensagem_menu_alterar_proprietario():
  limpar_tela()
  print("**************************************************")
  print("* ALTERANDO UM PROPRIETÁRIO CADASTRADO EXISTENTE *")
  print("*------------------------------------------------*") 
  print("* ESCOLHA A OPÇÃO PARA LOCALIZAR O CONTATO *")
  print("* 1 - ID *")
  print("* 2 - NOME *")
  print("* 3 - CPF *")
  print("* 0 - MENU PRINCIPAL *")
  print("**************************************************")

#------------------FUNÇÃO PARA MENSAGEM DE CADASTRAR PROPRIETARIO--------------------------
def mensagem_cadastrar_proprietario():
  limpar_tela()
  print("***************************************************")
  print("********* CADASTRANDO UM NOVO PROPRIETARIO *************")
  print("***************************************************")

#--------------------------------CADASTRAR PROPRIETARIO-----------------------------------------------------
def cadastrar_proprietario():
  mensagem_cadastrar_proprietario()
  nome = input("Informe o nome (obrigatório): ")
  fone = input("Informe o fone (obrigatório): ")
  cpf = input("Informe o cpf (obrigatório): ")
  email = input("Informe o endereço de e-mail: (obrigatório)")
  data_nascimento = input("Informe a data de nascimento: (obrigatório)")
  endereco = input("Informe o endereço: (obrigatório)")

  if nome and fone and cpf and email and data_nascimento and endereco:
    confirma = input(f"Confirma cadastro de: {nome}? (S/N): ")
    if confirma.upper() == "S":
      try:
        dade = (nome, fone, cpf, email, data_nascimento, endereco)
        conect = conect_db()
        curs = conect.cursor()
        comand = 'INSERT INTO proprietarios(nome, fone, cpf, email, data_nascimento, endereco) VALUES(%s, %s, %s, %s, %s, %s)'
        curs.execute(comand, dade)
        conect.commit()
        input("Contato cadastrado com sucesso!\nPressione uma tecla para voltar ao menu principal...")
      except:
        input("Ocorreu um erro no cadastro.\nPressione uma tecla para voltar ao menu principal...")
      finally:# closing database connection.
        if conect:
            curs.close()
            conect.close()
            print("PostgreSQL connection is closed")
        else:
          print("PostgreSQL connection is not closed")
    else:
      input("Cadastro cancelado.\nPressione uma tecla para voltar ao menu principal...")
  else:
    input("Todos os campos são obrigatórios.\nPressione uma tecla para voltar ao menu principal...")

  menu_principal()

#--------------------------ALTERAR O PROPRIETARIO CADASTRADO---------------------------------------------
def alterar_proprietario():
  mensagem_menu_alterar_proprietario()
  opcao = input("Informe a opção desejada: ")
  try:
    acoes_menu_alterar_proprietario[opcao]()
  except:
    input("Opção inválida.\nPressione uma tecla para voltar...")
    alterar_proprietario()

#-------------------------LISTA O REGISTRO DE CADASTRO DE PROPRIETARIO---------------------------------------------
def listar_proprietario():
  try:
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, cpf, email, data_nascimento, endereco FROM proprietarios ORDER BY id DESC")
    print("Registro da Tabela")
    lines = curs.fetchall()
    for lin in lines:
      print(f"Id:", lin[0])
      print(f"Nome:", lin[1])
      print(f"Fone:", lin[2])
      print(f"CPF:", lin[3])
      print(f"E-mail:", lin[4])
      print(f"Data de Nascimento:", lin[5])
      print(f"Endereço:", lin[6])
    input("Pressione uma tecla para voltar ao menu principal...")
    curs.close()
    conect.close()
  except:
    print("Ocorreu um erro ao listar.")
  menu_principal()

  #--------------------FUNÇÃO PARA DELETAR UM PROPRIETARIO----------------------------------------------
def deletar_proprietario():
  try:
    escolha = input("Sabe o cpf da pessoa a ser deletado? (S/N): ")
    if escolha.upper() == "N":
      listar_proprietario()
    else:
      cpf_delet = input("informe o cpf que consta no Registro a ser deletado: ")
      conect =conect_db()
      curs = conect.cursor()
      curs.execute(f"DELETE FROM proprietarios WHERE cpf like '%{cpf_delet}%'")
      conect.commit()
  except Exception as err:
    print("Ocorreu um erro ao deletar o cadastro. ", err)
    input("Pressione uma tecla para voltar... ")
  finally:
    if conect:
      curs.close()
      conect.close()
      print("PostgreSQL is closed. ")
  menu_principal()
#-------------------------PESQUISANDO PELO ID DO PROPRIETARIO-------------------------------------------------------
def pesquisar_id_proprietario(id=""):
  try:
    if not id:
      id = input("Informe o ID do Cliente Cadastrado: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, cpf,  email, data_nascimento, endereco FROM proprietarios WHERE id = {id}")
    cadastrado = {}
    for id, nome, fone, cpf, email, data_nascimento, endereco in curs:
      cadastrado = {"id": id, "nome": nome, "fone": fone, "cpf": cpf, "email": email, "data_nascimento": data_nascimento, "endereco": endereco}
    curs.close()
    conect.close()
    alterar_cadastro_proprietario(cadastrado)
  except Exception as err:
    print("Ocorreu erro na busca por ID! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_proprietario()

#-------------------------PESQUISANDO PELO NOME DO PROPRIETARIO-------------------------------------------------------
def pesquisar_nome_proprietario():
  try:
    nome = input("Informe o nome do contato: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, cpf, email, data_nascimento, endereco FROM proprietarios WHERE nome like '%{nome}%'")
    cadastrado = {}
    for id, nome, fone, cpf, email, data_nascimento, endereco in curs:
      cadastrado = {"id": id, "nome": nome, "fone": fone, "cpf": cpf, "email": email, "data_nascimento": data_nascimento, "endereco": endereco}
    curs.close()
    conect.close()
    if cadastrado:
      print(f"Cadastro localizado: id: {cadastrado['id']}, nome: {cadastrado['nome']}, fone: {cadastrado['fone']}, cpf: {cadastrado['cpf']}, "
            f"email: {cadastrado['email']}, data_nascimento: {cadastrado['data_nascimento']}, endereco: {cadastrado['endereco']}]")
      pesquisar_id_proprietario(cadastrado['id'])
  except Exception as err:
    print("Ocorreu erro na busca por nome! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_proprietario()

#-------------------------PESQUISANDO PELO CPF DO PROPRIETARIO -------------------------------------------------------
def pesquisar_cpf_proprietario():
  try:
    cpf = input("Informe o cpf do contato: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, cpf, email, data_nascimento, endereco FROM proprietarios WHERE cpf = '{cpf}'")
    cadastrado = {}
    for id, nome, fone, cpf, email, data_nascimento, endereco in curs:
      cadastrado = {"id": id, "nome": nome, "fone": fone, "cpf": cpf, "email": email, "data_nascimento": data_nascimento, "endereco": endereco}
    curs.close()
    conect.close()
    if cadastrado:
      print(f"Cadastro localizado: id: {cadastrado['id']}, nome: {cadastrado['nome']}, fone: {cadastrado['fone']}, cpf: {cadastrado['cpf']}"
            f"email: {cadastrado['email']}, data_nascimento: {cadastrado['data_nascimento']}, endereco: {cadastrado['endereco']}]")
    pesquisar_id_proprietario(cadastrado['id'])
  except Exception as err:
    print("Ocorreu erro na busca por cpf! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_proprietario()

#----------------------------------ALTERANDO UM PROPRIETARIO CADASTRADO------------------------------------------
def alterar_cadastro_proprietario(cadastrado):
  nome = input(f"Informe o nome ({cadastrado['nome']}): ") or cadastrado['nome']
  fone = input(f"Informe o fone do ({cadastrado['fone']}): ") or cadastrado['fone']
  cpf = input(f"Informe o cpf do ({cadastrado['cpf']}): ") or cadastrado['cpf']
  email = input(f"Informe o email do ({cadastrado['email']}): ") or cadastrado['email']
  data_nascimento = input(f"Informe  a data de nascimento do ({cadastrado['data_nascimento']}): ") or cadastrado['data_nascimento']
  endereco = input(f"Informe o endereço do ({cadastrado['endereco']}): ") or cadastrado['endereco']
  parecer = input(f"Confirma alteração do cadastro: {nome}? (S/N): ")
  if parecer.upper() == "S":
    try:
      conect = conect_db()
      curs = conect.cursor()
      curs.execute(f"UPDATE proprietarios SET nome = '{nome}', fone = '{fone}', cpf = '{cpf}', email = '{email}', data_nascimento = '{data_nascimento}', endereco = '{endereco}' WHERE id = {cadastrado['id']}")
      conect.commit()
      curs.close()
      conect.close()
      input("Cadastro alterado com sucesso!\n Pressione uma tecla para voltar... ")
    except:
      input("Ocorreu um erro na alteração.\nPressione uma tecla para voltar...")
  else:
    input("Alteração cancelada.\nPressione uma tecla para voltar...")
  alterar_proprietario()

############################################# IMÓVEL ################################################################
#####################################################################################################################

#------------------FUNÇÃO PARA MENSAGEM DE CADASTRAR IMÓVEL--------------------------
def mensagem_cadastrar_imovel():
  limpar_tela()
  print("***************************************************")
  print("*********** CADASTRANDO UM NOVO IMÓVEL ************")
  print("***************************************************")


  #------------FUNÇÃO PARA MENSAGEM DO MENU ALTERAR IMÓVEL----------------------------
def mensagem_menu_alterar_imovel():
  limpar_tela()
  print("**************************************************")
  print("* ALTERANDO UM IMÓVEL DO CADASTRO*")
  print("*------------------------------------------------*") 
  print("* ESCOLHA A OPÇÃO PARA LOCALIZAR O IMÓVEL *")
  print("* 1 - ID *")
  print("* 2 - NÚMERO DE MATRÍCULA *")
  print("* 0 - MENU PRINCIPAL *")
  print("**************************************************")

#--------------------------------CADASTRAR IMÓVEL-----------------------------------------------------
def cadastrar_imovel():
  mensagem_cadastrar_imovel()
  qtde_quartos = ""
  logradouro = input("Informe o logradouro (obrigatório): ")
  numero_end = input("Informe o número do endereço (obrigatório): ")
  bairro = input("Informe o bairro (obrigatório): ")
  cidade = input("Informe a cidade: (obrigatório): ")
  cep = input("Informe o CEP: (obrigatório): ")
  descricao = input("Descrição do imóvel. Ex.: Casa/Apart./Terreno/Chácara...: (obrigatório): ")
  area = input("Informe a área do imóvel: (obrigatório): ")
  qtde_quartos = input("Informe a quantidade de quartos. (Não obrigatório): ")
  numero_matricula = input("Informe o número da matrícula do imóvel. (Obrigatório): ")

  if logradouro and numero_end and bairro and cidade and cep and descricao and area and numero_matricula:
    confirma = input(f"Confirma cadastro de: {numero_matricula}? (S/N): ")
    if confirma.upper() == "S":
      try:
        dade = (logradouro, numero_end, bairro, cidade, cep, descricao, area, qtde_quartos, numero_matricula)
        conect = conect_db()
        curs = conect.cursor()
        comand = 'INSERT INTO imoveis(logradouro, numero_end, bairro, cidade, cep, descricao, area, qtde_quartos, numero_matricula) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        curs.execute(comand, dade)
        conect.commit()
        input("Imóvel cadastrado com sucesso!\nPressione uma tecla para voltar ao menu principal...")
      except:
        input("Ocorreu um erro no cadastro.\nPressione uma tecla para voltar ao menu principal...")
      finally:# closing database connection.
        if conect:
          curs.close()
          conect.close()
          print("PostgreSQL connection is closed")
        else:
          print("PostgreSQL connection is not closed")
    else:
      input("Cadastro cancelado.\nPressione uma tecla para voltar ao menu principal...")
  else:
    input("Todos os campos são obrigatórios.\nPressione uma tecla para voltar ao menu principal...")

  menu_principal()

#-------------------------FUNÇÃO ALTERAR IMOVEL---------------------------------------------------
def alterar_imov():
  mensagem_menu_alterar_imovel()
  opcao = input("Informe a opção desejada: ")
  try:
    acoes_menu_alterar_imovel[opcao]()
  except:
    input("Opção inválida.\nPressione uma tecla para voltar...")
    alterar_imov()

#-------------------------LISTAR OS IMÓVEIS DO REGISTRO----------------------------------------------------
def listar_imoveis():
  try:
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, logradouro, numero_end, bairro, cidade, cep, descricao, area, qtde_quartos, numero_matricula FROM imoveis ORDER BY id DESC")
    print("Registro da Tabela")
    lines = curs.fetchall()
    for lin in lines:
      print(f"Id: ", lin[0])
      print(f"Logradouro: ", lin[1])
      print(f"Número do Endereço: ", lin[2])
      print(f"Bairro: ", lin[3])
      print(f"Cidade: ", lin[4])
      print(f"CEP: ", lin[5])
      print(f"Descrição: ", lin[6])
      print(f"Área: ", lin[7])
      print(f"Quantidade de Quartos :", lin[8])
      print(f"Número da Matrícula: ", lin[9])
    input("Pressione uma tecla para voltar ao menu principal...")
    curs.close()
    conect.close()
  except:
    print("Ocorreu um erro ao listar.\nPressione uma tecla para voltar ao menu principal... ")
  menu_principal()

  #--------------------FUNÇÃO PARA DELETAR UM IMÓVEL DO REGISTRO----------------------------------------------
def deletar_imoveis():
  try:
    escolha = input("Sabe o ID do imóvel a ser deletado? (S/N): ")
    if escolha.upper() == "N":
      listar_imoveis()
    else:
      imov_delet = input("informe o ID que consta no Registro a ser deletado: ")
      conect =conect_db()
      curs = conect.cursor()
      curs.execute(f"DELETE FROM imoveis WHERE id = '{imov_delet}'")
      conect.commit()
  except Exception as err:
    print("Ocorreu um erro ao deletar o imóvel do registro.", err)
    input("Pressione uma tecla para voltar... ")
  finally:
    if conect:
      curs.close()
      conect.close()
      print("PostgreSQL is closed. ")
  menu_principal()

#-------------------------PESQUISANDO PELO ID DO IMÓVEL-------------------------------------------------------
def pesquisar_id_imovel(id=""):
  try:
    if not id:
      id = input("Informe o ID do Imóvel Cadastrado: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, logradouro, numero_end, bairro, cidade, cep, descricao, area, qtde_quartos, numero_matricula FROM imoveis WHERE id = {id}")
    cadastrado = {}
    for id, logradouro, numero_end, bairro, cidade, cep, descricao, area, qtde_quartos, numero_matricula in curs:
      cadastrado = {"id": id, "logradouro": logradouro, "numero_end": numero_end, "bairro": bairro, "cidade": cidade, "cep": cep,
                    "descricao": descricao, "area": area, "qtde_quartos":qtde_quartos, "numero_matricula": numero_matricula}
    curs.close()
    conect.close()
    alterar_imovel(cadastrado)
  except Exception as err:
    print("Ocorreu erro na busca pelo ID! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_imov()

#-------------------------PESQUISANDO PELO NÚMERO DA MATRÍCULA DO IMOVEL-------------------------------------------------------
def pesquisar_numero_matricula_imovel():
  try:
    numero_matricula = input("Informe o número da matrícula do imóvel: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, logradouro, numero_end, bairro, cidade, cep, descricao, area, qtde_quartos, numero_matricula FROM imoveis WHERE numero_matricula LIKE '%{numero_matricula}%'")
    cadastrado = {}
    for id, logradouro, numero_end, bairro, cidade, cep, descricao, area, qtde_quartos, numero_matricula in curs:
      cadastrado = {"id": id, "logradouro": logradouro, "numero_end": numero_end, "bairro": bairro, "cidade": cidade, "cep": cep, "descricao": descricao, "area": area, "qtde_quartos":qtde_quartos, "numero_matricula": numero_matricula}
    curs.close()
    conect.close()
    if cadastrado:
      print(f"Imóvel localizado: id: {cadastrado['id']}, logradouro: {cadastrado['logradouro']}, numero_end: {cadastrado['numero_end']}, bairro: {cadastrado['bairro']}, "
            f"cidade: {cadastrado['cidade']}, cep: {cadastrado['cep']}, descricao: {cadastrado['descricao']}, area: {cadastrado['area']}, "
            f"qtde_quartos: {cadastrado['qtde_quartos']}, numero_matricula: {cadastrado['numero_matricula']}]")
      pesquisar_id_imovel(cadastrado['id'])
  except Exception as err:
    print("Ocorreu erro na busca pelo número da matrícula! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_imov()

def alterar_imovel(cadastrado):
  logradouro = input(f"Informe o logradouro ({cadastrado['logradouro']}): ") or cadastrado['logradouro']
  numero_end = input(f"Informe o numero do endereço ({cadastrado['numero_end']}): ") or cadastrado['numero_end']
  bairro = input(f"Informe o bairro do ({cadastrado['bairro']}): ") or cadastrado['bairro']
  cidade = input(f"Informe o cidade do ({cadastrado['cidade']}): ") or cadastrado['cidade']
  cep = input(f"Informe  a cep do ({cadastrado['cep']}): ") or cadastrado['cep']
  descricao = input(f"Informe o descrição do ({cadastrado['descricao']}): ") or cadastrado['descricao']
  area = input(f"Informe  a area do ({cadastrado['area']}): ") or cadastrado['area']
  qtde_quartos = input(f"Informe  a quantidade de quartos do ({cadastrado['qtde_quartos']}): ") or cadastrado['qtde_quartos']
  numero_matricula = input(f"Informe  o numero da matricula ({cadastrado['numero_matricula']}): ") or cadastrado['numero_matricula']
  parecer = input(f"Confirma alteração do cadastro: {numero_matricula}? (S/N): ")
  if parecer.upper() == "S":
    try:
      conect = conect_db()
      curs = conect.cursor()
      curs.execute(f"UPDATE imoveis SET logradouro = '{logradouro}', numero_end = '{numero_end}', bairro = '{bairro}', cidade= '{cidade}', cep= '{cep}', descricao= '{descricao}', area= '{area}', qtde_quartos= '{qtde_quartos}', numero_matricula= '{numero_matricula}' WHERE id = {cadastrado['id']}")
      conect.commit()
      curs.close()
      conect.close()
      input("Cadastro alterado com sucesso!\n Pressione uma tecla para voltar... ")
    except:
      input("Ocorreu um erro na alteração.\nPressione uma tecla para voltar...")
  else:
    input("Alteração cancelada.\nPressione uma tecla para voltar...")
  alterar_imov()

#################################### INQUILINO #####################################################
####################################################################################################

#------------FUNÇÃO PARA MENSAGEM DO MENU ALTERAR CADASTRADO INQUILINO----------------------------
def mensagem_menu_alterar_inquilino():
  limpar_tela()
  print("**************************************************")
  print("* ALTERANDO UM INQUILINO CADASTRADO EXISTENTE *")
  print("*------------------------------------------------*") 
  print("* ESCOLHA A OPÇÃO PARA LOCALIZAR O INQUILINO *")
  print("* 1 - ID *")
  print("* 2 - NOME *")
  print("* 3 - CPF *")
  print("* 0 - MENU PRINCIPAL *")
  print("**************************************************")

#------------------FUNÇÃO PARA MENSAGEM DE CADASTRAR INQUILINO --------------------------
def mensagem_cadastrar_inquilino():
  limpar_tela()
  print("***************************************************")
  print("********* CADASTRANDO UM NOVO INQUILINO *************")
  print("***************************************************")

#--------------------------------CADASTRAR INQUILINO-----------------------------------------------------
def cadastrar_inquilino():
  mensagem_cadastrar_inquilino()
  nome = input("Informe o nome (obrigatório): ")
  fone = input("Informe o fone (obrigatório): ")
  cpf = input("Informe o cpf (obrigatório): ")
  email = input("Informe o endereço de e-mail (obrigatório): ")
  data_nascimento = input("Informe a data de nascimento: (obrigatório)")
  endereco = input("Informe o endereço (obrigatório): ")
  fiador = input("Informe o fiador do inquilino (obrigatorio): ")

  if nome and fone and cpf and email and data_nascimento and endereco and fiador:
    confirma = input(f"Confirma cadastro de: {nome}? (S/N): ")
    if confirma.upper() == "S":
      try:
        dade = (nome, fone, cpf, email, data_nascimento, endereco, fiador)
        conect = conect_db()
        curs = conect.cursor()
        comand = 'INSERT INTO inquilinos(nome, fone, cpf, email, data_nascimento, endereco, fiador) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        curs.execute(comand, dade)
        conect.commit()
        input("Inquilino cadastrado com sucesso!\nPressione uma tecla para voltar ao menu principal...")
      except:
        input("Ocorreu um erro no cadastro.\nPressione uma tecla para voltar ao menu principal...")
      finally:# closing database connection.
        if conect:
            curs.close()
            conect.close()
            print("PostgreSQL connection is closed")
        else:
          print("PostgreSQL connection is not closed")
    else:
      input("Cadastro cancelado.\nPressione uma tecla para voltar ao menu principal...")
  else:
    input("Todos os campos são obrigatórios.\nPressione uma tecla para voltar ao menu principal...")

  menu_principal()

#--------------------------ALTERAR O INQUILINO CADASTRADO---------------------------------------------
def alterar_inquilino():
  mensagem_menu_alterar_inquilino()
  opcao = input("Informe a opção desejada: ")
  try:
    acoes_menu_alterar_inquilino[opcao]()
  except:
    input("Opção inválida.\nPressione uma tecla para voltar...")
    alterar_inquilino()

#-------------------------LISTA O REGISTRO DE CADASTRO DE INQUILINO---------------------------------------------
def listar_inquilinos():
  try:
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, cpf, email, data_nascimento, endereco, fiador FROM inquilinos ORDER BY id DESC")
    print("Registro da Tabela")
    lines = curs.fetchall()
    for lin in lines:
      print(f"Id:", lin[0])
      print(f"Nome:", lin[1])
      print(f"Fone:", lin[2])
      print(f"CPF:", lin[3])
      print(f"E-mail:", lin[4])
      print(f"Data de Nascimento:", lin[5])
      print(f"Endereço:", lin[6])
      print(f"Fiador:", lin[7])
    input("Pressione uma tecla para voltar ao menu principal...")
    curs.close()
    conect.close()
  except:
    print("Ocorreu um erro ao listar.")
  menu_principal()

  #--------------------FUNÇÃO PARA DELETAR UM INQUILINO----------------------------------------------
def deletar_inquilino():
  try:
    escolha = input("Sabe o cpf do inquilino a ser deletado? (S/N): ")
    if escolha.upper() == "N":
      listar_inquilinos()
    else:
      cpf_delet = input("informe o cpf que consta no Registro a ser deletado: ")
      conect =conect_db()
      curs = conect.cursor()
      curs.execute(f"DELETE FROM inquilinos WHERE cpf = '{cpf_delet}'")
      conect.commit()
  except Exception as err:
    print("Ocorreu um erro ao deletar o inquilino do cadastro. ", err)
    input("Pressione uma tecla para voltar... ")
  finally:
    if conect:
      curs.close()
      conect.close()
      print("PostgreSQL is closed. ")
  menu_principal()

#-------------------------PESQUISANDO PELO ID DO INQUILINO-------------------------------------------------------
def pesquisar_id_inquilino(id=""):
  try:
    if not id:
      id = input("Informe o ID do Inquilino Cadastrado: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, cpf,  email, data_nascimento, endereco, fiador FROM inquilinos WHERE id = {id}")
    cadastrado = {}
    for id, nome, fone, cpf, email, data_nascimento, endereco, fiador in curs:
      cadastrado = {"id": id, "nome": nome, "fone": fone, "cpf": cpf, "email": email, "data_nascimento": data_nascimento, "endereco": endereco, "fiador": fiador}
    curs.close()
    conect.close()
    alterar_cadastro_inquilino(cadastrado)
  except Exception as err:
    print("Ocorreu erro na busca por ID! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_inquilino()

#-------------------------PESQUISANDO PELO NOME DO INQUILINO-------------------------------------------------------
def pesquisar_nome_inquilino():
  try:
    nome = input("Informe o nome do inquilino: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, cpf, email, data_nascimento, endereco, fiador FROM inquilinos WHERE nome like '%{nome}%'")
    cadastrado = {}
    for id, nome, fone, cpf, email, data_nascimento, endereco, fiador in curs:
      cadastrado = {"id": id, "nome": nome, "fone": fone, "cpf": cpf, "email": email, "data_nascimento": data_nascimento, "endereco": endereco, "fiador": fiador}
    curs.close()
    conect.close()
    if cadastrado:
      print(f"Cadastro localizado: id: {cadastrado['id']}, nome: {cadastrado['nome']}, fone: {cadastrado['fone']}, cpf: {cadastrado['cpf']}, "
            f"email: {cadastrado['email']}, data_nascimento: {cadastrado['data_nascimento']}, endereco: {cadastrado['endereco']}, fiador: {cadastrado['fiador']}")
      pesquisar_id_inquilino(cadastrado['id'])
  except Exception as err:
    print("Ocorreu erro na busca por nome! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_inquilino()

#-------------------------PESQUISANDO PELO CPF DO INQUILINO -------------------------------------------------------
def pesquisar_cpf_inquilino():
  try:
    cpf = input("Informe o cpf do inquilino: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, cpf, email, data_nascimento, endereco, fiador FROM inquilinos WHERE cpf = '{cpf}'")
    cadastrado = {}
    for id, nome, fone, cpf, email, data_nascimento, endereco, fiador in curs:
      cadastrado = {"id": id, "nome": nome, "fone": fone, "cpf": cpf, "email": email, "data_nascimento": data_nascimento, "endereco": endereco, "fiador": fiador}
    curs.close()
    conect.close()
    if cadastrado:
      print(f"Cadastro localizado: id: {cadastrado['id']}, nome: {cadastrado['nome']}, fone: {cadastrado['fone']}, cpf: {cadastrado['cpf']}"
            f"email: {cadastrado['email']}, data_nascimento: {cadastrado['data_nascimento']}, endereco: {cadastrado['endereco']}, fiador: {cadastrado['fiador']}")
    pesquisar_id_inquilino(cadastrado['id'])
  except Exception as err:
    print("Ocorreu erro na busca por cpf! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_inquilino()

#----------------------------------ALTERANDO UM INQUILINO CADASTRADO------------------------------------------
def alterar_cadastro_inquilino(cadastrado):
  nome = input(f"Informe o nome ({cadastrado['nome']}): ") or cadastrado['nome']
  fone = input(f"Informe o fone do ({cadastrado['fone']}): ") or cadastrado['fone']
  cpf = input(f"Informe o cpf do ({cadastrado['cpf']}): ") or cadastrado['cpf']
  email = input(f"Informe o email do ({cadastrado['email']}): ") or cadastrado['email']
  data_nascimento = input(f"Informe  a data de nascimento do ({cadastrado['data_nascimento']}): ") or cadastrado['data_nascimento']
  endereco = input(f"Informe o endereço do ({cadastrado['endereco']}): ") or cadastrado['endereco']
  fiador = input(f"Informe o fiador do ({cadastrado['fiador']}): ") or cadastrado['fiador']
  parecer = input(f"Confirma alteração do cadastro: {nome}? (S/N): ")
  if parecer.upper() == "S":
    try:
      conect = conect_db()
      curs = conect.cursor()
      curs.execute(f"UPDATE inquilinos SET nome = '{nome}', fone = '{fone}', cpf = '{cpf}', email = '{email}', data_nascimento = '{data_nascimento}', endereco = '{endereco}', fiador = '{fiador}' WHERE id = {cadastrado['id']}")
      conect.commit()
      curs.close()
      conect.close()
      input("Cadastro alterado com sucesso!\n Pressione uma tecla para voltar... ")
    except:
      input("Ocorreu um erro na alteração.\nPressione uma tecla para voltar...")
  else:
    input("Alteração cancelada.\nPressione uma tecla para voltar...")
  alterar_inquilino()


#################################### CORRETOR #####################################################
####################################################################################################

#------------FUNÇÃO PARA MENSAGEM DO MENU ALTERAR CADASTRADO CORRETOR----------------------------
def mensagem_menu_alterar_corretor():
  limpar_tela()
  print("**************************************************")
  print("* ALTERANDO UM CORRETOR CADASTRADO EXISTENTE *")
  print("*------------------------------------------------*") 
  print("* ESCOLHA A OPÇÃO PARA LOCALIZAR O CORRETOR *")
  print("* 1 - ID *")
  print("* 2 - NOME *")
  print("* 3 - CPF *")
  print("* 0 - MENU PRINCIPAL *")
  print("**************************************************")

#----------------------------FUNÇÃO PARA MENSAGEM DE CADASTRAR CORRETOR -----------------------------
def mensagem_cadastrar_corretor():
  limpar_tela()
  print("***************************************************")
  print("********* CADASTRANDO UM NOVO CORRETOR *************")
  print("***************************************************")

#--------------------------------CADASTRAR CORRETOR-----------------------------------------------------
def cadastrar_corretor():
  mensagem_cadastrar_corretor()
  nome = input("Informe o nome (obrigatório): ")
  fone = input("Informe o fone (obrigatório): ")
  doc_identidade = input("Informe o documento de identidade: ")
  cpf = input("Informe o cpf (obrigatório): ")
  email = input("Informe o endereço de e-mail (obrigatório): ")
  data_ent_imobil = input("Informe a data de entrada na imobiliaria: (obrigatório)")
  endereco = input("Informe o endereço (obrigatório): ")
  nivel = input("Informe o nivel do corretor (obrigatorio): ")

  if nome and fone and doc_identidade and cpf and email and data_ent_imobil and endereco and nivel:
    confirma = input(f"Confirma cadastro de: {nome}? (S/N): ")
    if confirma.upper() == "S":
      try:
        dade = (nome, fone, doc_identidade, cpf, email, data_ent_imobil, endereco, nivel)
        conect = conect_db()
        curs = conect.cursor()
        comand = 'INSERT INTO corretores(nome, fone, doc_identidade, cpf, email, data_ent_imobil, endereco, nivel) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        curs.execute(comand, dade)
        conect.commit()
        input("Corretor cadastrado com sucesso!\nPressione uma tecla para voltar ao menu principal...")
      except:
        input("Ocorreu um erro no cadastro.\nPressione uma tecla para voltar ao menu principal...")
      finally:# closing database connection.
        if conect:
            curs.close()
            conect.close()
            print("PostgreSQL connection is closed")
        else:
          print("PostgreSQL connection is not closed")
    else:
      input("Cadastro cancelado.\nPressione uma tecla para voltar ao menu principal...")
  else:
    input("Todos os campos são obrigatórios.\nPressione uma tecla para voltar ao menu principal...")

  menu_principal()

#--------------------------ALTERAR O INQUILINO CADASTRADO---------------------------------------------
def alterar_corretor():
  mensagem_menu_alterar_corretor()
  opcao = input("Informe a opção desejada: ")
  try:
    acoes_menu_alterar_corretor[opcao]()
  except:
    input("Opção inválida.\nPressione uma tecla para voltar...")
    alterar_corretor()

#-------------------------LISTA O REGISTRO DE CADASTRO DE INQUILINO---------------------------------------------
def listar_corretores():
  try:
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, doc_identidade, cpf, email, data_ent_imobil, endereco, nivel FROM corretores ORDER BY id DESC")
    print("Registro da Tabela")
    lines = curs.fetchall()
    for lin in lines:
      print(f"Id:", lin[0])
      print(f"Nome:", lin[1])
      print(f"Fone:", lin[2])
      print(f"Identidade:", lin[3])
      print(f"CPF:", lin[4])
      print(f"E-mail:", lin[5])
      print(f"Data de Entrada na Imobiliaria:", lin[6])
      print(f"Endereço:", lin[7])
      print(f"Nivel:", lin[8])
      
    input("Pressione uma tecla para voltar ao menu principal...")
    curs.close()
    conect.close()
  except:
    print("Ocorreu um erro ao listar.")
  menu_principal()

  #--------------------FUNÇÃO PARA DELETAR UM INQUILINO----------------------------------------------
def deletar_corretor():
  try:
    escolha = input("Sabe o cpf do corretor a ser deletado? (S/N): ")
    if escolha.upper() == "N":
      listar_corretores()
    else:
      cpf_delet = input("informe o cpf que consta no Registro a ser deletado: ")
      conect =conect_db()
      curs = conect.cursor()
      curs.execute(f"DELETE FROM corretores WHERE cpf = '{cpf_delet}'")
      conect.commit()
  except Exception as err:
    print("Ocorreu um erro ao deletar o Corretor do cadastro. ", err)
    input("Pressione uma tecla para voltar... ")
  finally:
    if conect: 
      curs.close()
      conect.close()
      print("PostgreSQL is closed. ")
  menu_principal()

#------------------------- PESQUISANDO PELO ID DO CORRETOR -------------------------------------------------------
def pesquisar_id_corretor(id=""):
  try:
    if not id:
      id = input("Informe o ID do Corretor Cadastrado: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, doc_identidade, cpf,  email, data_ent_imobil, endereco, nivel FROM corretores WHERE id = {id}")
    cadastrado = {}
    for id, nome, fone, doc_identidade, cpf, email, data_ent_imobil, endereco, nivel in curs:
      cadastrado = {"id": id, "nome": nome, "fone": fone, "doc_identidade": doc_identidade, "cpf": cpf, "email": email, "data_ent_imobil": data_ent_imobil, "endereco": endereco, "nivel": nivel}
    curs.close()
    conect.close()
    alterar_cadastro_corretor(cadastrado)
  except Exception as err:
    print("Ocorreu erro na busca por ID! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_corretor()

#-------------------------PESQUISANDO PELO NOME DO CORRETOR-------------------------------------------------------
def pesquisar_nome_corretor():
  try:
    nome = input("Informe o nome do Corretor: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, doc_identidade, cpf, email, data_ent_imobil, endereco, nivel FROM inquilinos WHERE nome like '%{nome}%'")
    cadastrado = {}
    for id, nome, fone, doc_identidade, cpf, email, data_ent_imobil, endereco, nivel in curs:
      cadastrado = {"id": id, "nome": nome, "fone": fone, "doc_identidade": doc_identidade,"cpf": cpf, "email": email, "data_ent_imobil": data_ent_imobil, "endereco": endereco, "nivel": nivel}
    curs.close()
    conect.close()
    if cadastrado:
      print(f"Cadastro localizado: id: {cadastrado['id']}, nome: {cadastrado['nome']}, fone: {cadastrado['fone']}, doc_identidade: {cadastrado['doc_identidade']}, cpf: {cadastrado['cpf']}, "
            f"email: {cadastrado['email']}, data_ent_imobil: {cadastrado['data_ent_imobil']}, endereco: {cadastrado['endereco']}, nivel: {cadastrado['nivel']}")
      pesquisar_id_corretor(cadastrado['id'])
  except Exception as err:
    print("Ocorreu erro na busca por nome! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_corretor()

#-------------------------PESQUISANDO PELO CPF DO CORRETOR -------------------------------------------------------
def pesquisar_cpf_corretor():
  try:
    cpf = input("Informe o cpf do corretor: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, nome, fone, doc_identidade, cpf, email, data_ent_imobil, endereco, nivel FROM corretores WHERE cpf = '{cpf}'")
    cadastrado = {}
    for id, nome, fone, doc_identidade, cpf, email, data_ent_imobil, endereco, nivel in curs:
      cadastrado = {"id": id, "nome": nome, "fone": fone, "doc_identidade": doc_identidade,"cpf": cpf, "email": email, "data_ent_imobil": data_ent_imobil, "endereco": endereco, "nivel": nivel}
    curs.close()
    conect.close()
    if cadastrado:
      print(f"Cadastro localizado: id: {cadastrado['id']}, nome: {cadastrado['nome']}, fone: {cadastrado['fone']}, doc_identidade: {cadastrado['doc_identidade']}, cpf: {cadastrado['cpf']}"
            f"email: {cadastrado['email']}, data_ent_imobil: {cadastrado['data_ent_imobil']}, endereco: {cadastrado['endereco']}, nivel: {cadastrado['nivel']}")
    pesquisar_id_corretor(cadastrado['id'])
  except Exception as err:
    print("Ocorreu erro na busca por cpf! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_corretor()

#----------------------------------ALTERANDO UM CORRETOR CADASTRADO------------------------------------------
def alterar_cadastro_corretor(cadastrado):
  nome = input(f"Informe o nome ({cadastrado['nome']}): ") or cadastrado['nome']
  fone = input(f"Informe o fone do ({cadastrado['fone']}): ") or cadastrado['fone']
  doc_identidade = input(f"Informe a Identidade do ({cadastrado['doc_identidade']}): ") or cadastrado['doc_identidade']
  cpf = input(f"Informe o cpf do ({cadastrado['cpf']}): ") or cadastrado['cpf']
  email = input(f"Informe o email do ({cadastrado['email']}): ") or cadastrado['email']
  data_ent_imobil = input(f"Informe  a data de entrada na imobiliaria ({cadastrado['data_ent_imobil']}): ") or cadastrado['data_ent_imobil']
  endereco = input(f"Informe o endereço do ({cadastrado['endereco']}): ") or cadastrado['endereco']
  nivel = input(f"Informe o nivel do ({cadastrado['nivel']}): ") or cadastrado['nivel']
  parecer = input(f"Confirma alteração do cadastro: {nome}? (S/N): ")
  if parecer.upper() == "S":
    try:
      conect = conect_db()
      curs = conect.cursor()
      curs.execute(f"UPDATE corretores SET nome = '{nome}', fone = '{fone}', doc_identidade = '{doc_identidade}', cpf = '{cpf}', email = '{email}', data_ent_imobil = '{data_ent_imobil}', endereco = '{endereco}', nivel = '{nivel}' WHERE id = {cadastrado['id']}")
      conect.commit()
      curs.close()
      conect.close()
      input("Cadastro alterado com sucesso!\n Pressione uma tecla para voltar... ")
    except:
      input("Ocorreu um erro na alteração.\nPressione uma tecla para voltar...")
  else:
    input("Alteração cancelada.\nPressione uma tecla para voltar...")
  alterar_corretor()

  ##################################################### CONTRATO ############################################################
  ###########################################################################################################################

#------------------FUNÇÃO PARA MENSAGEM DE CADASTRAR CONTRATO--------------------------
def mensagem_cadastrar_contrato():
  limpar_tela()
  print("***************************************************")
  print("*********** CADASTRANDO UM NOVO CONTRATO ************")
  print("***************************************************")

  #------------FUNÇÃO PARA MENSAGEM DO MENU ALTERAR CONTRATO----------------------------
def mensagem_menu_alterar_contrato():
  limpar_tela()
  print("**************************************************")
  print("* ALTERANDO UM CONTRATO DO CADASTRO*")
  print("*------------------------------------------------*") 
  print("* ESCOLHA A OPÇÃO PARA LOCALIZAR O CONTRATO *")
  print("* 1 - ID *")
  print("* 2 - NÚMERO DE REGISTRO *")
  print("* 0 - MENU PRINCIPAL *")
  print("**************************************************")

#--------------------------------CADASTRAR CONTRATO-----------------------------------------------------
def cadastrar_contrato():
  mensagem_cadastrar_contrato() 
  data_assinat = input("Informe a data da assinatura do contrato (obrigatório): ")
  valor_aluguel = input("Informe o valor do aluguel (obrigatório): ")
  data_ent_imovel = input("Informe a data de entrada no imóvel (obrigatório): ")
  duracao = input("Informe a duração do contrato: (obrigatório)")
  termos = input("Espaço para os termos do contrato: (obrigatório)")
  num_regist = input("Informe o número de registro do contrato: (obrigatório)")

  if data_assinat and valor_aluguel and data_ent_imovel and duracao and termos and num_regist:
    confirma = input(f"Confirma cadastro de: {num_regist}? (S/N): ")
    if confirma.upper() == "S":
      try:
        dade = (data_assinat, valor_aluguel, data_ent_imovel, duracao, termos, num_regist)
        conect = conect_db()
        curs = conect.cursor()
        comand = 'INSERT INTO contratos(data_assinat, valor_aluguel, data_ent_imovel, duracao, termos, num_regist) VALUES(%s, %s, %s, %s, %s, %s)'
        curs.execute(comand, dade)
        conect.commit()
        input("Contrato cadastrado com sucesso!\nPressione uma tecla para voltar ao menu principal...")
      except:
        input("Ocorreu um erro no cadastro do contrato.\nPressione uma tecla para voltar ao menu principal...")
      finally:# closing database connection.
        if conect:
            curs.close()
            conect.close()
            print("PostgreSQL connection is closed")
        else:
          print("PostgreSQL connection is not closed")
    else:
      input("Cadastro cancelado.\nPressione uma tecla para voltar ao menu principal...")
  else:
    input("Todos os campos são obrigatórios.\nPressione uma tecla para voltar ao menu principal...")

  menu_principal()

#--------------------------ALTERAR O CONTRATO CADASTRADO---------------------------------------------
def alterar_contrato():
  mensagem_menu_alterar_contrato()
  opcao = input("Informe a opção desejada: ")
  try:
    acoes_menu_alterar_contrato[opcao]()
  except:
    input("Opção inválida.\nPressione uma tecla para voltar...")
    alterar_contrato()

#-------------------------LISTA O REGISTRO DE CADASTRO DE CONTRATOS---------------------------------------------
def listar_contratos():
  try:
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, data_assinat, valor_aluguel, data_ent_imovel, duracao, termos, num_regist FROM contratos ORDER BY id DESC")
    print("Registro da Tabela")
    lines = curs.fetchall()
    for lin in lines:
      print(f"Id:", lin[0])
      print(f"Data Assinatura:", lin[1])
      print(f"Valor Aluguel:", lin[2])
      print(f"Data Entrada no Imóvel:", lin[3])
      print(f"Duração:", lin[4])
      print(f"Termos:", lin[5])
      print(f"Numero de Registro do Contrato:", lin[6])
    input("Pressione uma tecla para voltar ao menu principal...")
    curs.close()
    conect.close()
  except:
    print("Ocorreu um erro ao listar.")
  menu_principal()

  #--------------------FUNÇÃO PARA DELETAR UM CONTRATO CADASTRADO----------------------------------------------
def deletar_contrato():
  try:
    escolha = input("Sabe o número de registro do contrato a ser deletado? (S/N): ")
    if escolha.upper() == "N":
      listar_contratos()
    else:
      num_regist_delet = input("informe o número de registro do Imóvel a ser deletado: ")
      conect =conect_db()
      curs = conect.cursor()
      curs.execute(f"DELETE FROM contratos WHERE num_regist = '{num_regist_delet}'")
      #curs.execute(f"DELETE FROM imoveis WHERE id = '{imov_delet}'")
      conect.commit()
  except Exception as err:
    print("Ocorreu um erro ao deletar o contrato cadastrado. ", err)
    input("Pressione uma tecla para voltar... ")
  finally:
    if conect:
      curs.close()
      conect.close()
      print("PostgreSQL is closed. ")
  menu_principal()
#-------------------------PESQUISANDO PELO ID DO CONTRATO-------------------------------------------------------
def pesquisar_id_contrato(id=""):
  try:
    if not id:
      id = input("Informe o ID do Contrato Cadastrado: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, data_assinat, valor_aluguel, data_ent_imovel, duracao, termos, num_regist FROM contratos WHERE id = {id}")
    cadastrado = {}
    for id, data_assinat, valor_aluguel, data_ent_imovel, duracao, termos, num_regist in curs:
      cadastrado = {"id": id, "data_assinat": data_assinat, "valor_aluguel": valor_aluguel, "data_ent_imovel": data_ent_imovel, "duracao": duracao, "termos": termos, "num_regist": num_regist}
    curs.close()
    conect.close()
    alterar_cadastro_contrato(cadastrado)
  except Exception as err:
    print("Ocorreu erro na busca por ID! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_contrato()

#-------------------------PESQUISANDO PELO NUMERO DE REGISTRO DO CONTRATO-------------------------------------
def pesquisar_num_regist_contrato():
  try:
    num_regist = input("Informe o número de registro do contrato: ")
    conect = conect_db()
    curs = conect.cursor()
    curs.execute(f"SELECT id, data_assinat, valor_aluguel, data_ent_imovel, duracao, termos, num_regist FROM contratos WHERE num_regist like '%{num_regist}%'")
    cadastrado = {}
    for id, data_assinat, valor_aluguel, data_ent_imovel, duracao, termos, num_regist in curs:
      cadastrado = {"id": id, "data_assinat": data_assinat, "valor_aluguel": valor_aluguel, "data_ent_imovel": data_ent_imovel, "duracao": duracao, "termos": termos, "num_regist": num_regist}
    curs.close()
    conect.close()
    if cadastrado:
      print(f"Cadastro localizado: id: {cadastrado['id']}, data_assinat: {cadastrado['data_assinat']}, valor_aluguel: {cadastrado['valor_aluguel']}, data_ent_imovel: {cadastrado['data_ent_imovel']}, "
            f"duracao: {cadastrado['duracao']}, termos: {cadastrado['termos']}, num_regist: {cadastrado['num_regist']}]")
      pesquisar_id_contrato(cadastrado['id'])
  except Exception as err:
    print("Ocorreu erro na busca pelo numero de registro! ", err)
    input("Pressione uma tecla para voltar...")
    alterar_contrato()


#----------------------------------ALTERANDO UM CONTRATO CADASTRADO------------------------------------------
def alterar_cadastro_contrato(cadastrado):
  data_assinat = input(f"Informe o data_assinat ({cadastrado['data_assinat']}): ") or cadastrado['data_assinat']
  valor_aluguel = input(f"Informe o valor_aluguel do ({cadastrado['valor_aluguel']}): ") or cadastrado['valor_aluguel']
  data_ent_imovel = input(f"Informe o data_ent_imovel do ({cadastrado['data_ent_imovel']}): ") or cadastrado['data_ent_imovel']
  duracao = input(f"Informe a duração do ({cadastrado['duracao']}): ") or cadastrado['duracao']
  termos = input(f"Espaço para os termos do contrato ({cadastrado['termos']}): ") or cadastrado['termos']
  num_regist = input(f"Informe o endereço do ({cadastrado['num_regist']}): ") or cadastrado['num_regist']
  parecer = input(f"Confirma alteração do cadastro: {data_assinat}? (S/N): ")
  if parecer.upper() == "S":
    try:
      conect = conect_db()
      curs = conect.cursor()
      curs.execute(f"UPDATE contratos SET data_assinat = '{data_assinat}', valor_aluguel = '{valor_aluguel}', data_ent_imovel = '{data_ent_imovel}', duracao = '{duracao}', termos = '{termos}', num_regist = '{num_regist}' WHERE id = {cadastrado['id']}")
      conect.commit()
      curs.close()
      conect.close()
      input("Cadastro de contrato alterado com sucesso!\n Pressione uma tecla para voltar... ")
    except:
      input("Ocorreu um erro na alteração.\nPressione uma tecla para voltar...")
  else:
    input("Alteração cancelada.\nPressione uma tecla para voltar...")
  alterar_contrato()

################################## DICIONARIOS E CHAMADA DO MAIN #######################################
#############################################################################################

#-----------------------------DICIONÁRIO DAS FUNÇÕES PARA ALTERAR CONTRATO-------------------
acoes_menu_alterar_contrato = { 
                              '1': pesquisar_id_contrato,
                              '2': pesquisar_num_regist_contrato,
                              '0': menu_principal
                              }

#----------------------------- DICIONÁRIO DAS FUNÇÕES PARA ALTERAR IMÓVEL -------------------
acoes_menu_alterar_imovel = {
                            '1': pesquisar_id_imovel,
                            '2': pesquisar_numero_matricula_imovel,
                            '0': menu_principal
                            }

#-----------------------------DICIONÁRIO DAS FUNÇÕES PARA ALTERAR INQUILINO-------------------
acoes_menu_alterar_inquilino = { 
                              '1': pesquisar_id_inquilino,
                              '2': pesquisar_nome_inquilino,
                              '3': pesquisar_cpf_inquilino,
                              '0': menu_principal
                              }

#----------------------------- DICIONÁRIO DAS FUNÇÕES PARA ALTERAR CADASTRO DE PROPRIETARIO --------------------------
acoes_menu_alterar_proprietario = {
                                  '1': pesquisar_id_proprietario,
                                  '2': pesquisar_nome_proprietario,
                                  '3': pesquisar_cpf_proprietario,
                                  '0': menu_principal
                                  }

#----------------------------- DICIONÁRIO DAS FUNÇÕES PARA ALTERAR CADASTRO DE CORRETOR --------------------------
acoes_menu_alterar_corretor = {
                              '1': pesquisar_id_corretor,
                              '2': pesquisar_nome_corretor,
                              '3': pesquisar_cpf_corretor,
                              '0': menu_principal
                              }

#----------------------------DICIONÁRIO PARA AS FUNÇÕES DO MENU PRINCIPAL-----------
acoes_menu_principal = {
                        '0': sair,
                        '1': cadastrar_proprietario,
                        '2': alterar_proprietario,
                        '3': listar_proprietario,
                        '4': deletar_proprietario,
                        '5': cadastrar_imovel,
                        '6': alterar_imov,
                        '7': listar_imoveis,
                        '8': deletar_imoveis,
                        '9': cadastrar_inquilino,
                        '10': alterar_inquilino,
                        '11': listar_inquilinos,
                        '12': deletar_inquilino,
                        '13': cadastrar_corretor,
                        '14': alterar_corretor,
                        '15': listar_corretores,
                        '16': deletar_corretor,
                        '17': cadastrar_contrato,
                        '18': alterar_contrato,
                        '19': listar_contratos,
                        '20': deletar_contrato
                        }

if __name__ == "__main__":
  menu_principal()
















