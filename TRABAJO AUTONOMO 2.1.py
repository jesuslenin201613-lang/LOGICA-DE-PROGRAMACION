import random #Importamos la palabra reservada RANDOM para generar valores aleatroios
def generar_contraseña(longitud):#Se define una funcion GENERAR_CONTRASEÑA con el parametro LONGITUD que indicara cuantos caracteres tendra la contraseña
    caracteres = "abcdefghijklmnñopqrstvwxyzABCDEFGHIJKLMNÑOPQRSTVWXYZ0123456789#$&*!"# Crea una variable CARACTERES que contiene numeros, letras y simbolos
    contraseña = "" #Crea una variable vacia con el fin de ir agregando los caracteres aleatorios
    for i in range (longitud):#Ciclo FOR en el cual se repetira tantas veces como indique la variable LONGITUD
        contraseña += random.choice(caracteres) # Selecciona aleatoriamente en la cadena de CARACTERES y += para agregar un caracter al final en cada repeticion
    return contraseña # Devuelve la contraseña generada
