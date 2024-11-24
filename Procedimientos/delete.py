import pyodbc
import pymysql
from Clases.clases import *
from Clases.Conexion import Conexion

class Delete:
    #Metodo para eliminar Municipio
    def eliminar_municipio(self, municipio_id: int) -> None:
        consulta = "CALL proc_DeleteMunicipio(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {municipio_id}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar el parámetro
            cursor.execute(consulta, (municipio_id,))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Municipio con ID {municipio_id} eliminado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")
    
    # Método para eliminar departamento
    def eliminar_departamento(self, departamento_id: int) -> None:
        consulta = "CALL proc_DeleteDepartamento(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {departamento_id}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            cursor.execute(consulta, (departamento_id,))

            conexion.commit()
            cursor.close()
            conexion.close()

            print(f"Departamento con ID {departamento_id} eliminado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    # Método para eliminar alcalde
    def eliminar_alcalde(self, alcalde_id: int) -> None:
        consulta = "CALL proc_DeleteAlcalde(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {alcalde_id}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            cursor.execute(consulta, (alcalde_id,))

            conexion.commit()
            cursor.close()
            conexion.close()

            print(f"Alcalde con ID {alcalde_id} eliminado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    # Método para eliminar proyecto
    def eliminar_proyecto(self, proyecto_id: int) -> None:
        consulta = "CALL proc_DeleteProyecto(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {proyecto_id}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            cursor.execute(consulta, (proyecto_id,))

            conexion.commit()
            cursor.close()
            conexion.close()

            print(f"Proyecto con ID {proyecto_id} eliminado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    # Método para eliminar proveedor
    def eliminar_proveedor(self, proveedor_id: int) -> None:
        consulta = "CALL proc_DeleteProveedor(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {proveedor_id}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            cursor.execute(consulta, (proveedor_id,))

            conexion.commit()
            cursor.close()
            conexion.close()

            print(f"Proveedor con ID {proveedor_id} eliminado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    # Método para eliminar contrato
    def eliminar_contrato(self, contrato_id: int) -> None:
        consulta = "CALL proc_DeleteContrato(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {contrato_id}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            cursor.execute(consulta, (contrato_id,))

            conexion.commit()
            cursor.close()
            conexion.close()

            print(f"Contrato con ID {contrato_id} eliminado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    # Método para eliminar empleado
    def eliminar_empleado(self, empleado_id: int) -> None:
        consulta = "CALL proc_DeleteEmpleado(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {empleado_id}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            cursor.execute(consulta, (empleado_id,))

            conexion.commit()
            cursor.close()
            conexion.close()

            print(f"Empleado con ID {empleado_id} eliminado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    # Método para eliminar evento municipal
    def eliminar_evento_municipal(self, evento_id: int) -> None:
        consulta = "CALL proc_DeleteEventoMunicipal(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {evento_id}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            cursor.execute(consulta, (evento_id,))

            conexion.commit()
            cursor.close()
            conexion.close()

            print(f"Evento Municipal con ID {evento_id} eliminado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    # Método para eliminar presupuesto municipal
    def eliminar_presupuesto_municipal(self, presupuesto_id: int) -> None:
        consulta = "CALL proc_DeletePresupuestoMunicipal(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {presupuesto_id}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            cursor.execute(consulta, (presupuesto_id,))

            conexion.commit()
            cursor.close()
            conexion.close()

            print(f"Presupuesto Municipal con ID {presupuesto_id} eliminado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    # Método para eliminar programa social
    def eliminar_programa_social(self, programa_id: int) -> None:
        consulta = "CALL proc_DeleteProgramaSocial(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {programa_id}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            cursor.execute(consulta, (programa_id,))

            conexion.commit()
            cursor.close()
            conexion.close()

            print(f"Programa Social con ID {programa_id} eliminado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")