lista = list()
lista.append("banana")


cartaidentitaEdo = {
"Nome" : "Edoardo",
"cognome" : "albanese",
"codice fiscale": "LBNDR0925FEN9R"
}

cartaidentitaDavide = {
"Nome" : "Davide",
"cognome" : "Xiao",
"età": 17,
"codice fiscale": "feojifejaewip",
"cibo preferito": "carne"
}

carteidentita = [cartaidentitaEdo, cartaidentitaDavide]

cartaidentitaEdo.update({"Età": 16})
cartaidentitaEdo.update({"Comune di nascità": "Napoli"})
cartaidentitaDavide.pop("cibo preferito")

for i in carteidentita:
    print("Carta identità n.", carteidentita.index(i) + 1)
    for element in i:
        print(str(element), i[element])


