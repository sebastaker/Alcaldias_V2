import pyodbc
import pymysql
from Clases.clases import *
from Clases.Conexion import Conexion


class Update:
    #Metodo para actualizar municipio
    def actualizar_municipio(self, municipio_id: int, nombre: str, poblacion: int, area: float, alcalde_actual: str, fecha_fundacion: str) -> None:
        consulta = "CALL proc_EditMunicipio(%s, %s, %s, %s, %s, %s)"
        print(f"Ejecutando consulta: {consulta} con parámetros: {municipio_id}, {nombre}, {poblacion}, {area}, {alcalde_actual}, {fecha_fundacion}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()            
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar los parámetros
            cursor.execute(consulta, (municipio_id, nombre, poblacion, area, alcalde_actual, fecha_fundacion))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Municipio con ID {municipio_id} actualizado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    #Metodo para actualizar Departamento
    def actualizar_departamento(self, departamento_id: int, nombre: str, municipio_id: int, responsable: str, funcion: str) -> None:
        consulta = "CALL proc_UpdateDepartamento(%s, %s, %s, %s, %s)"
        print(f"Ejecutando consulta: {consulta} con parámetros: {departamento_id}, {nombre}, {municipio_id}, {responsable}, {funcion}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar los parámetros
            cursor.execute(consulta, (departamento_id, nombre, municipio_id, responsable, funcion))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Departamento con ID {departamento_id} actualizado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    #Metodo para actualizar Alcalde
    def actualizar_alcalde(self, alcalde_id: int, nombre: str, apellido: str, municipio_id: int, fecha_inicio_mandato: str, fecha_fin_mandato: str) -> None:
        consulta = "CALL proc_UpdateAlcalde(%s, %s, %s, %s, %s, %s)"
        print(f"Ejecutando consulta: {consulta} con parámetros: {alcalde_id}, {nombre}, {apellido}, {municipio_id}, {fecha_inicio_mandato}, {fecha_fin_mandato}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar los parámetros
            cursor.execute(consulta, (alcalde_id, nombre, apellido, municipio_id, fecha_inicio_mandato, fecha_fin_mandato))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Alcalde con ID {alcalde_id} actualizado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    #Metodo para actualizar Proyecto
    def actualizar_proyecto(self, proyecto_id: int, nombre: str, departamento_id: int, fecha_inicio: str, fecha_fin: str, presupuesto: float, estado: str) -> None:
        consulta = "CALL proc_UpdateProyecto(%s, %s, %s, %s, %s, %s, %s)"
        print(f"Ejecutando consulta: {consulta} con parámetros: {proyecto_id}, {nombre}, {departamento_id}, {fecha_inicio}, {fecha_fin}, {presupuesto}, {estado}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar los parámetros
            cursor.execute(consulta, (proyecto_id, nombre, departamento_id, fecha_inicio, fecha_fin, presupuesto, estado))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Proyecto con ID {proyecto_id} actualizado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    #Metodo para actualizar proveedor
    def actualizar_proveedor(self, proveedor_id: int, nombre: str, tipo: str, contacto: str, telefono: str, correo: str) -> None:
        consulta = "CALL proc_UpdateProveedor(%s, %s, %s, %s, %s, %s)"
        print(f"Ejecutando consulta: {consulta} con parámetros: {proveedor_id}, {nombre}, {tipo}, {contacto}, {telefono}, {correo}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar los parámetros
            cursor.execute(consulta, (proveedor_id, nombre, tipo, contacto, telefono, correo))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Proveedor con ID {proveedor_id} actualizado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")


    #Metodo para actualizar Contrato
    def actualizar_contrato(self, contrato_id: int, proyecto_id: int, proveedor_id: int, monto: float, fecha_firma: str, fecha_termino: str, estado: str) -> None:
        consulta = "CALL proc_UpdateContrato(%s, %s, %s, %s, %s, %s, %s)"
        print(f"Ejecutando consulta: {consulta} con parámetros: {contrato_id}, {proyecto_id}, {proveedor_id}, {monto}, {fecha_firma}, {fecha_termino}, {estado}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar los parámetros
            cursor.execute(consulta, (contrato_id, proyecto_id, proveedor_id, monto, fecha_firma, fecha_termino, estado))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Contrato con ID {contrato_id} actualizado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    #Metodo para actualizar Empleado
    def actualizar_empleado(self, empleado_id: int, nombre: str, apellido: str, cargo: str, departamento_id: int, fecha_ingreso: str, salario: float) -> None:
        consulta = "CALL proc_UpdateEmpleado(%s, %s, %s, %s, %s, %s, %s)"
        print(f"Ejecutando consulta: {consulta} con parámetros: {empleado_id}, {nombre}, {apellido}, {cargo}, {departamento_id}, {fecha_ingreso}, {salario}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar los parámetros
            cursor.execute(consulta, (empleado_id, nombre, apellido, cargo, departamento_id, fecha_ingreso, salario))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Empleado con ID {empleado_id} actualizado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    #Metodo para actualizar Evento Municipal
    def actualizar_evento_municipal(self, evento_id: int, nombre: str, municipio_id: int, fecha: str, ubicacion: str, descripcion: str, tipo: str) -> None:
        consulta = "CALL proc_UpdateEventoMunicipal(%s, %s, %s, %s, %s, %s, %s)"
        print(f"Ejecutando consulta: {consulta} con parámetros: {evento_id}, {nombre}, {municipio_id}, {fecha}, {ubicacion}, {descripcion}, {tipo}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar los parámetros
            cursor.execute(consulta, (evento_id, nombre, municipio_id, fecha, ubicacion, descripcion, tipo))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Evento Municipal con ID {evento_id} actualizado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    #Metodo para actualizar Presupuesto Municipal
    def actualizar_presupuesto_municipal(self, presupuesto_id: int, municipio_id: int, anio: int, ingresos: float, egresos: float, saldo: float) -> None:
        consulta = "CALL proc_UpdatePresupuestoMunicipal(%s, %s, %s, %s, %s, %s)"
        print(f"Ejecutando consulta: {consulta} con parámetros: {presupuesto_id}, {municipio_id}, {anio}, {ingresos}, {egresos}, {saldo}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar los parámetros
            cursor.execute(consulta, (presupuesto_id, municipio_id, anio, ingresos, egresos, saldo))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Presupuesto Municipal con ID {presupuesto_id} actualizado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    #Metodo para actualizar Programa Social
    def actualizar_programa_social(self, programa_id: int, nombre: str, departamento_id: int, beneficiarios: int, fecha_inicio: str, fecha_fin: str) -> None:
        consulta = "CALL proc_UpdateProgramaSocial(%s, %s, %s, %s, %s, %s)"
        print(f"Ejecutando consulta: {consulta} con parámetros: {programa_id}, {nombre}, {departamento_id}, {beneficiarios}, {fecha_inicio}, {fecha_fin}")

        try:
            conexion = Conexion()
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar el procedimiento almacenado y pasar los parámetros
            cursor.execute(consulta, (programa_id, nombre, departamento_id, beneficiarios, fecha_inicio, fecha_fin))

            conexion.commit()  # Confirmar los cambios realizados
            cursor.close()
            conexion.close()

            print(f"Programa Social con ID {programa_id} actualizado exitosamente.")
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")







