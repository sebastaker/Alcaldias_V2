import sys;
from flask import jsonify;
import flask;
import sys;
import json;
import pyodbc;
import datetime;
import decimal;
from Clases.clases import *
from Clases.Conexion import *
import Procedimientos.select as select
import Procedimientos.insert as insert
import Procedimientos.delete as delete
import Procedimientos.update as update

class Principal:

    def __init__(self):
        # Inicializamos la conexión solo una vez
        self.conexion = Conexion()   
        self.conexion.verificar_conexion()   # Verificar la conexión 1  

        self.conexion2 = Conexion2()
        self.conexion2.verificar_conexion()  # Verificar la conexión 2
        
      
if __name__ == "__main__":    
    
    # Consultas
    conexion = select.Select()
    conexion.consultar_municipio(municipio_id = 1)
        
    
    #Editar municipio
    conexion = update.Update()
    conexion.actualizar_municipio(municipio_id=1, nombre='Medellín', poblacion=500000, area=100.5, alcalde_actual='Federico Gutierrez', fecha_fundacion='1990-01-01')
    conexion = select.Select()
    conexion.consultar_municipio(municipio_id = 1)
    #Eliminar municipio
    #conexion.eliminar_municipio(municipio_id=1)  

principal = Principal()