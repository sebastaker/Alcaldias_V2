import sys;
import jsonify;
import flask;
import sys;
import json;
import pyodbc;
import datetime;
import decimal;

# print( "¡Hola Mundo!" );
# app = flask.Flask(__name__);
# print(__name__);

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

# Ejecución como script
if __name__ == "__main__":
    # Bloque de conexión
    conexion = Conexion()
    conexionBD = conexion.ConexionBasica()
    # conexion.CerrarConexion(conexionBD)