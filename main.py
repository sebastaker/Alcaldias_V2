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
        
    
    #Ediciones
    conexion = update.Update()
    conexion.actualizar_municipio(municipio_id=1, nombre='Medellín', poblacion=500000, area=100.5, alcalde_actual='Federico Gutierrez', fecha_fundacion='1990-01-01')
    conexion = select.Select()
    conexion.consultar_municipio(municipio_id = 1)

    # Inserciones
    conexion = insert.Insert()
    # #Municipio
    conexion.insertar_municipio('Girardota', 2500000, 380.64, 'Daniel Quintero', datetime.date(1616, 3, 2))
    #conexion.insertar_municipio("Envigado", 230000, 79.72, "Braulio Espinosa", datetime.date(1775, 8, 31))
    #conexion.insertar_municipio("Barbosa", 600000, 149.9, "Rambo III", datetime.date(1676, 12, 27))
    conexion = select.Select()
    #conexion.consultar_municipio(municipio_id = 4)
    #conexion.consultar_municipio(municipio_id = 5)
    conexion.consultar_municipio(municipio_id = 7)
    # Departamento
    # conexion.insertar_departamento('Despacho del Alcalde', 1, 'Daniel Quintero', 'Centro de toma de decisiones y representación legal')
    # conexion.insertar_departamento('Secretaría General', 1, 'Juan Pérez', 'Coordinación de actividades administrativas')
    # conexion.insertar_departamento('Secretaría de Hacienda', 1, 'María González', 'Administración de los recursos financieros del municipio')
    # # Alcaldes
    # conexion.insertar_alcalde('Daniel', 'Quintero', 1, '2020-01-01', '2023-12-31')
    # conexion.insertar_alcalde('Braulio', 'Espinosa', 2, '2020-01-01', '2023-12-31')
    # conexion.insertar_alcalde('Óscar Andrés', 'Pérez', 3, '2020-01-01', '2023-12-31')
    # # Proyectos
    # conexion.insertar_proyecto('Construcción de Parque', 1, '2023-01-01', '2023-12-31', 50000000, 'En progreso'),
    # conexion.insertar_proyecto('Mejoramiento de Vías', 2, '2023-02-01', '2023-11-30', 120000000, 'En progreso');
    # # Proveedores
    # conexion.insertar_proveedor('Construcciones Antioquia', 'Construcción', 'Carlos Ríos', '3012345678', 'contacto@construantioquia.com')
    # conexion.insertar_proveedor('Servicios Urbanos', 'Servicios Públicos', 'Ana López', '3023456789', 'info@serviciosurbanos.com')
    # # Contratos
    # conexion.insertar_contrato(1, 1, 25000000, '2023-01-15', '2023-06-30', 'Completado')
    # conexion.insertar_contrato(2, 2, 80000000, '2023-03-01', '2023-10-30', 'En progreso')
    # # Empleados
    # conexion.insertar_empleado('Juan', 'Pérez', 'Coordinador General', 1, '2019-03-15', 3000000)
    # conexion.insertar_empleado('María', 'González', 'Secretaria de Hacienda', 2, '2018-06-01', 3500000)
    # # Presupuesto Municipal
    # conexion.insertar_presupuesto_municipal(1, 2023, 800000000, 650000000, 150000000)
    # conexion.insertar_presupuesto_municipal(2, 2023, 300000000, 250000000, 50000000)
    # # Programas Sociales
    # conexion.insertar_programa_social('Alimentación Escolar', 1, 10000, '2023-01-01', '2023-12-31')
    # conexion.insertar_programa_social('Subsidio de Transporte', 2, 5000, '2023-01-01', '2023-06-30')
    # # Eventos Municipales
    # conexion.insertar_evento_municipal('Feria de las Flores', 1, '2023-08-01', 'Centro de Medellín', 'Evento cultural tradicional', 'Cultural')
    # conexion.insertar_evento_municipal('Festival del Rio', 2, '2023-09-15', 'Parque Principal', 'Celebración anual del río', 'Recreativo')

    #Eliminaciones
    conexion = delete.Delete()
    conexion.eliminar_municipio(municipio_id=7)
    conexion = select.Select()
    conexion.consultar_municipio(municipio_id = 7)

principal = Principal()