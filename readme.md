# Aplicacion de consulta de valor actual de criptomonedas

programa hecho en python para recuerar el valor en euros de una criptomoneda 
desde www.coinapi.io

## Instalacion
-obtener una apikaey en www.coinapi.io
-Renombrar el fichero config_template.py a config.py
-Agregar dentro de config.py el api key de esta manera:


```
APIKEY= "AQUI VA SU APIKEY"
```

## Instalacion de dependencias

-crear un entorno virtual de python
```
py -m venv entorno

```

-Activar el entorno e instalar los requerimientos
```
-.\entorno\SCripts\activate
pip install -r requirements.txt


```
-utiliza las librerias de pytest y requests
