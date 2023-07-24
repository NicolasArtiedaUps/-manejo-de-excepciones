# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:49:21 2023

@author: lab
"""

class errorRegistro(Exception):
    pass

class Modelo:
    lista=[]
    def verficarDato(self,valor):
        if valor in self.lista:
            print("sensor ya registrado")
        else:
            self.lista.append(valor)
            print( "nuevo sensor registrado")
    
        
class Controlador:
    def __init__(self,modelo,vista):
        self.vista=vista
        self.modelo=modelo
    def obtener_Dato_vista(self,valor):
        # print("",valor) 
        self.modelo.verficarDato(valor)
        

class Vista:
    def EntradaSensor(self):
        sensor=input("ingrese el nombre del sensor ")
        return sensor


vista=Vista()
modelo=Modelo()
controlador=Controlador(modelo,vista)

while True:
    print("1. registrar sensor ")
    print("2. salir")
    op=int(input("elija la opcion "))
    if op==1:
       x=vista.EntradaSensor()
       controlador.obtener_Dato_vista(x) 
    elif op==2:
        break