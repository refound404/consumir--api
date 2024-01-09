from appcoints.model import AllCointsApiIO,Exchange,ModelError
from appcoints.config import apikey
import pytest

def test_allcoint():
    lista_total =AllCointsApiIO()
    lista_total.getALLCoins(apikey)
    assert lista_total != None
    cantidad = len(lista_total.lista_criptos) + len(lista_total.lista_no_criptos)
    assert cantidad == 18549#true

def test_exchange():
    cambio = Exchange("ETH")
    cambio.updateExchange(apikey)
    assert cambio.rate>0
    assert cambio.rate != None


def test_exchange_error():
    cambio = Exchange("ÑÑÑ")
    

    with pytest.raises(ModelError) as exceptionInfo:
        cambio.updateExchange(apikey)
    assert str(exceptionInfo.value)== f"status:{cambio.status_code}, error: You requested specific single item that we don't have at this moment."
   