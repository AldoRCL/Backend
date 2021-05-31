CREATE DATABASE zapateria;
USE zapateria;
CREATE TABLE categorias(
	id int not null unique auto_increment,
    nombre varchar (50),
    abbr varchar(10),
    imagen text
);

CREATE TABLE productos(
id int not null unique auto_increment,
nombre varchar(50),
precio decimal(5,2),

disponible boolean,
categoria_id int,

constraint relacion_producto_categoria
foreign key (categoria_id) references categorias(id)
);



INSERT INTO categorias (nombre, abbr, imagen) VALUES ("ZAPATO", "ZAP", "url11");
INSERT INTO categorias (nombre, abbr, imagen) VALUES ("ZAPATILLA","ZAPT","url12");
INSERT INTO categorias (nombre, abbr, imagen) VALUES ("BOTIN","BOT","url13");
INSERT INTO categorias (nombre, abbr, imagen) VALUES ("BOTA", "BOT", "url14");
#INSERT INTO categorias (nombre, abbr, imagen) VALUES ("BOTA","BOTA","url15");

INSERT INTO PRODUCTOS (nombre, precio, disponible, categoria_id) VALUES("ZAPATO VERANO", 99.90, true, 1);
INSERT INTO PRODUCTOS (nombre, precio, disponible, categoria_id) VALUES("ZAPATO HOMBRE", 120.00, true, 1);
INSERT INTO PRODUCTOS (nombre, precio, disponible, categoria_id) VALUES("ZAPATO MUJER", 199.00, false, 1);
INSERT INTO PRODUCTOS (nombre, precio, disponible, categoria_id) VALUES("ZAPATILLA TREKKIN HOMBRE", 189.90, true, 2);
INSERT INTO PRODUCTOS (nombre, precio, disponible, categoria_id) VALUES("ZAPATILLA RUN MUJER", 220.00, true, 2);
INSERT INTO PRODUCTOS (nombre, precio, disponible, categoria_id) VALUES("ZAPATILLA OFFROAD MUJER", 320.89, true, 2);
INSERT INTO PRODUCTOS (nombre, precio, disponible, categoria_id) VALUES("BOTIN TACO 4", 520.00, true, 3);
INSERT INTO PRODUCTOS (nombre, precio, disponible, categoria_id) VALUES("BOTA TACO 10", 710, false, 4);

SELECT *  FROM categorias where nombre LIKE '%A%';
-- EJERCICIOS --
-- DEVOLVER TODOS LOS PRODUCTOS CUYO PRECIO SEA ENTRE 100 y 250 soles
SELECT *  FROM productos where (precio >= 100 and precio<=250);
-- DEVOLVER TODOS LOS PRODUCTOS DISPONIBLES
SELECT *  FROM productos where disponible = true;
-- DEVOLVER TODOS LOS PRODUCTOS QUE SEAN PARA HOMBRE
SELECT *  FROM productos where nombre LIKE "%HOMBRE";
-- DEVOLVER TODOS LOS PRODUCTOS QUE TENGAN TACO 4
SELECT *  FROM productos where nombre LIKE "%TACO 4";

SELECT *  FROM productos where categoria_id = 2;

SELECT *  FROM productos where (precio > 500 and disponible = false);

SELECT *  FROM productos where (categoria_id = 2 or categoria_id = 4);
-- FIN EJERCICIOS --
INSERT INTO CATEGORIAS (nombre, abbr, imagen) VALUE ("BEBES","BEB", "url5");

SELECT * FROM categorias INNER JOIN productos ON categorias.id = productos.categoria_id;
SELECT * FROM categorias LEFT JOIN productos ON categorias.id = productos.categoria_id;
SELECT * FROM categorias RIGHT JOIN productos ON categorias.id = productos.categoria_id;

SELECT cat.nombre AS nombrecito
FROM categorias AS cat JOIN productos AS prod ON cat.id = prod.categoria_id
WHERE cat.nombre = "ZAPATO";

UPDATE CATEGORIAS SET abbr = "BOT" WHERE ID = 4;









drop table productos;
drop table categorias;

SELECT * FROM categorias;
SELECT * FROM productos;
