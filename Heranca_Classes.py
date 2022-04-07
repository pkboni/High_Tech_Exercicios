#Exercicio de Herança de Classes:
#Fazer a herança das seguintes classes:
#MeioTransporte
#Terrestre            / Aquatico           / Aereo
#Carro / Caminhao     Remo / Barco       Avião / Helicóptero
#Use a imaginação para criar e separar os seus atributos
#Para o dia 07/04
#import os

class MeioDeTransporte(object):
    def __init__(self, NumeroDePassageiros, NumeroDeRegistro): 
        self.NumeroDePassageiros = NumeroDePassageiros
        self.DocumentoDeRegistro = NumeroDeRegistro

    def registro_passageiros(self, NumeroDePassageiros, NumeroDeRegistro):
        print("Numero de registro da viagem:", NumeroDeRegistro, "com", NumeroDePassageiros, "passageiros\n")


class Terrestre(MeioDeTransporte):    #CategoriaTerrestre = {'1': "Automovel", '2': "Mototaxi"}
    def __init__(self, NumeroDePassageiros, NumeroDeRegistro, Ponto):
        super().__init__(NumeroDePassageiros, NumeroDeRegistro)
        self.Ponto = Ponto


class Automovel(Terrestre):
    def __init__(self, NumeroDePassageiros, NumeroDeRegistro, Ponto, Sedan, Arcondicionado): #Sedan: Sim/Nao  Arcondicoinado: Sim/Nao
        super().__init__(NumeroDePassageiros, NumeroDeRegistro, Ponto)        
        self.Sedan = Sedan
        self.Arcondiconado = Arcondicionado
 
    def calcular_pagamento(NumeroDePassageiros):
        print(NumeroDePassageiros*25.00)

    def nivel(self):
        print(self.Sedan, self.Arcondiconado)
        
    
class Mototaxi(Terrestre):
    def __init__(self, NumeroDePassageiros, NumeroDeRegistro, Ponto, Porte, Cilindradas): #Porte: alta, baixa; Cilindradas: 125, 250, 500,...
        super().__init__(NumeroDePassageiros, NumeroDeRegistro, Ponto)
        self.Porte = Porte
        self.Cilindradas = Cilindradas

    def moto(self):
        print(self.Porte, self.Cilindradas)

passageiro_auto = Automovel(NumeroDePassageiros= 23, NumeroDeRegistro= 1111, Ponto= "Araras", Sedan= "Sedan", Arcondicionado= "Ar condicionado")
passageiro_auto.nivel()


class Aquatico(MeioDeTransporte):    #CategoriaAquatico = {'1': "Barco", '2': "Bote"}
    def __init__(self, NumeroDePassageiros, NumeroDeRegistro, Porto):
        super().__init__(NumeroDePassageiros, NumeroDeRegistro)
        self.Porto = Porto
    

class Barco(Aquatico):
    def __init__(self, NumeroDePassageiros, NumeroDeRegistro, Porto, Potencia, Coberto):
        super().__init__(NumeroDePassageiros, NumeroDeRegistro, Porto)
        self.Potencia = Potencia
        self.Coberto = Coberto

    def barco(self):
        print(self.Potencia, self.Coberto)


class Bote(Aquatico):
    def __init__(self, NumeroDePassageiros, NumeroDeRegistro, Porto, Remo, Acento):
        super().__init__(NumeroDePassageiros, NumeroDeRegistro, Porto)
        self.Remo = Remo
        self.Acento = Acento

    def bote(self):
        print(self.Remo, self.Acento)

passageiro_barco = Barco(NumeroDePassageiros= 23, NumeroDeRegistro= 1111, Porto ="Santos", Potencia= "200 hp", Coberto= "Sim")
passageiro_barco.barco()


class Aereo(MeioDeTransporte):    #CategoriaAereo = {'1': "Helicoptero", '2': "Aviao"}
    def __init__(self, NumeroDePassageiros, NumeroDeRegistro, Taxi):
        super().__init__(NumeroDePassageiros, NumeroDeRegistro)
        self.Taxi = Taxi

class Helicoptero(Aereo):
    def __init__(self, NumeroDePassageiros, NumeroDeRegistro, Taxi, Heliponto, Acentos_disponiveis):
        super().__init__(NumeroDePassageiros, NumeroDeRegistro, Taxi)
        self.Heliponto = Heliponto
        self.Acentos_disponiveis = Acentos_disponiveis
    
    def helicoptero(self):
        print(self.Heliponto, self.Acentos_disponiveis)


class Aviao(Aereo):
    def __init__(self, NumeroDePassageiros, NumeroDeRegistro, Taxi, Classes, ServicoBordo):
        super().__init__(NumeroDePassageiros, NumeroDeRegistro, Taxi)
        self.Classes = Classes
        self.ServicoBordo = ServicoBordo

    def aviao(self):
        print(self.Classes, self.ServicoBordo)
    
passageiro_aviao = Aviao(NumeroDePassageiros= 23, NumeroDeRegistro= 1111, Taxi= "Nao", Classes= "Sim, 3 classes", ServicoBordo= "Nao")
passageiro_aviao.aviao()


class Anfibio(Terrestre, Aquatico):  #Multipla Heranca
    def __init__(self, Ponto, Porto):
        self.Ponto = Ponto
        self.Porto = Porto

    def anfibio(self):
        print("Veiculo anfibio! Ponto:", self.Ponto, ". Porto:", self.Porto)
passageiro_anfibio = Anfibio("Araraquara", "Vitoria")
passageiro_anfibio.anfibio()
#print(passageiro_anfibio.Ponto)
#print(passageiro_anfibio.Porto)








#class Pessoa():
#    def __init__(self, nome, documento, localidade):
#      self.nome = nome
#      self.documento = documento
#      self.localidade = localidade

#    def dar_entrada(self):
#        print("Entrando")

#    def alugar(self):
#        print("Alugando")



#class PessoaJuridica(Pessoa):
#    def __init__(self, nome, documento, localidade, data_fundacao):
#        super().__init__(nome, documento, localidade)
#        self.data_fundacao = data_fundacao
        
#    def fundar(self):
#        print("Fundando")


#class PessoaFisica(Pessoa):
#    def __init__(self, nome, documento, localidade, data_nascimento):
#        super().__init__(nome, documento, localidade)
#        self.data_nascimento = data_nascimento

#    def nascer(self):
#        print("Nascendo")
#        self.__metodo()
    
#    def __metodo(self):
#        print("metodo")

#pf = PessoaFisica(nome="Jeff", documento="123123", localidade="RJ", data_nascimento="01/01/2001")
#pf.nascer()
#pf.dar_entrada()
#pf.alugar()
#print(f"Documento da pessoa: {pf.documento} ")

#pj = PessoaJuridica("Jeff Company", "1233123/0002-4", "RJ", "01/01/2000")
#pj.fundar()
#pj.dar_entrada()
#pj.alugar()
#print(f"Documento da empresa: {pj.documento} ")

