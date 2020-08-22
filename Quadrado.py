"""
Classe Quadrado: Crie uma clasee que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e Calcular Área;
"""

class Meu_Quadrado:
    def __init__(self,L):
        self.lado = L
        
    def Muda_lado(self):
        while True:
            escolha = int(input("\nDeseja mudar o lado do seu quadrado? 1(Sim) 2(Não):"))
            if escolha == 1:
                self.lado = int(input("\nDigite um novo valor para o lado do quadrado:"))
                break
            elif escolha == 2:
                break
            print("\nEscolha invalida")

    def Retorna_Valor_Lado(self):
        print("O valor do lado desse quadrado ficou definido como sendo %i"%(self.lado))

    def Calculo_Area(self):
        area = self.lado**2
        print("A área do circulo de lado %i é igual a %i"%(self.lado,area))

quadrado = Meu_Quadrado(5)

quadrado.Muda_lado()
quadrado.Retorna_Valor_Lado()
quadrado.Calculo_Area()
