import pyodbc
from Clases.clases import *

class Conexion:
  # Cadena de conexión
    string_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=Administracion_Alcaldias;
        PORT=3306;
        user=sebas_python;
        password=Sebas5279"""

    # Insertar un municipio 
    def insertar_municipio(self, nombre, poblacion, area, alcalde_actual, fecha_fundacion) -> None:
        if not nombre or not poblacion or not area or not alcalde_actual or not fecha_fundacion:
            print("Error: Todos los campos deben estar diligenciados")
            return
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()
            if isinstance(fecha_fundacion, datetime.date):
                fecha_fundacion = fecha_fundacion.strftime('%Y-%m-%d')

            # Llamada al procedimiento almacenado
            consulta = f"CALL proc_InsertMunicipio('{nombre}', {poblacion}, {area}, '{alcalde_actual}', '{fecha_fundacion}')"
            cursor.execute(consulta)
            conexion.commit()
            print("Municipio insertado exitosamente.")
        except Exception as e:
            print("Error al insertar municipio: ", e)
        finally:
            cursor.close()
            conexion.close()

    # Insertar un departamento 
    def insertar_departamento(self, nombre, municipio_id, responsable, funcion)-> None:
        if not nombre or not municipio_id or not responsable or not funcion:
            print("Error: Todos los campos deben estar diligenciados")
            return
        
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()

            # Llamada al procedimiento almacenado
            consulta = f"CALL proc_InsertDepartamento('{nombre}', {municipio_id}, '{responsable}', '{funcion}')"
            cursor.execute(consulta)
            conexion.commit()
            print("Departamento insertado exitosamente.")
        except Exception as e:
            print("Error al insertar departamento: ", e)
        finally:
            cursor.close()
            conexion.close()

    # Insertar un alcalde 
    def insertar_alcalde(self, nombre, apellido, municipio_id, fecha_inicio_mandato, fecha_fin_mandato)-> None:
        if not nombre or not municipio_id or not apellido or not fecha_inicio_mandato or not fecha_fin_mandato:
            print("Error: Todos los campos deben estar diligenciados")
            return
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()

            # Convertir fechas a formato string si son del tipo datetime.date
            if isinstance(fecha_inicio_mandato, datetime.date):
                fecha_inicio_mandato = fecha_inicio_mandato.strftime('%Y-%m-%d')
                fecha_fin_mandato = fecha_fin_mandato.strftime('%Y-%m-%d')

            # Llamada al procedimiento almacenado
            consulta = f"CALL proc_InsertAlcalde('{nombre}', '{apellido}', {municipio_id}, '{fecha_inicio_mandato}', '{fecha_fin_mandato}')"
            cursor.execute(consulta)
            conexion.commit()
            print("Alcalde insertado exitosamente.")
        except Exception as e:
            print("Error al insertar alcalde: ", e)
        finally:
            cursor.close()
            conexion.close()

    # Insertar un proyecto 
    def insertar_proyecto(self, nombre, departamento_id, fecha_inicio, fecha_fin, presupuesto, estado)-> None:
        if not nombre or not departamento_id or not presupuesto or not fecha_inicio or not fecha_fin or not estado:
            print("Error: Todos los campos deben estar diligenciados")
            return
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()

            # Convertir fechas a formato string si son del tipo datetime.date
            if isinstance(fecha_inicio, datetime.date):
                fecha_inicio = fecha_inicio.strftime('%Y-%m-%d')
                fecha_fin = fecha_fin.strftime('%Y-%m-%d')

            # Llamada al procedimiento almacenado
            consulta = f"CALL proc_InsertProyecto('{nombre}', {departamento_id}, '{fecha_inicio}', '{fecha_fin}', {presupuesto}, '{estado}')"
            cursor.execute(consulta)
            conexion.commit()
            print("Proyecto insertado exitosamente.")
        except Exception as e:
            print("Error al insertar proyecto: ", e)
        finally:
            cursor.close()
            conexion.close()

    # Insertar un proveedor 
    def insertar_proveedor(self, nombre, tipo, contacto, telefono, correo)-> None:
        if not nombre or not tipo or not contacto or not telefono or not correo:
            print("Error: Todos los campos deben estar diligenciados")
            return
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()

            # Llamada al procedimiento almacenado
            consulta = f"CALL proc_InsertProveedor('{nombre}', '{tipo}', '{contacto}', '{telefono}', '{correo}')"
            cursor.execute(consulta)
            conexion.commit()
            print("Proveedor insertado exitosamente.")
        except Exception as e:
            print("Error al insertar proveedor: ", e)
        finally:
            cursor.close()
            conexion.close()

    # Insertar un contrato 
    def insertar_contrato(self, proyecto_id, proveedor_id, monto, fecha_firma, fecha_termino, estado)-> None:
        if not proyecto_id or not proveedor_id or not monto or not fecha_firma or not fecha_termino or not estado:
            print("Error: Todos los campos deben estar diligenciados")
            return
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()

            # Convertir fechas a formato string si son del tipo datetime.date
            if isinstance(fecha_firma, datetime.date):
                fecha_firma = fecha_firma.strftime('%Y-%m-%d')
                fecha_termino = fecha_termino.strftime('%Y-%m-%d')

            # Llamada al procedimiento almacenado
            consulta = f"CALL proc_InsertContrato({proyecto_id}, {proveedor_id}, {monto}, '{fecha_firma}', '{fecha_termino}', '{estado}')"
            cursor.execute(consulta)
            conexion.commit()
            print("Contrato insertado exitosamente.")
        except Exception as e:
            print("Error al insertar contrato: ", e)
        finally:
            cursor.close()
            conexion.close()

    # Insertar un empleado 
    def insertar_empleado(self, nombre, apellido, cargo, departamento_id, fecha_ingreso, salario)-> None:
        if not nombre or not apellido or not cargo or not departamento_id or not fecha_ingreso or not salario:
            print("Error: Todos los campos deben estar diligenciados")
            return
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()

            # Convertir fecha a formato string si es del tipo datetime.date
            if isinstance(fecha_ingreso, datetime.date):
                fecha_ingreso = fecha_ingreso.strftime('%Y-%m-%d')

            # Llamada al procedimiento almacenado
            consulta = f"CALL proc_InsertEmpleado('{nombre}', '{apellido}', '{cargo}', {departamento_id}, '{fecha_ingreso}', {salario})"
            cursor.execute(consulta)
            conexion.commit()
            print("Empleado insertado exitosamente.")
        except Exception as e:
            print("Error al insertar empleado: ", e)
        finally:
            cursor.close()
            conexion.close()

    # Insertar un presupuesto 
    def insertar_presupuesto_municipal(self, municipio_id, anio, ingresos, egresos, saldo)-> None:
        if not municipio_id or not anio or not ingresos or not egresos or not saldo:
            print("Error: Todos los campos deben estar diligenciados")
            return
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()

            # Llamada al procedimiento almacenado
            consulta = f"CALL proc_InsertPresupuestoMunicipal({municipio_id}, {anio}, {ingresos}, {egresos}, {saldo})"
            cursor.execute(consulta)
            conexion.commit()
            print("Presupuesto municipal insertado exitosamente.")
        except Exception as e:
            print("Error al insertar presupuesto municipal: ", e)
        finally:
            cursor.close()
            conexion.close()

    # Insertar un programa social 
    def insertar_programa_social(self, nombre, departamento_id, beneficiarios, fecha_inicio, fecha_fin)-> None:
        if not nombre or not departamento_id or not beneficiarios or not fecha_inicio or not fecha_fin:
            print("Error: Todos los campos deben estar diligenciados")
            return
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()

            # Convertir fechas a formato string si son del tipo datetime.date
            if isinstance(fecha_inicio, datetime.date):
                fecha_inicio = fecha_inicio.strftime('%Y-%m-%d')
                fecha_fin = fecha_fin.strftime('%Y-%m-%d')

            # Llamada al procedimiento almacenado
            consulta = f"CALL proc_InsertProgramaSocial('{nombre}', {departamento_id}, {beneficiarios}, '{fecha_inicio}', '{fecha_fin}')"
            cursor.execute(consulta)
            conexion.commit()
            print("Programa social insertado exitosamente.")
        except Exception as e:
            print("Error al insertar programa social: ", e)
        finally:
            cursor.close()
            conexion.close()

    # Insertar un evento municipal 
    def insertar_evento_municipal(self, nombre, municipio_id, fecha, ubicacion, descripcion, tipo)-> None:
        if not nombre or not municipio_id or not fecha or not ubicacion or not descripcion or not tipo:
            print("Error: Todos los campos deben estar diligenciados")
            return
        try:
            conexion = pyodbc.connect(self.string_conexion)
            cursor = conexion.cursor()

            # Convertir fecha a formato string si es del tipo datetime.date
            if isinstance(fecha, datetime.date):
                fecha = fecha.strftime('%Y-%m-%d')

            # Llamada al procedimiento almacenado
            consulta = f"CALL proc_InsertEventoMunicipal('{nombre}', {municipio_id}, '{fecha}', '{ubicacion}', '{descripcion}', '{tipo}')"
            cursor.execute(consulta)
            conexion.commit()
            print("Evento municipal insertado exitosamente.")
        except Exception as e:
            print("Error al insertar evento municipal: ", e)
        finally:
            cursor.close()
            conexion.close()
