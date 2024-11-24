import pyodbc
import pymysql
from Clases.clases import *
from Clases.Conexion import Conexion


class Select:
    def consultar_municipio(self, municipio_id: int) -> None:
        conexion = Conexion()
        consulta: str = "CALL proc_SelectMunicipio(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {municipio_id}")
        
        try:
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar la consulta y pasa el parámetro
            cursor.execute(consulta, (municipio_id,))
            
            lista = []
            
            for elemento in cursor.fetchall():                
                entidad = Municipio()
                entidad.SetId(elemento[0])
                entidad.SetNombre(elemento[1])
                entidad.SetPoblacion(elemento[2])
                entidad.SetArea(elemento[3])
                entidad.SetAlcaldeActual(elemento[4])
                entidad.SetFechaFundacion(elemento[5])
                lista.append(entidad)
            
            cursor.close()
            conexion.close()
            
            # Imprimir los resultados
            for dato in lista:
                print(f"Id: {dato.GetId()}, Nombre Municipio: {dato.GetNombre()}, Poblacion: {dato.GetPoblacion()}, Area: {dato.GetArea()}, Alcalde Actual: {dato.GetAlcaldeActual()}, Fecha Fundacion: {dato.GetFechaFundacion()}")
        
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    def consultar_departamento(self, departamento_id: int) -> None:
        conexion = Conexion()
        consulta: str = "CALL proc_SelectDepartamento(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {departamento_id}")
        
        try:
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar la consulta con el parámetro
            cursor.execute(consulta, (departamento_id,))
            lista: list = []

            for elemento in cursor.fetchall():
                entidad = Departamento()
                entidad.SetId(elemento[0])
                entidad.SetNombre(elemento[1])
                entidad.SetMunicipio(Municipio())
                entidad.GetMunicipio().SetId(elemento[2])
                entidad.SetResponsable(elemento[3])
                entidad.SetFuncion(elemento[4])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for dato in lista:
                print(f"Id: {dato.GetId()}, Nombre Departamento: {dato.GetNombre()}, "
                    f"Municipio ID: {dato.GetMunicipio().GetId()}, Responsable: {dato.GetResponsable()}, "
                    f"Función: {dato.GetFuncion()}")
        
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    def consultar_alcalde(self, alcalde_id: int) -> None:
        conexion = Conexion()
        consulta: str = "CALL proc_SelectAlcalde(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {alcalde_id}")
        
        try:
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar la consulta con el parámetro
            cursor.execute(consulta, (alcalde_id,))
            lista: list = []

            for elemento in cursor.fetchall():
                entidad = Alcalde()
                entidad.SetId(elemento[0])
                entidad.SetNombre(elemento[1])
                entidad.SetApellido(elemento[2])
                entidad.SetMunicipio(Municipio())
                entidad.GetMunicipio().SetId(elemento[3])
                entidad.SetFechaInicioMandato(elemento[4])
                entidad.SetFechaFinMandato(elemento[5])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for dato in lista:
                print(f"Id: {dato.GetId()}, Nombre Alcalde: {dato.GetNombre()}, Apellido: {dato.GetApellido()}, "
                    f"Municipio ID: {dato.GetMunicipio().GetId()}, Fecha Inicio Mandato: {dato.GetFechaInicioMandato()}, "
                    f"Fecha Fin Mandato: {dato.GetFechaFinMandato()}")
        
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    def consultar_proyecto(self, proyecto_id: int) -> None:
        conexion = Conexion()
        consulta: str = "CALL proc_SelectProyecto(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {proyecto_id}")
        
        try:
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar la consulta con el parámetro
            cursor.execute(consulta, (proyecto_id,))
            lista: list = []

            for elemento in cursor.fetchall():
                entidad = Proyecto()
                entidad.SetId(elemento[0])
                entidad.SetNombre(elemento[1])
                entidad.SetDepartamento(Departamento())
                entidad.GetDepartamento().SetId(elemento[2])
                entidad.SetFechaInicio(elemento[3])
                entidad.SetFechaFin(elemento[4])
                entidad.SetPresupuesto(elemento[5])
                entidad.SetEstado(elemento[6])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for dato in lista:
                print(f"Id: {dato.GetId()}, Nombre Proyecto: {dato.GetNombre()}, "
                    f"Departamento ID: {dato.GetDepartamento().GetId()}, Fecha Inicio: {dato.GetFechaInicio()}, "
                    f"Fecha Fin: {dato.GetFechaFin()}, Presupuesto: {dato.GetPresupuesto()}, Estado: {dato.GetEstado()}")
        
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    def consultar_proveedor(self, proveedor_id: int) -> None:
        conexion = Conexion()
        consulta: str = "CALL proc_SelectProveedor(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {proveedor_id}")
        
        try:
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar la consulta con el parámetro
            cursor.execute(consulta, (proveedor_id,))
            lista: list = []

            for elemento in cursor.fetchall():
                entidad = Proveedor()
                entidad.SetId(elemento[0])
                entidad.SetNombre(elemento[1])
                entidad.SetTipo(elemento[2])
                entidad.SetContacto(elemento[3])
                entidad.SetTelefono(elemento[4])
                entidad.SetCorreo(elemento[5])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for dato in lista:
                print(f"Id: {dato.GetId()}, Nombre Proveedor: {dato.GetNombre()}, Tipo: {dato.GetTipo()}, "
                    f"Contacto: {dato.GetContacto()}, Teléfono: {dato.GetTelefono()}, Correo: {dato.GetCorreo()}")
        
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    def consultar_contrato(self, contrato_id: int) -> None:
        conexion = Conexion()
        consulta: str = "CALL proc_SelectContrato(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {contrato_id}")
        
        try:
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar la consulta con el parámetro
            cursor.execute(consulta, (contrato_id,))
            lista: list = []

            for elemento in cursor.fetchall():
                entidad = Contrato()
                entidad.SetId(elemento[0])
                entidad.SetProyecto(Proyecto())
                entidad.GetProyecto().SetId(elemento[1])
                entidad.SetProveedor(Proveedor())
                entidad.GetProveedor().SetId(elemento[2])
                entidad.SetMonto(elemento[3])
                entidad.SetFechaFirma(elemento[4])
                entidad.SetFechaTermino(elemento[5])
                entidad.SetEstado(elemento[6])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for dato in lista:
                print(f"Id: {dato.GetId()}, Proyecto ID: {dato.GetProyecto().GetId()}, Proveedor ID: {dato.GetProveedor().GetId()}, "
                    f"Monto: {dato.GetMonto()}, Fecha Firma: {dato.GetFechaFirma()}, Fecha Termino: {dato.GetFechaTermino()}, "
                    f"Estado: {dato.GetEstado()}")
        
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    def consultar_empleado(self, empleado_id: int) -> None:
        conexion = Conexion()
        consulta: str = "CALL proc_SelectEmpleado(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {empleado_id}")
        
        try:
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar la consulta con el parámetro
            cursor.execute(consulta, (empleado_id,))
            lista: list = []

            for elemento in cursor.fetchall():
                entidad = Empleado()
                entidad.SetId(elemento[0])
                entidad.SetNombre(elemento[1])
                entidad.SetApellido(elemento[2])
                entidad.SetCargo(elemento[3])
                entidad.SetDepartamento(Departamento())
                entidad.GetDepartamento().SetId(elemento[4])
                entidad.SetFechaIngreso(elemento[5])
                entidad.SetSalario(elemento[6])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for dato in lista:
                print(f"Id: {dato.GetId()}, Nombre Empleado: {dato.GetNombre()}, Apellido: {dato.GetApellido()}, "
                    f"Cargo: {dato.GetCargo()}, Departamento ID: {dato.GetDepartamento().GetId()}, Fecha Ingreso: {dato.GetFechaIngreso()}, "
                    f"Salario: {dato.GetSalario()}")
        
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    def consultar_presupuesto_municipal(self, presupuesto_id: int) -> None:
        conexion = Conexion()
        consulta: str = "CALL proc_SelectPresupuestoMunicipal(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {presupuesto_id}")
        
        try:
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar la consulta con el parámetro
            cursor.execute(consulta, (presupuesto_id,))
            lista: list = []

            for elemento in cursor.fetchall():
                entidad = PresupuestoMunicipal()
                entidad.SetId(elemento[0])
                entidad.SetMunicipio(Municipio())
                entidad.GetMunicipio().SetId(elemento[1])
                entidad.SetAnio(elemento[2])
                entidad.SetIngresos(elemento[3])
                entidad.SetEgresos(elemento[4])
                entidad.SetSaldo(elemento[5])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for dato in lista:
                print(f"Id: {dato.GetId()}, Municipio ID: {dato.GetMunicipio().GetId()}, Año: {dato.GetAnio()}, "
                    f"Ingresos: {dato.GetIngresos()}, Egresos: {dato.GetEgresos()}, Saldo: {dato.GetSaldo()}")
        
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

    def consultar_programa_social(self, programa_id: int) -> None:
        conexion = Conexion()
        consulta: str = "CALL proc_SelectProgramaSocial(%s)"
        print(f"Ejecutando consulta: {consulta} con parámetro: {programa_id}")
        
        try:
            conexion = conexion.get_conexion()
            cursor = conexion.cursor()

            # Ejecutar la consulta con el parámetro
            cursor.execute(consulta, (programa_id,))
            lista: list = []

            for elemento in cursor.fetchall():
                entidad = ProgramaSocial()
                entidad.SetId(elemento[0])
                entidad.SetNombre(elemento[1])
                entidad.SetDepartamento(Departamento())
                entidad.GetDepartamento().SetId(elemento[2])
                entidad.SetBeneficiarios(elemento[3])
                entidad.SetFechaInicio(elemento[4])
                entidad.SetFechaFin(elemento[5])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for dato in lista:
                print(f"Id: {dato.GetId()}, Nombre Programa: {dato.GetNombre()}, Departamento ID: {dato.GetDepartamento().GetId()}, "
                    f"Beneficiarios: {dato.GetBeneficiarios()}, Fecha Inicio: {dato.GetFechaInicio()}, Fecha Fin: {dato.GetFechaFin()}")
        
        except pymysql.MySQLError as e:
            print(f"Error al ejecutar la consulta: {e}")

