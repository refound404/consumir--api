class Views:
    def insterCoin(self):
        moneda_cripto = input("Ingrese una criptomoneda conocida ").upper()
        return moneda_cripto
    
    def viewListCoins(self,allcoint):
        print("Total: ",len(allcoint.lista_general))
        print("Criptos: ",len(allcoint.lista_criptos))
        print("No criptos: ",len(allcoint.lista_no_criptos))

    def viewRateExchange(sel,change ):
         print( "{:.2f}€".format( change.rate))

    def getError(self,er):
        print(er)