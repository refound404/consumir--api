from config import apikey
from model import *

#consulta de todas las monedas
allcoint = AllCointsApiIO()
allcoint.getALLCoins(apikey)

print("Total: ",len(allcoint.lista_general))
print("Criptos: ",len(allcoint.lista_criptos))
print("No criptos: ",len(allcoint.lista_no_criptos))

##############################################################################################
moneda_cripto = input("Ingrese una criptomoneda conocida ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha():
    if moneda_cripto in allcoint.lista_criptos:
        exchange = Exchange(moneda_cripto)
        try:  
            exchange.updateExchange(apikey)
        except ModelError as error:
            print(error)

        

    moneda_cripto = input("Ingrese una criptomoneda conocida ").upper()