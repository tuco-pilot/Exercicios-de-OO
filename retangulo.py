"""
Classe Retangulo: Crie uma classe que modele um retangulo;

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, Calcular Área e
Calcular Perimetro;
Crie um programa que utilize essa classe. Ele deve pedir ao usuário que informe
as medidas de um local. Depois, deve criar um objeto com as medidas e calcular
a quantidade de pisos necessarios para o local.
"""

def main():

    #Área que deve ser coberta
    while True:
        area_total = float(input("Digite a medida do local que vai ser coberto com os pisos retangulares:"))
        if area_total > 0:
            break
        print("\nA área deve ser maior do que 0!")

    #Definindo o objto retangulo
    retangulo = Retangulo()

    largura = float(input("\nDigite o valor da largura do retangulo:"))
    comprimento = float(input("Digite o valor do comprimento do retangulo:"))

    while True:
        if largura <= 0:
            print("A largura deve ser maior do que zero!")
            largura = float(input("\nDigite o valor da largura do retangulo:"))
        elif comprimento <= 0:
            print(O comprimento deve ser maior do zero!")
            comprimento = float(input("\nDigite o valor do comprimento do retangulo:"))
        else:
            break
    

    retangulo.MudaValor(largura,comprimento)

    #Calculando a área de um retangulo
    area_retangulo = retangulo.CalculaArea()

    #Definindo a quantidade de pisos necessários 
    quantidade_pisos = area_total//area_retangulo
    if area_total % 1 != 0:
        quantidade_pisos += 1

    print("\nVão ser necessario %i retangulos para cobrir uma área de %.2f."%(quantidade_pisos,area_total))

class Retangulo():
    
    def __init__(self):
        self.LadoA = 0
        self.LadoB = 0

    def MudaValor(self, largura, comprimento):
        self.LadoA = largura
        self.LadoB = comprimento

    def RetornaLalor(self):
        return self.LadoA, self.LadoB

    def CalculaArea(self):
        area = self.LadoA*self.LadoB
        return area

    def CalculaPerimetro(self):
        perimetro = self.LadoA + self.LadoB
        return perimetro
        
main()        
