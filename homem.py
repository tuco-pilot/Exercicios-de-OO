"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor
que 21 anos, ela deve crescer 0,5 cm.
"""


#Função principal do programa
def main():
    nome = input("Digite um nome:")
    idade = define_idade()
    peso = define_peso()
    altura = define_altura()

    #Criando o objeto homem

    homem = Pessoa()
    homem.define_homem(nome,idade,peso,altura)
    
    #Alterando as caracteristicas do homem
    while True:
        escolha = escolhe_alterar()

        if escolha == 2:
            print("\nObrigado por utilizar o programa!")
            break
        else:
            envelheceu = envelhecendo()
            variacao_peso = round(float(input("Digite quanto o peso ira varaiar:")),2)
            idade_inicial = homem.envelhecer(envelheceu)
            homem.engordar(variacao_peso)
            homem.emagrecer(variacao_peso)
            homem.crescer(envelheceu,idade_inicial)

            

#######   Funções usadas dentro do programa  ##########
            
#Função que define uma idade
def define_idade():
    while True:
        idade = int(input("\nDigite uma idade:"))
        if idade >= 0:
            return idade
        print("\nIdade invalida!")

        

#Função que define um peso
def define_peso():
    while True:
        peso = round(float(input("\nDigite um peso:")),2)
        if peso > 0:
            return peso
        print("\nPeso invalido!")

        

#Função que define uma altura
def define_altura():
    while True:
        altura = round(float(input("\nDigite uma altura:")),2)
        if altura > 0:
            return altura
        print("\nAltura invalida!")

        

#Função na qual o usuario escolhe se quer ou não alterar os atributos do "homem".
def escolhe_alterar():
    while True:
        escolha = int(input("\nVocê deseja alterar as caracteristicas do homem? 1-(Sim) 2-(Não):"))
        if escolha == 1:
            return escolha
        elif escolha == 2:
            return escolha
    print("\nEscolha invalida!")

    

#Função que define quantos anos o homem vai envelhecer
def envelhecendo():
    while True:
        envelhece = int(input("Digite quantos anos o homem vai envelhecer:"))
        if envelhece >= 0:
            return envelhece
        print("\nEntrada invalida!")


 
################## Classe que define uma pessoa #####################
        
class Pessoa:
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.peso = 0
        self.altura = 0

    def define_homem(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, envelheceu):
        idade_inicial = self.idade
        self.idade += envelheceu
        print("\n%s envelheceu %i anos e agora está com %i anos de idade."%(self.nome,envelheceu,self.idade))
        return idade_inicial

    def engordar(self, variacao_peso):
        if variacao_peso >= 0:
            self.peso += variacao_peso
            print("\n%s engordou %.2f Kg e agora está com %.2f Kg."%(self.nome, variacao_peso, self.peso))

    def emagrecer(self, variacao_peso):
        if variacao_peso < 0:
            self.peso = self.peso - ((-1)*variacao_peso)
            print("\n%s emagreceu %.2f Kg e agora está com %.2f Kg."%(self.nome,variacao_peso, self.peso))

    def crescer(self,envelheceu, idade_inicial):
        if envelheceu > 0:
            if self.idade <= 21:
                self.altura += 0.05*envelheceu
                print("\n%s teve um aumento de %.2f de altura e agora tem %.2f de altura."%(self.nome, 0.05*envelheceu, self.altura))
            elif idade_inicial < 21 and self.idade >21:
                base = idade_inicial
                while base <21:
                    self.altura += 0.05
                    base += 1
                print("\n%s teve um aumento de %.2f de altura e agora tem %.2f de altura."%(self.nome, (21-idade_inicial)*0.05, self.altura))
            elif idade_inicial > 21:
                print("\nPor ter mais de 21 anos %s não cresce mais."%self.nome)
        else:
            print("\nNão se teve variação de idade!")

main()
