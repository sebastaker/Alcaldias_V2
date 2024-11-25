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
# @app.route('/<tabla>/<accion>', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def controlador_generico(tabla, accion):
#     try:
#         if accion == "consultar" and request.method == "GET":
#             id_registro = request.args.get('id', type=int)
#             if not id_registro:
#                 return jsonify({"error": "Falta el parámetro 'id'"}), 400

#             # Llama al método correspondiente
#             resultado = getattr(conexion, f"consultar_{tabla}")(id_registro)
#             return jsonify({"resultado": resultado}), 200

#         elif accion == "insertar" and request.method == "POST":
#             datos = request.json
#             # Llama al método genérico para insertar datos
#             getattr(conexion_insert, f"insertar_{tabla}")(**datos)
#             return jsonify({"mensaje": f"{tabla.capitalize()} insertado correctamente"}), 201

#         elif accion == "actualizar" and request.method == "PUT":
#             datos = request.json
#             # Llama al método genérico para actualizar datos
#             getattr(conexion_update, f"actualizar_{tabla}")(**datos)
#             return jsonify({"mensaje": f"{tabla.capitalize()} actualizado correctamente"}), 200

#         elif accion == "eliminar" and request.method == "DELETE":
#             id_registro = request.args.get('id', type=int)
#             if not id_registro:
#                 return jsonify({"error": "Falta el parámetro 'id'"}), 400

#             # Llama al método genérico para eliminar
#             getattr(conexion_delete, f"eliminar_{tabla}")(id_registro)
#             return jsonify({"mensaje": f"{tabla.capitalize()} eliminado correctamente"}), 200

#         else:
#             return jsonify({"error": "Acción no soportada"}), 400

#     except AttributeError:
#         return jsonify({"error": f"Tabla o acción no soportada: {tabla}, {accion}"}), 400
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

    # Diccionario que mapea cada tabla con los parámetros requeridos
PARAMETROS_REQUERIDOS = {
    "municipio": ["nombre", "poblacion", "area", "alcalde_actual", "fecha_fundacion"],
    "departamento": ["nombre", "municipio_id", "responsable", "funcion"],
    "alcalde": ["nombre", "apellido", "municipio_id", "fecha_inicio_mandato", "fecha_fin_mandato"],
    "proyecto": ["nombre", "departamento_id", "fecha_inicio", "fecha_fin", "presupuesto", "estado"],
    "proveedor": ["nombre", "tipo", "contacto", "telefono", "correo"],
    "contrato": ["proyecto_id", "proveedor_id", "monto", "fecha_firma", "fecha_termino", "estado"],
    "empleado": ["nombre", "apellido", "cargo", "departamento_id", "fecha_ingreso", "salario"],
    "presupuesto_municipal": ["municipio_id", "anio", "ingresos", "egresos", "saldo"],
    "programa_social": ["nombre", "departamento_id", "beneficiarios", "fecha_inicio", "fecha_fin"],
    "evento_municipal": ["nombre", "municipio_id", "fecha", "ubicacion", "descripcion", "tipo"],
}

@app.route('/<tabla>/<accion>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def controlador_generico(tabla, accion):
    try:
        # Verificar si la tabla es válida
        if tabla not in PARAMETROS_REQUERIDOS:
            return jsonify({"error": f"Tabla no soportada: {tabla}"}), 400

        # Obtener los datos del cuerpo de la solicitud para POST y PUT
        datos = request.json if request.method in ["POST", "PUT"] else {}

        # Validar parámetros requeridos para las acciones de insertar y actualizar
        if accion in ["insertar", "actualizar"]:
            parametros_requeridos = PARAMETROS_REQUERIDOS[tabla]
            parametros_faltantes = [param for param in parametros_requeridos if param not in datos]
            if parametros_faltantes:
                return jsonify({"error": f"Faltan los siguientes parámetros: {', '.join(parametros_faltantes)}"}), 400

            # Convertir fechas en formato string a objetos datetime, si es necesario
            for key in datos:
                if "fecha" in key and isinstance(datos[key], str):
                    try:
                        datos[key] = datetime.datetime.strptime(datos[key], "%Y-%m-%d").date()
                    except ValueError:
                        return jsonify({"error": f"El formato de la fecha '{key}' debe ser YYYY-MM-DD"}), 400

            # Llama al método correspondiente en la clase Insert o Update
            metodo = f"{accion}_{tabla}"
            getattr(globals()[f"conexion_{accion}"], metodo)(**datos)
            return jsonify({"mensaje": f"{tabla.capitalize()} {accion}ado correctamente"}), 200 if accion == "actualizar" else 201

        elif accion == "consultar" and request.method == "GET":
            id_registro = request.args.get('id', type=int)
            if not id_registro:
                return jsonify({"error": "Falta el parámetro 'id'"}), 400

            resultado = getattr(conexion, f"consultar_{tabla}")(id_registro)
            return jsonify({"resultado": resultado}), 200

        elif accion == "eliminar" and request.method == "DELETE":
            id_registro = request.args.get('id', type=int)
            if not id_registro:
                return jsonify({"error": "Falta el parámetro 'id'"}), 400

            getattr(conexion_delete, f"eliminar_{tabla}")(id_registro)
            return jsonify({"mensaje": f"{tabla.capitalize()} eliminado correctamente"}), 200

        else:
            return jsonify({"error": "Acción no soportada"}), 400

    except AttributeError as e:
        return jsonify({"error": f"Tabla o acción no soportada: {tabla}, {accion}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Correr la aplicación
if __name__ == "__main__":
    app.run(host='localhost', port=4040)