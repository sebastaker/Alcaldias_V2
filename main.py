import sys;
from flask import jsonify;
import flask;
import sys;
import json;
import pyodbc;
import datetime;
import decimal;
import Procedimientos.select
import Procedimientos.insert
import Procedimientos.delete
import Procedimientos.update

class Conexion:
      
    # Consultar registros de cualquier tabla
    def consultar_registros(self, tabla, condiciones=None):
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()
            consulta = f"SELECT * FROM {tabla}"

            if condiciones:
                consulta += f" WHERE {condiciones}"

            cursor.execute(consulta)
            resultados = cursor.fetchall()

            # Obtener los nombres de las columnas
            columnas = [column[0] for column in cursor.description]
            registros = [dict(zip(columnas, fila)) for fila in resultados]

            print(f"Resultados obtenidos de la tabla {tabla}:")
            for registro in registros:
                print(registro)

            return registros
        except Exception as e:
            print(f"Error al consultar la tabla {tabla}: ", e)
            return None
        finally:
            cursor.close()


# Ejecución como script
if __name__ == "__main__":
    # Bloque de conexión
    conexion = Conexion()
    conexionBD = conexion.ConexionBasica()
    if conexionBD:
        # Bloque de inserción

        # Municipio
        conexion.insertar_municipio('Medellín', 2500000, 380.64, 'Daniel Quintero', datetime.date(1616, 3, 2))
        conexion.insertar_municipio("Envigado", 230000, 79.72, "Braulio Espinosa", datetime.date(1775, 8, 31))
        conexion.insertar_municipio("Bello", 600000, 149.9, "Óscar Andrés Pérez", datetime.date(1676, 12, 27))

        # Departamento
        conexion.insertar_departamento('Despacho del Alcalde', 1, 'Daniel Quintero', 'Centro de toma de decisiones y representación legal')
        conexion.insertar_departamento('Secretaría General', 1, 'Juan Pérez', 'Coordinación de actividades administrativas')
        conexion.insertar_departamento('Secretaría de Hacienda', 1, 'María González', 'Administración de los recursos financieros del municipio')

        # Alcaldes
        conexion.insertar_alcalde('Daniel', 'Quintero', 1, '2020-01-01', '2023-12-31')
        conexion.insertar_alcalde('Braulio', 'Espinosa', 2, '2020-01-01', '2023-12-31')
        conexion.insertar_alcalde('Óscar Andrés', 'Pérez', 3, '2020-01-01', '2023-12-31')

        # Proyectos
        conexion.insertar_proyecto('Construcción de Parque', 1, '2023-01-01', '2023-12-31', 50000000, 'En progreso'),
        conexion.insertar_proyecto('Mejoramiento de Vías', 2, '2023-02-01', '2023-11-30', 120000000, 'En progreso');

        # Proveedores
        conexion.insertar_proveedor('Construcciones Antioquia', 'Construcción', 'Carlos Ríos', '3012345678', 'contacto@construantioquia.com')
        conexion.insertar_proveedor('Servicios Urbanos', 'Servicios Públicos', 'Ana López', '3023456789', 'info@serviciosurbanos.com')

        # Contratos
        conexion.insertar_contrato(1, 1, 25000000, '2023-01-15', '2023-06-30', 'Completado')
        conexion.insertar_contrato(2, 2, 80000000, '2023-03-01', '2023-10-30', 'En progreso')

        # Empleados
        conexion.insertar_empleado('Juan', 'Pérez', 'Coordinador General', 1, '2019-03-15', 3000000)
        conexion.insertar_empleado('María', 'González', 'Secretaria de Hacienda', 2, '2018-06-01', 3500000)

        # Presupuesto Municipal
        conexion.insertar_presupuesto_municipal(1, 2023, 800000000, 650000000, 150000000)
        conexion.insertar_presupuesto_municipal(2, 2023, 300000000, 250000000, 50000000)

        # Programas Sociales
        conexion.insertar_programa_social('Alimentación Escolar', 1, 10000, '2023-01-01', '2023-12-31')
        conexion.insertar_programa_social('Subsidio de Transporte', 2, 5000, '2023-01-01', '2023-06-30')

        # Eventos Municipales
        conexion.insertar_evento_municipal('Feria de las Flores', 1, '2023-08-01', 'Centro de Medellín', 'Evento cultural tradicional', 'Cultural')
        conexion.insertar_evento_municipal('Festival del Rio', 2, '2023-09-15', 'Parque Principal', 'Celebración anual del río', 'Recreativo')

        # Consultas
        conexion.consultar_registros('municipios')
        conexion.consultar_registros('departamentos', "responsable = 'Juan Pérez'")
        conexion.consultar_registros('proyectos proy INNER JOIN departamentos deps ON proy.departamento_id = deps.departamento_id', "proy.estado = 'En progreso'")
        conexion.consultar_registros("presupuesto_municipal", "anio = '2023'")

        #Editar municipio
        conexion.editar_municipio(municipio_id=1, nombre='Medallo', poblacion=500000, area=100.5, alcalde_actual='Alcalde A', fecha_fundacion='1990-01-01')
        
        #Eliminar municipio
        conexion.eliminar_municipio(municipio_id=1)  

        #Consultar municipios
        conexion.consultar_municipios()
        
              

        conexion.CerrarConexion(conexionBD)