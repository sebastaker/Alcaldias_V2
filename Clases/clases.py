import pyodbc;
import datetime;
import decimal;

from decimal import Decimal

class Municipio:
    id: int = 0
    nombre: str = None
    poblacion: int = 0
    area: Decimal = Decimal(0)
    alcalde_actual: str = None
    fecha_fundacion: str = None

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetPoblacion(self) -> int:
        return self.poblacion

    def SetPoblacion(self, value: int) -> None:
        self.poblacion = value

    def GetArea(self) -> Decimal:
        return self.area

    def SetArea(self, value: Decimal) -> None:
        self.area = value

    def GetAlcaldeActual(self) -> str:
        return self.alcalde_actual

    def SetAlcaldeActual(self, value: str) -> None:
        self.alcalde_actual = value

    def GetFechaFundacion(self) -> str:
        return self.fecha_fundacion

    def SetFechaFundacion(self, value: str) -> None:
        self.fecha_fundacion = value


class Departamento:
    id: int = 0
    nombre: str = None
    responsable: str = None
    funcion: str = None
    _municipio: Municipio = None  # Relación con Municipio

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetResponsable(self) -> str:
        return self.responsable

    def SetResponsable(self, value: str) -> None:
        self.responsable = value

    def GetFuncion(self) -> str:
        return self.funcion

    def SetFuncion(self, value: str) -> None:
        self.funcion = value

    def GetMunicipio(self) -> Municipio:
        return self._municipio

    def SetMunicipio(self, value: Municipio) -> None:
        self._municipio = value


class Alcalde:
    id: int = 0
    nombre: str = None
    apellido: str = None
    _municipio: Municipio = None  # Relación con Municipio
    fecha_inicio_mandato: str = None
    fecha_fin_mandato: str = None

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetApellido(self) -> str:
        return self.apellido

    def SetApellido(self, value: str) -> None:
        self.apellido = value

    def GetMunicipio(self) -> Municipio:
        return self._municipio

    def SetMunicipio(self, value: Municipio) -> None:
        self._municipio = value

    def GetFechaInicioMandato(self) -> str:
        return self.fecha_inicio_mandato

    def SetFechaInicioMandato(self, value: str) -> None:
        self.fecha_inicio_mandato = value

    def GetFechaFinMandato(self) -> str:
        return self.fecha_fin_mandato

    def SetFechaFinMandato(self, value: str) -> None:
        self.fecha_fin_mandato = value


class Proyecto:
    id: int = 0
    nombre: str = None
    _departamento: Departamento = None  # Relación con Departamento
    fecha_inicio: str = None
    fecha_fin: str = None
    presupuesto: Decimal = Decimal(0)
    estado: str = None

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetDepartamento(self) -> Departamento:
        return self._departamento

    def SetDepartamento(self, value: Departamento) -> None:
        self._departamento = value

    def GetFechaInicio(self) -> str:
        return self.fecha_inicio

    def SetFechaInicio(self, value: str) -> None:
        self.fecha_inicio = value

    def GetFechaFin(self) -> str:
        return self.fecha_fin

    def SetFechaFin(self, value: str) -> None:
        self.fecha_fin = value

    def GetPresupuesto(self) -> Decimal:
        return self.presupuesto

    def SetPresupuesto(self, value: Decimal) -> None:
        self.presupuesto = value

    def GetEstado(self) -> str:
        return self.estado

    def SetEstado(self, value: str) -> None:
        self.estado = value


class Proveedor:
    id: int = 0
    nombre: str = None
    tipo: str = None
    contacto: str = None
    telefono: str = None
    correo: str = None

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetTipo(self) -> str:
        return self.tipo

    def SetTipo(self, value: str) -> None:
        self.tipo = value

    def GetContacto(self) -> str:
        return self.contacto

    def SetContacto(self, value: str) -> None:
        self.contacto = value

    def GetTelefono(self) -> str:
        return self.telefono

    def SetTelefono(self, value: str) -> None:
        self.telefono = value

    def GetCorreo(self) -> str:
        return self.correo

    def SetCorreo(self, value: str) -> None:
        self.correo = value


class Contrato:
    id: int = 0
    _proyecto: Proyecto = None  # Relación con Proyecto
    _proveedor: Proveedor = None  # Relación con Proveedor
    monto: Decimal = Decimal(0)
    fecha_firma: str = None
    fecha_termino: str = None
    estado: str = None

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetProyecto(self) -> Proyecto:
        return self._proyecto

    def SetProyecto(self, value: Proyecto) -> None:
        self._proyecto = value

    def GetProveedor(self) -> Proveedor:
        return self._proveedor

    def SetProveedor(self, value: Proveedor) -> None:
        self._proveedor = value

    def GetMonto(self) -> Decimal:
        return self.monto

    def SetMonto(self, value: Decimal) -> None:
        self.monto = value

    def GetFechaFirma(self) -> str:
        return self.fecha_firma

    def SetFechaFirma(self, value: str) -> None:
        self.fecha_firma = value

    def GetFechaTermino(self) -> str:
        return self.fecha_termino

    def SetFechaTermino(self, value: str) -> None:
        self.fecha_termino = value

    def GetEstado(self) -> str:
        return self.estado

    def SetEstado(self, value: str) -> None:
        self.estado = value


class Empleado:
    id: int = 0
    nombre: str = None
    apellido: str = None
    cargo: str = None
    _departamento: Departamento = None  # Relación con Departamento
    fecha_ingreso: str = None
    salario: Decimal = Decimal(0)

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetApellido(self) -> str:
        return self.apellido

    def SetApellido(self, value: str) -> None:
        self.apellido = value

    def GetCargo(self) -> str:
        return self.cargo

    def SetCargo(self, value: str) -> None:
        self.cargo = value

    def GetDepartamento(self) -> Departamento:
        return self._departamento

    def SetDepartamento(self, value: Departamento) -> None:
        self._departamento = value

    def GetFechaIngreso(self) -> str:
        return self.fecha_ingreso

    def SetFechaIngreso(self, value: str) -> None:
        self.fecha_ingreso = value

    def GetSalario(self) -> Decimal:
        return self.salario

    def SetSalario(self, value: Decimal) -> None:
        self.salario = value


from decimal import Decimal

class PresupuestoMunicipal:
    id: int = 0
    _municipio: Municipio = None  # Relación con Municipio
    anio: int = 0
    ingresos: Decimal = Decimal(0)
    egresos: Decimal = Decimal(0)
    saldo: Decimal = Decimal(0)

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetMunicipio(self) -> Municipio:
        return self._municipio

    def SetMunicipio(self, value: Municipio) -> None:
        self._municipio = value

    def GetAnio(self) -> int:
        return self.anio

    def SetAnio(self, value: int) -> None:
        self.anio = value

    def GetIngresos(self) -> Decimal:
        return self.ingresos

    def SetIngresos(self, value: Decimal) -> None:
        self.ingresos = value

    def GetEgresos(self) -> Decimal:
        return self.egresos

    def SetEgresos(self, value: Decimal) -> None:
        self.egresos = value

    def GetSaldo(self) -> Decimal:
        return self.saldo

    def SetSaldo(self, value: Decimal) -> None:
        self.saldo = value


class ProgramaSocial:
    id: int = 0
    nombre: str = None
    _departamento: Departamento = None  # Relación con Departamento
    beneficiarios: int = 0
    fecha_inicio: str = None
    fecha_fin: str = None

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetDepartamento(self) -> Departamento:
        return self._departamento

    def SetDepartamento(self, value: Departamento) -> None:
        self._departamento = value

    def GetBeneficiarios(self) -> int:
        return self.beneficiarios

    def SetBeneficiarios(self, value: int) -> None:
        self.beneficiarios = value

    def GetFechaInicio(self) -> str:
        return self.fecha_inicio

    def SetFechaInicio(self, value: str) -> None:
        self.fecha_inicio = value

    def GetFechaFin(self) -> str:
        return self.fecha_fin

    def SetFechaFin(self, value: str) -> None:
        self.fecha_fin = value


class EventoMunicipal:
    id: int = 0
    nombre: str = None
    _municipio: Municipio = None  # Relación con Municipio
    fecha: str = None
    ubicacion: str = None
    descripcion: str = None
    tipo: str = None

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre

    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetMunicipio(self) -> Municipio:
        return self._municipio

    def SetMunicipio(self, value: Municipio) -> None:
        self._municipio = value

    def GetFecha(self) -> str:
        return self.fecha

    def SetFecha(self, value: str) -> None:
        self.fecha = value

    def GetUbicacion(self) -> str:
        return self.ubicacion

    def SetUbicacion(self, value: str) -> None:
        self.ubicacion = value

    def GetDescripcion(self) -> str:
        return self.descripcion

    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    def GetTipo(self) -> str:
        return self.tipo

    def SetTipo(self, value: str) -> None:
        self.tipo = value
