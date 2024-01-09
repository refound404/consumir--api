from appcoints.config import apikey
from appcoints.model import *
from appcoints.view import *


class AppCoinsController:

    def executeProgram(self):
        #consulta de todas las monedas
        allcoint = AllCointsApiIO()
        viewTools =Views()
        allcoint.getALLCoins(apikey)
       
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