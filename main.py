import sys;
import jsonify;
import flask;
import sys;
import json;
import pyodbc;
import datetime;
import decimal;

# Prueba de funcionalidad del proyecto
print( "¡Hola Mundo!" );
app = flask.Flask(__name__);
print(__name__);

class Conexion:
  # Cadena de conexión
    string_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=Administracion_Alcaldias;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!"""

    # Conexión a base de datos
    def ConexionBasica(self) -> None:
        try:
            conexion = pyodbc.connect(self.string_conexion)
            print("Conexión exitosa a la base de datos.")
            # Devuelver conexión establecida
            return conexion
        except pyodbc.Error as e:
            # Captura errores de conexión
            print("Error al conectar con la base de datos: ", e)
            return None

    # Cerrar la conexión a la base de datos
    def CerrarConexion(self, conexion):
        try:
            conexion.close()
            print("Conexión cerrada correctamente.")
        except pyodbc.Error as e:
            # Captura errores al cerrar la conexión
            print("Error al cerrar la conexión:", e)

    # Insertar un municipio en la base de datos usando un procedimiento almacenado
    def insertar_municipio(self, nombre, poblacion, area, alcalde_actual, fecha_fundacion):
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

    # Insertar un departamento en la base de datos usando un procedimiento almacenado
    def insertar_departamento(self, nombre, municipio_id, responsable, funcion):
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

    # Insertar un alcalde en la base de datos usando un procedimiento almacenado
    def insertar_alcalde(self, nombre, apellido, municipio_id, fecha_inicio_mandato, fecha_fin_mandato):
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

    # Insertar un proyecto en la base de datos usando un procedimiento almacenado
    def insertar_proyecto(self, nombre, departamento_id, fecha_inicio, fecha_fin, presupuesto, estado):
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

    # Insertar un proveedor en la base de datos usando un procedimiento almacenado
    def insertar_proveedor(self, nombre, tipo, contacto, telefono, correo):
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

    # Insertar un contrato en la base de datos usando un procedimiento almacenado
    def insertar_contrato(self, proyecto_id, proveedor_id, monto, fecha_firma, fecha_termino, estado):
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

    # Insertar un empleado en la base de datos usando un procedimiento almacenado
    def insertar_empleado(self, nombre, apellido, cargo, departamento_id, fecha_ingreso, salario):
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

    # Insertar un presupuesto en la base de datos usando un procedimiento almacenado
    def insertar_presupuesto_municipal(self, municipio_id, anio, ingresos, egresos, saldo):
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

    # Insertar un programa social en la base de datos usando un procedimiento almacenado
    def insertar_programa_social(self, nombre, departamento_id, beneficiarios, fecha_inicio, fecha_fin):
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

    # Insertar un municipal en la base de datos usando un procedimiento almacenado
    def insertar_evento_municipal(self, nombre, municipio_id, fecha, ubicacion, descripcion, tipo):
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


# Ejecución como script
if __name__ == "__main__":
    # Bloque de conexión
    conexion = Conexion()
    conexionBD = conexion.ConexionBasica()
    if conexionBD:
        # Bloque de inserción

        # Municipio
        conexion.insertar_municipio('Medellín', 2500000, 380.64, 'Daniel Quintero', datetime.date(1616, 3, 2))
        insertar_municipio(conexion, "Envigado", 230000, 79.72, "Braulio Espinosa", datetime.date(1775, 8, 31))
        insertar_municipio(conexion, "Bello", 600000, 149.9, "Óscar Andrés Pérez", datetime.date(1676, 12, 27))

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

        conexion.CerrarConexion(conexionBD)