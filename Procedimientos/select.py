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

    def consultar_municipio(self) -> None:

        consulta: str = ("CALL proc_SelectMunicipio()") # Llama al procedimiento almacenado
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        
        cursor.execute(consulta)  
        lista: list = []
        
        for elemento in cursor:
            entidad = Municipio()
            entidad.SetId(elemento[0])
            entidad.SetPoblacion(elemento[1])
            entidad.SetArea(elemento[2])
            entidad.SetAlcaldeActual(elemento[3])
            entidad.SetFechaFundacion(elemento[4])
            lista.append(entidad)
        
        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Nombre Municipio: {dato.GetNombre()}, Poblacion: {dato.GetPoblacion()}, Area: {dato.GetArea()}, Alcalde Actual: {dato.GetAlcaldeActual()}, Fecha Funcacion: {dato.GetFechaFundacion()}")

    
    def consultar_municipio(self) -> None:
        consulta: str = "CALL proc_SelectMunicipio()"
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        cursor.execute(consulta)
        lista: list = []

        for elemento in cursor:
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

        for dato in lista:
            print(f"Id: {dato.GetId()}, Nombre Municipio: {dato.GetNombre()}, "
                f"Poblacion: {dato.GetPoblacion()}, Area: {dato.GetArea()}, "
                f"Alcalde Actual: {dato.GetAlcaldeActual()}, Fecha Fundación: {dato.GetFechaFundacion()}")

    def consultar_departamento(self) -> None:
        consulta: str = "CALL proc_SelectDepartamento()"
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        cursor.execute(consulta)
        lista: list = []

        for elemento in cursor:
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

    def consultar_alcalde(self) -> None:
        consulta: str = "CALL proc_SelectAlcalde()"
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        cursor.execute(consulta)
        lista: list = []

        for elemento in cursor:
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

    def consultar_proyecto(self) -> None:
        consulta: str = "CALL proc_SelectProyecto()"
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        cursor.execute(consulta)
        lista: list = []

        for elemento in cursor:
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

    def consultar_proveedor(self) -> None:
        consulta: str = "CALL proc_SelectProveedor()"
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        cursor.execute(consulta)
        lista: list = []

        for elemento in cursor:
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

    def consultar_contrato(self) -> None:
        consulta: str = "CALL proc_SelectContrato()"
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        cursor.execute(consulta)
        lista: list = []

        for elemento in cursor:
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

    def consultar_empleado(self) -> None:
        consulta: str = "CALL proc_SelectEmpleado()"
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        cursor.execute(consulta)
        lista: list = []

        for elemento in cursor:
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

    def consultar_presupuesto_municipal(self) -> None:
        consulta: str = "CALL proc_SelectPresupuestoMunicipal()"
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        cursor.execute(consulta)
        lista: list = []

        for elemento in cursor:
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

    def consultar_programa_social(self) -> None:
        consulta: str = "CALL proc_SelectProgramaSocial()"
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()

        cursor.execute(consulta)
        lista: list = []

        for elemento in cursor:
            entidad = ProgramaSocial()
            entidad.SetId(elemento[0])
            entidad.SetNombre(elemento[1])
            entidad.SetDepartamento(Departamento())
            entidad.GetDepartamento().SetId(elemento[2])
            entidad.SetPresupuesto(elemento[3])
            entidad.SetFechaInicio(elemento[4])
            entidad.SetFechaFin(elemento[5])
            lista.append(entidad)

        cursor.close()
        conexion.close()

        for dato in lista:
            print(f"Id: {dato.GetId()}, Nombre Programa: {dato.GetNombre()}, Departamento ID: {dato.GetDepartamento().GetId()}, "
                f"Presupuesto: {dato.GetPresupuesto()}, Fecha Inicio: {dato.GetFechaInicio()}, Fecha Fin: {dato.GetFechaFin()}")

