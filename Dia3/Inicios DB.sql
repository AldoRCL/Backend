CREATE DATABASE pruebas;
USE pruebas;

CREATE TABLE alumnos(
id int primary key not null auto_increment,
nombre varchar(40),
apellido varchar(25),
sexo varchar(10),
numero_emergencia int,
religion varchar(10),
fecha_nacimiento date
);

CREATE TABLE habilidades(
id int auto_increment not null unique primary key,
descripcion varchar(100),
nivel varchar(15),
alumno_id int not null
);

CREATE TABLE hbailidades_alumnos(
id int auto_increment not null unique primary key,
alumno_id int not null,
habilidad_id int not null,
foreign key (habilidad_id) references habilidades(id),
foreign key (alumno_id) references alumnos(id)
);

INSERT INTO alumnos (nombre, apellido, sexo, numero_emergencia, religion, fecha_nacimiento) 
			VALUES ("Eduardo", "de rivero", "M", 974207075, "CATOLICO", "1990-08-14");
INSERT INTO alumnos (nombre, apellido, sexo, numero_emergencia, religion, fecha_nacimiento) 
			VALUES ("Fiorella","Ccalla", "F",96564587, "ATEO", "1993-01-07");
INSERT INTO alumnos (nombre, apellido, sexo, numero_emergencia, religion, fecha_nacimiento) 
			VALUES ("Matheus","Peña", "M",92219087, "EVANGELICO", "1989-04-06");
            
INSERT INTO alumnos VALUES (2,"Aldo","Cotrina Lozano", "M",92219087, "CATOLICO", "1990-08-14");
            
select * from alumnos;
select * from alumnos where nombre = "Eduardo";
DROP TABLE alumnos;

