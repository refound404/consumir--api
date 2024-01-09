from config import apikey
from model import *
from view import *

#consulta de todas las monedas
allcoint = AllCointsApiIO()
allcoint.getALLCoins(apikey)
viewTools =Views()

viewTools.viewListCoins(allcoint=allcoint)
##############################################################################################
moneda_cripto = viewTools.insterCoin()

while moneda_cripto != "" and moneda_cripto.isalpha():
    if moneda_cripto in allcoint.lista_criptos:
        exchange = Exchange(moneda_cripto)
        try:  
            exchange.updateExchange(apikey)
            viewTools.viewRateExchange(exchange)
        except ModelError as error:
            viewTools.getError(error)
        
    moneda_cripto = viewTools.insterCoin()