class Views:
    def insterCoin(self):
        moneda_cripto = input("Ingrese una moneda conocida ").upper()
        return moneda_cripto
    
    def viewListCoins(self,allcoint):
        print(f"Total: ,{len(allcoint.lista_general)}\nCriptos: {len(allcoint.lista_criptos)}\nNo criptos: {len(allcoint.lista_no_criptos)}")

    def viewRateExchange(self,change ):
         print(f"fecha de consulta: {change.time}" + "\n{:.2f}€".format( change.rate))

    def viewRateExchange(self,change ):
        print(f"fecha de consulta: {change.time}\n{change.rate}")

    def getError(self,er):
        print(er)
