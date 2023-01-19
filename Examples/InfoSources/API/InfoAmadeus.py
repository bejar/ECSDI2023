"""
.. module:: InfoAmadeus

InfoAmadeus
******

:Description: InfoAmadeus

    Consulta a Amadeus mediante la libreria amadeus

https://github.com/amadeus4dev/amadeus-python

Demo que hace una consulta simple a Amadeus de un vuelo Barcelona a Paris, hoteles en Londres y Actividades en Barcelona
Consultar la web de la libreria para mas tipos de queries e informacion

Para usarla hay que darse de alta en el site de desarrolladores de Amadeus y crear una API para obtener una Key de acceso
https://developers.amadeus.com/

Se ha de crear un fichero python APIKeys.py que contenga la información para el
acceso a Amadeis (AMADEUS_KEY, AMADEUS_SECRET)

:Authors:
    bejar

:Version: 

:Date:  02/02/2021
"""
from amadeus import Client, ResponseError
from AgentUtil.APIKeys import AMADEUS_KEY, AMADEUS_SECRET
from pprint import PrettyPrinter

__author__ = 'bejar'

amadeus = Client(
    client_id=AMADEUS_KEY,
    client_secret=AMADEUS_SECRET
)
ppr = PrettyPrinter(indent=4)

# Flights query
try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='BCN',
        destinationLocationCode='PAR',
        departureDate='2021-06-01',
        adults=1)
    print("FLIGHTS")
    print("-----------------------------------")
    ppr.pprint(response.data)
except ResponseError as error:
    print(error)

# Hotels query
try:
    response = amadeus.shopping.hotel_offers.get(cityCode='LON')
    print("-----------------------------------")
    print("HOTELS")
    print("-----------------------------------")
    for h in response.data:
        ppr.pprint(h['hotel']['name'])
    print('---')
    # Siguientes paginas de resultados
    response = amadeus.next(response)
    for h in response.data:
        ppr.pprint(h['hotel']['name'])
    print('---')
    response = amadeus.next(response)
    for h in response.data:
        ppr.pprint(h['hotel']['name'])

except ResponseError as error:
    print(error)


# Activities query
try:
    response = amadeus.shopping.activities.by_square.get(north=41.397158, west=2.160873,
                                          south=41.394582, east=2.177181)
    print("ACTIVITIES")
    print("-----------------------------------")
    ppr.pprint(response.data)
except ResponseError as error:
    print(error)
