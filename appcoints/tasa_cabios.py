import requests

moneda_cripto = input("Ingrese una criptomoneda conocida ").upper()
apikey= "68406179-6C37-44CD-B433-7E891D8C2722"


while moneda_cripto != "" and moneda_cripto.isalpha():
    #invocando al metodo get conn la url especifica
    url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}"
    r = requests.get(url)

    #ejercicio 1 como capturamos el rate
    respuesta =r.json()#obtener la respuesta en formato diccionario

    #ejercicio 2 capturar errores de peticion http
    if r.status_code == 200:
        print("rate: ",respuesta['rate'])

    else:
        print("error:",respuesta['error'])


    moneda_cripto = input("Ingrese una criptomoneda conocida").upper()