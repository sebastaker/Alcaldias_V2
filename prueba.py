import sys;
import jsonify;
import flask;
import json;
import datetime;
from flask import Flask, jsonify, request
from Clases.clases import *
from Clases.Conexion import *
import Procedimientos.select as select
import Procedimientos.insert as insert
import Procedimientos.delete as delete
import Procedimientos.update as update
 
app = Flask(__name__)
 
# Instanciar las clases de conexión
conexion = select.Select()
conexion_update = update.Update()
conexion_insert = insert.Insert()
conexion_delete = delete.Delete()
 
#Controlador generico que recibe tabla y accion como parametro para su funcion
@app.route('/<tabla>/<accion>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def controlador_generico(tabla, accion):
    try:
        if accion == "consultar" and request.method == "GET":
            id_registro = request.args.get('id', type=int)
            if not id_registro:
                return jsonify({"error": "Falta el parámetro 'id'"}), 400
 
            # Llama al método correspondiente
            resultado = getattr(conexion, f"consultar_{tabla}")(id_registro)
            #return jsonify({"resultado": resultado}), 200
            return jsonify({"mensaje": f"{tabla.capitalize()} constultado correctamente"})
 
        elif accion == "insertar" and request.method == "POST":
            datos = request.json
            # Llama al método genérico para insertar datos
            getattr(conexion_insert, f"insertar_{tabla}")(**datos)
            return jsonify({"mensaje": f"{tabla.capitalize()} insertado correctamente"}), 201
 
        elif accion == "actualizar" and request.method == "PUT":
            datos = request.json
            # Llama al método genérico para actualizar datos
            getattr(conexion_update, f"actualizar_{tabla}")(**datos)
            return jsonify({"mensaje": f"{tabla.capitalize()} actualizado correctamente"}), 200
 
        elif accion == "eliminar" and request.method == "DELETE":
            id_registro = request.args.get('id', type=int)
            if not id_registro:
                return jsonify({"error": "Falta el parámetro 'id'"}), 400
 
            # Llama al método genérico para eliminar
            getattr(conexion_delete, f"eliminar_{tabla}")(id_registro)
            return jsonify({"mensaje": f"{tabla.capitalize()} eliminado correctamente"}), 200
 
        else:
            return jsonify({"error": "Acción no soportada"}), 400
 
    except AttributeError:
        return jsonify({"error": f"Tabla o acción no soportada: {tabla}, {accion}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
   
# Correr la aplicación
if __name__ == "__main__":
    app.run(host='localhost', port=4040)