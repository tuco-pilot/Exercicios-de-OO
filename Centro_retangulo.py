"""
Classe Ponto e Retangulo:
Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior
esquerdo do retângulo, que deve ser um objeto da classe Ponto.

A função para encontrar o centro do retângulo deve retornar o valor para um
objeto do tipo ponto que indique os valores de x e y para o centro do objeto.

O valor do centro do objeto deve ser mostrado na tela

Crie um menu para alterar os valores do retângulo e imprimir o centro deste
retângulo.
"""

###### Classes #######
class ponto:
    def __init__(self):
        self.x = 0
        self.y = 0
    

class retangulo:
    def __init__(self, ponto):
        self.base = 0
        self.altura = 0
        self.ponto = ponto

    def ponto_central(self):
        self.x = (self.ponto.x)/2 + (self.base/2 - self.ponto.x/2)     
        self.y = (self.ponto.y)/2 + (self.altura/2 - self.ponto.y/2)

    def printa_central(self):
        print("O ponto central do retangulo é a cooordenada (%.2f,%.2f)."%(self.x,self.y))
            

############# Funções do programa #########################


#Função principal do programa
def main():
    point = ponto()
    retan = retangulo(point)
    define_retangulo(retan)
    define_ponto_x(point,retan)
    define_ponto_y(point,retan)

    while True:
        escolha = menu()
        if escolha == "s":
            print("\nObrigao por usar o programa!")
            break
        elif escolha == "i":
            retan.ponto_central()
            retan.printa_central()
        elif escolha == "a":
            define_retangulo(retan)
            define_ponto_x(point,retan)
            define_ponto_y(point,retan)
            print("\nRetangulo definido com %.2f de base e %.2f de altura"%(retan.base,retan.altura))
            print("Novo vértice de partida definido como sendo as coordenadas (%.2f,%.2f)"%(point.x,point.y))
           
#Função que da valor para o retangulo
def define_retangulo(retan):
    retan.base = round(float(input("Digite qual vai ser a base do retangulo:")),2)
    retan.altura = round(float(input("Digite qual vai ser a altura do retangulo:")),2)
    while retan.base <= 0:
        print("\nA base do retangulo deve ser maior do que 0!")
        retan.base = round(float(input("Digite qual vai ser a base do retangulo:")),2)
    while retan.altura <= 0:
        print("\nA altura do retangulo deve ser maior do que 0!")
        retan.altura = round(float(input("Digite qual vai ser a altura do retangulo:")),2)

#Função que define o vertice inicial na coordenada x
def define_ponto_x(point,retan):
    while True:
        point.x = round(float(input("\nDigite o ponto x do vértice:")),2)
        if point.x <= 0:
            print("\nO ponto x deve ser maior do que 0!")
        elif point.x > retan.base:
            print("\n O ponto x do vértice saiu dos limites do retangulo!")
        else:
            break

#Função que define o vertice inicial na coordenada y
def define_ponto_y(point,retan):
    while True:
        point.y = round(float(input("\nDigite o ponto y do vértice:"),),2)
        if point.y <= 0:
            print("\nO ponto y deve ser maior do que 0!")
        elif point.y > retan.altura:
            print("\nO ponto y do vértice saiu dos limites do retangulo!")
        else:
            break

#Função na qual o usuário faz a sua escolha
def menu():
    while True:
        opcao = input("\nVocê deseja alterar o seu retangulo e seu vértice(a), imprimir o centro do retangulo(i) ou sair do programa(s)?:")
        opcao.lower()
        if not opcao.isalpha():
            print("\nEntrada invalida!")
        if opcao in ["a","i","s"]:
            return opcao
        print("\nDigite umas das letras solicitadas!")
        
main()      
