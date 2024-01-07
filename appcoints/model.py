import requests


class ModelError(Exception):
    pass

class AllCointsApiIO:

    def __init__(self):
        self.url=""
        self.lista_criptos=[]
        self.lista_no_criptos =[]

    def getALLCoins(self,apikey):
        self.url=f"https://rest.coinapi.io/v1/assets/?apikey={apikey}"
        r = requests.get(self.url)
        if r.status_code != 200:
            raise Exception("Error en consulta condigo: {}".format(r.status_code))

        lista_general= r.json()
       
        for dic in lista_general:
            if dic["type_is_crypto"]==1:
                self.lista_criptos.append(dic["asset_id"] )
            else :
                self.lista_no_criptos.append(dic["asset_id"] )

class Exchange:
    def __init__(self,cripto):
       self.rate=None 
       self.moneda_cripto = cripto

    def updateExchange(self,apikey):
        url = f"https://rest.coinapi.io/v1/exchangerate/{self.moneda_cripto}/EUR?apikey={apikey}"
        r = requests.get(url)
        self.status_code = r.status_code
        respuesta =r.json()
        if r.status_code == 200:
            self.rate = respuesta ['rate'] 
        else:
            raise ModelError(f"status:{r.status_code},error:{respuesta['error']}")
        
