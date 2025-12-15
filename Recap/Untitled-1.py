'''
Python3
Programmazione ad oggetti
'''

class auto:

    # Attributi di Classe
    garanzia = 1
    assicurazione = True
    parcoAuto = 0

    #Metodo costruttore
    def __init__(self,proprietario, marca, modello, cilidrata, cavalli, colore, bellezza):

        # Attributi di Istanza
        self.proprietario = proprietario
        self.marca = marca
        self.modello = modello
        self.cilindrata = cilidrata
        self.cavalli = cavalli
        self.colore = colore
        self.bellezza = bellezza
        
        auto.parcoAuto +=1

    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n Marca: {self.marca}\n Modello: {self.modello}\n Cilindrata: {self.cilindrata}\n Cavalli: {self.cavalli}\n colore: {self.colore}\n assicurazione: {self.assicurazione}\n bellezza: {self.bellezza}' 


# inizia il programma chiamante

if __name__ == "__main__":

    giovanni = auto("giovanni","ford","fiesta",1500, 160, "rosso", "brutta")
    marco = auto("marco","fiat","Bravo", 2500, 200, "verde", "meh...")
    pippo = auto("marco","jeep","classe G", 2800, 300, "blu", "carina")
    frank = auto("frank", "nissan", "skyline", 3000, 500, "nero", "stupenda!")


    print("Il tipo di variabile costruita è:")
    print(giovanni)
    print(marco)
    print(frank)

    print("\nLa singola scheda è:")
    print (giovanni.scheda())
    print (marco.scheda())
    print (frank.scheda())
    print("\nauto totali: ",auto.parcoAuto)

    print("\n\naltro metodo per visualizzare le informazioni (__dict__):")

    print(giovanni.__dict__)
    print(marco.__str__)
    print(frank.__dict__)

    print(dir(giovanni))
    print(dir(frank))
