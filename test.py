#import logging
#import requests
#from pprint import pprint
import sqlite3
import datetime

#from telebot.db import SQL
#from telebot.models import Message
#from telebot.telegram import send_message
# from telebot.telegram import download_image
#from telebot import telegram
from telebot.telegram import get_message_creation_date

'''
Guia de resolución:

1. La funcion `register_message` en `telebot/telegram.py` cumple dos funciones en una: Registrar
un mensaje en la base de datos y mandar un mensaje de bienvenida.
Evaluar dicha funcion y separar ambas tareas.

Resuelto en las lineas 106 a 139 de telegram.py. Separando la funcion "register_message" en dos.
Una con el mismo nombre y otra llamada "respond_message"

2. Actualmente `get_updates` en `telebot/telegram.py` obtiene siempre toda la lista de novedades
desde la API de telegram, sin embargo se le puede pasar un offset para traer mensajes desde el 
ultimo lugar que se leyo. Hacer los cambios necesarios para que traiga los mensajes en base a lo 
que guardado en la base de datos.

Resuelto en las lineas 89 a 97 de telegram.py. Agregando los parametros offset y limit utilizando
una nueva funcion llamada "get_updates_id" (lineas 47 a 60 de telegram.py). Esta ultima busca en 
la base de datos los update_id de los mensajes almacenados y devuelve una lista con todos ellos
de mas antiguo a mas nuevo.

3. Que pasa si al chat se envia una imagen en vez de un texto?
Realizar los cambios necesarios para manejar dicha situacion. La imagen se puede guardar en el
filesystem o la base de datos, pero es opcional, puede descartarse.

Resuelto en las lineas 128 a 133 de telegram.py. Agregando una excepcion y llamando a una nueva
funcion llamada "download_image" (lineas 175 a 189 de telegram.py), se pudo lograr capturar la
imagen enviada y guardarla en la carpeta images.

4. El bot solamente responde un mensaje de bienvenida. Continuar la interaccion con el bot o bien
segun cual sea el mensaje de saludo dar alguna informacion determinada como el precio del dolar,
el clima, etc.

Resuelto en las lineas 146 a 205 de telegram.py. Despues de definir las funciones continuar_interaccion
y terminar_interaccion pudimos lograr que el bot contestara con diferentes temas de conversasión, aunque
algo limitados y con valores estaticos. Ademas de llamar una funcion extra en funciones.py que transforma
los strings de la base de datos en fechas para que el programa sepa cuando dar el mensaje de bienvenida.
Por lo pronto no se pudo implementar la funcion terminar_interaccion y no se llego a programar la parte
dinamica de la recaudacion de informacion del dolar y del clima.

'''


'''
class Clase():
    def __init__(self, arg):
        #codigo que se ejecuta cuando se instancia un objeto de la clase
        print(f"Estoy inicializando la clase")
        print(f"Recibi el argumento {arg}")
        self.name = arg

    def print_something(self):
        print(f"Hola {self.name}")


def test_main():
    objeto = Clase("Tomas")
    objeto.print_something()

'''
#bot_token = test
#file_id = test
#print(f"downlaod_image return: {telegram.download_image(file_id, bot_token)}")

 
# https://www.dustloop.com/wiki/images/thumb/5/5f/DBFZ_SS4Gogeta_x100BigBangKamehameha.png/800px-DBFZ_SS4Gogeta_x100BigBangKamehameha.png
# Probando imagenes

#a = "inFORmaCIon"
#b = a.lower()

#if "info" in b and (len(b) == 4 or len(b) == 11):
#    print ("Encontrado")

# Using a while loop
#from telebot.telegram import get__last_arg

#print (get__last_arg("telegram.db","message"))

#get_message_creation_date("telegram.db","message")