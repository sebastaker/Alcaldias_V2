-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS Administracion_Alcaldias;
USE Administracion_Alcaldias;

-- Creación de las tablas

CREATE TABLE MUNICIPIOS (
    municipio_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    poblacion INT NOT NULL,
    area DECIMAL(10, 2) NOT NULL,
    alcalde_actual VARCHAR(100),
    fecha_fundacion DATE
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE DEPARTAMENTOS (
    departamento_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    municipio_id INT,
    responsable VARCHAR(100),
    funcion VARCHAR(255),
    FOREIGN KEY (municipio_id) REFERENCES MUNICIPIOS(municipio_id) ON DELETE CASCADE
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE ALCALDES (
    alcalde_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    municipio_id INT,
    fecha_inicio_mandato DATE,
    fecha_fin_mandato DATE,
    FOREIGN KEY (municipio_id) REFERENCES MUNICIPIOS(municipio_id) ON DELETE CASCADE
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE PROYECTOS (
    proyecto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    departamento_id INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    presupuesto DECIMAL(15, 2),
    estado VARCHAR(50),
    FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(departamento_id) ON DELETE CASCADE
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE PROVEEDORES (
    proveedor_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50),
    contacto VARCHAR(100),
    telefono VARCHAR(20),
    correo VARCHAR(100)
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE CONTRATOS (
    contrato_id INT PRIMARY KEY AUTO_INCREMENT,
    proyecto_id INT,
    proveedor_id INT,
    monto DECIMAL(15, 2),
    fecha_firma DATE,
    fecha_termino DATE,
    estado VARCHAR(50),
    FOREIGN KEY (proyecto_id) REFERENCES PROYECTOS(proyecto_id) ON DELETE CASCADE,
    FOREIGN KEY (proveedor_id) REFERENCES PROVEEDORES(proveedor_id) ON DELETE CASCADE
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE EMPLEADOS (
    empleado_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    cargo VARCHAR(100),
    departamento_id INT,
    fecha_ingreso DATE,
    salario DECIMAL(15, 2),
    FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(departamento_id) ON DELETE CASCADE
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE PRESUPUESTO_MUNICIPAL (
    presupuesto_id INT PRIMARY KEY AUTO_INCREMENT,
    municipio_id INT,
    anio INT NOT NULL,
    ingresos DECIMAL(15, 2),
    egresos DECIMAL(15, 2),
    saldo DECIMAL(15, 2),
    FOREIGN KEY (municipio_id) REFERENCES MUNICIPIOS(municipio_id) ON DELETE CASCADE
) DEFAULT CHARSET=utf8mb4; 

CREATE TABLE PROGRAMAS_SOCIALES (
    programa_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    departamento_id INT,
    beneficiarios INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(departamento_id) ON DELETE CASCADE
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE EVENTOS_MUNICIPALES (
    evento_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    municipio_id INT,
    fecha DATE,
    ubicacion VARCHAR(100),
    descripcion TEXT,
    tipo VARCHAR(50),
    FOREIGN KEY (municipio_id) REFERENCES MUNICIPIOS(municipio_id) ON DELETE CASCADE
) DEFAULT CHARSET=utf8mb4;

-- Inserción de datos 

INSERT INTO MUNICIPIOS (nombre, poblacion, area, alcalde_actual, fecha_fundacion)
VALUES 
('Medellín', 2500000, 380.64, 'Daniel Quintero', '1616-03-02'),
('Envigado', 230000, 79.72, 'Braulio Espinosa', '1775-08-31'),
('Bello', 600000, 149.90, 'Óscar Andrés Pérez', '1676-12-27');

INSERT INTO DEPARTAMENTOS (nombre, municipio_id, responsable, funcion)
VALUES 
('Despacho del Alcalde', 1, 'Daniel Quintero', 'Centro de toma de decisiones y representación legal'),
('Secretaría General', 1, 'Juan Pérez', 'Coordinación de actividades administrativas'),
('Secretaría de Hacienda', 1, 'María González', 'Administración de los recursos financieros del municipio');

INSERT INTO ALCALDES (nombre, apellido, municipio_id, fecha_inicio_mandato, fecha_fin_mandato)
VALUES 
('Daniel', 'Quintero', 1, '2020-01-01', '2023-12-31'),
('Braulio', 'Espinosa', 2, '2020-01-01', '2023-12-31'),
('Óscar Andrés', 'Pérez', 3, '2020-01-01', '2023-12-31');

INSERT INTO PROYECTOS (nombre, departamento_id, fecha_inicio, fecha_fin, presupuesto, estado)
VALUES 
('Construcción de Parque', 1, '2023-01-01', '2023-12-31', 50000000, 'En progreso'),
('Mejoramiento de Vías', 2, '2023-02-01', '2023-11-30', 120000000, 'En progreso');

INSERT INTO PROVEEDORES (nombre, tipo, contacto, telefono, correo)
VALUES 
('Construcciones Antioquia', 'Construcción', 'Carlos Ríos', '3012345678', 'contacto@construantioquia.com'),
('Servicios Urbanos', 'Servicios Públicos', 'Ana López', '3023456789', 'info@serviciosurbanos.com');

INSERT INTO CONTRATOS (proyecto_id, proveedor_id, monto, fecha_firma, fecha_termino, estado)
VALUES 
(1, 1, 25000000, '2023-01-15', '2023-06-30', 'Completado'),
(2, 2, 80000000, '2023-03-01', '2023-10-30', 'En progreso');

INSERT INTO EMPLEADOS (nombre, apellido, cargo, departamento_id, fecha_ingreso, salario)
VALUES 
('Juan', 'Pérez', 'Coordinador General', 2, '2019-03-15', 3000000),
('María', 'González', 'Secretaria de Hacienda', 3, '2018-06-01', 3500000);

INSERT INTO PRESUPUESTO_MUNICIPAL (municipio_id, anio, ingresos, egresos, saldo)
VALUES 
(1, 2023, 800000000, 650000000, 150000000),
(2, 2023, 300000000, 250000000, 50000000);

INSERT INTO PROGRAMAS_SOCIALES (nombre, departamento_id, beneficiarios, fecha_inicio, fecha_fin)
VALUES 
('Alimentación Escolar', 2, 10000, '2023-01-01', '2023-12-31'),
('Subsidio de Transporte', 3, 5000, '2023-01-01', '2023-06-30');

INSERT INTO EVENTOS_MUNICIPALES (nombre, municipio_id, fecha, ubicacion, descripcion, tipo)
VALUES 
('Feria de las Flores', 1, '2023-08-01', 'Centro de Medellín', 'Evento cultural tradicional', 'Cultural'),
('Festival del Rio', 2, '2023-09-15', 'Parque Principal', 'Celebración anual del río', 'Recreativo');

-- Procedimientos almacenados para insertar datos

DELIMITER $$

CREATE PROCEDURE proc_InsertMunicipio(
    IN p_nombre VARCHAR(100),
    IN p_poblacion INT,
    IN p_area FLOAT,
    IN p_alcalde_actual VARCHAR(100),
    IN p_fecha_fundacion DATE
)
BEGIN
    INSERT INTO MUNICIPIOS (nombre, poblacion, area, alcalde_actual, fecha_fundacion)
    VALUES (p_nombre, p_poblacion, p_area, p_alcalde_actual, p_fecha_fundacion);
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_InsertDepartamento(
    IN p_nombre VARCHAR(100),
    IN p_municipio_id INT,
    IN p_responsable VARCHAR(100),
    IN p_funcion VARCHAR(255)
)
BEGIN
    INSERT INTO DEPARTAMENTOS (nombre, municipio_id, responsable, funcion)
    VALUES (p_nombre, p_municipio_id, p_responsable, p_funcion);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_InsertAlcalde(
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_municipio_id INT,
    IN p_fecha_inicio_mandato DATE,
    IN p_fecha_fin_mandato DATE
)
BEGIN
    INSERT INTO ALCALDES (nombre, apellido, municipio_id, fecha_inicio_mandato, fecha_fin_mandato)
    VALUES (p_nombre, p_apellido, p_municipio_id, p_fecha_inicio_mandato, p_fecha_fin_mandato);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_InsertProyecto(
    IN p_nombre VARCHAR(100),
    IN p_departamento_id INT,
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_presupuesto FLOAT,
    IN p_estado VARCHAR(50)
)
BEGIN
    INSERT INTO PROYECTOS (nombre, departamento_id, fecha_inicio, fecha_fin, presupuesto, estado)
    VALUES (p_nombre, p_departamento_id, p_fecha_inicio, p_fecha_fin, p_presupuesto, p_estado);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_InsertProveedor(
    IN p_nombre VARCHAR(100),
    IN p_tipo VARCHAR(50),
    IN p_contacto VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_correo VARCHAR(100)
)
BEGIN
    INSERT INTO PROVEEDORES (nombre, tipo, contacto, telefono, correo)
    VALUES (p_nombre, p_tipo, p_contacto, p_telefono, p_correo);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_InsertContrato(
    IN p_proyecto_id INT,
    IN p_proveedor_id INT,
    IN p_monto FLOAT,
    IN p_fecha_firma DATE,
    IN p_fecha_termino DATE,
    IN p_estado VARCHAR(50)
)
BEGIN
    INSERT INTO CONTRATOS (proyecto_id, proveedor_id, monto, fecha_firma, fecha_termino, estado)
    VALUES (p_proyecto_id, p_proveedor_id, p_monto, p_fecha_firma, p_fecha_termino, p_estado);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_InsertEmpleado(
    IN p_nombre VARCHAR(100),
    IN p_apellido VARCHAR(100),
    IN p_cargo VARCHAR(100),
    IN p_departamento_id INT,
    IN p_fecha_ingreso DATE,
    IN p_salario FLOAT
)
BEGIN
    INSERT INTO EMPLEADOS (nombre, apellido, cargo, departamento_id, fecha_ingreso, salario)
    VALUES (p_nombre, p_apellido, p_cargo, p_departamento_id, p_fecha_ingreso, p_salario);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_InsertPresupuestoMunicipal(
    IN p_municipio_id INT,
    IN p_anio INT,
    IN p_ingresos FLOAT,
    IN p_egresos FLOAT,
    IN p_saldo FLOAT
)
BEGIN
    INSERT INTO PRESUPUESTO_MUNICIPAL (municipio_id, anio, ingresos, egresos, saldo)
    VALUES (p_municipio_id, p_anio, p_ingresos, p_egresos, p_saldo);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_InsertProgramaSocial(
    IN p_nombre VARCHAR(100),
    IN p_departamento_id INT,
    IN p_beneficiarios INT,
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE
)
BEGIN
    INSERT INTO PROGRAMAS_SOCIALES (nombre, departamento_id, beneficiarios, fecha_inicio, fecha_fin)
    VALUES (p_nombre, p_departamento_id, p_beneficiarios, p_fecha_inicio, p_fecha_fin);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_InsertEventoMunicipal(
    IN p_nombre VARCHAR(100),
    IN p_municipio_id INT,
    IN p_fecha DATE,
    IN p_ubicacion VARCHAR(100),
    IN p_descripcion TEXT,
    IN p_tipo VARCHAR(50)
)
BEGIN
    INSERT INTO EVENTOS_MUNICIPALES (nombre, municipio_id, fecha, ubicacion, descripcion, tipo)
    VALUES (p_nombre, p_municipio_id, p_fecha, p_ubicacion, p_descripcion, p_tipo);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_EditMunicipio(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_poblacion INT,
    IN p_area FLOAT,
    IN p_alcalde_actual VARCHAR(100),
    IN p_fecha_fundacion DATE
)
BEGIN
    UPDATE MUNICIPIOS
    SET 
        nombre = p_nombre,
        poblacion = p_poblacion,
        area = p_area,
        alcalde_actual = p_alcalde_actual,
        fecha_fundacion = p_fecha_fundacion
    WHERE municipio_id = p_id;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE proc_DeleteMunicipio(
    IN p_id INT
)
BEGIN
    DELETE FROM MUNICIPIOS
    WHERE municipio_id = p_id;
END$$

DELIMITER ;