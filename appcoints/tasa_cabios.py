import requests
from config import apikey

moneda_cripto = input("Ingrese una criptomoneda conocida ").upper()


while moneda_cripto != "" and moneda_cripto.isalpha():
    #invocando al metodo get conn la url especifica
    url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}"
    r = requests.get(url)

    #ejercicio 1 como capturamos el rate
    respuesta =r.json()#obtener la respuesta en formato diccionario

    #ejercicio 2 capturar errores de peticion http
    if r.status_code == 200:
        #print("rate: ",respuesta['rate'])
        print( "{:.2f}€".format( respuesta ['rate'] ) )
        break

    else:
        print("error:",respuesta['error'])


    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()