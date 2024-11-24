import pymysql
import pyodbc

class Conexion:
  # Cadena de conexión
    string_conexion = {
            'host': 'localhost',
            'user': 'sebas_python',  
            'password': 'Sebas5279',
            'database': 'Administracion_Alcaldias',
            'port': 3306  # Puerto por defecto para MySQL
        }
    
    def get_conexion(self):
        """Devuelve una conexión a la base de datos."""
        return pymysql.connect(**self.string_conexion)

    def verificar_conexion(self):
        try:
            conexion = self.get_conexion()
            print("Conexión exitosa a la base de datos.")
            conexion.close()
        except pymysql.MySQLError as e:
            print(f"Error al conectar a la base de datos: {e}")

class Conexion2:
  # Cadena de conexión
    string_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=Administracion_Alcaldias;
        PORT=3306;
        user=sebas_python;
        password=Sebas5279"""
    
    def get_conexion(self):
        """Devuelve una conexión a la base de datos."""
        return pyodbc.connect(self.string_conexion)
    
    def verificar_conexion(self):
        try:
            conexion = self.get_conexion()
            print("Conexión exitosa a la base de datos.")
            conexion.close()
        except pyodbc.Error as e:            
            print("Error al conectar con la base de datos: ", e)
            return None