from datetime import datetime
from faker import Faker
from faker.providers import internet, misc, address, date_time
fake = Faker()
fake.add_provider(internet)
fake.add_provider(misc)
fake.add_provider(address)
fake.add_provider(date_time)

#print(fake.image_url(width=100,height=100))

#print(fake.unique.first_name())

#print(fake.last_name())

#print(fake.email())

#print(fake.first_name())

#print(fake.random_int(min=1, max=501))

#print(uuid.uuid1())


def data_personales(limite):
    for id in range(1, limite):
        nombre = fake.first_name()
        apellido = fake.last_name()
        identificador = fake.uuid4()
        departamento_id = fake.random_int(min=1, max=4)
        if id == 1:
            supervisor_id = "null"
        else:
            supervisor_id = fake.random_int(min=-10, max=id-1)
            # haremos que el numero random pueda ir desde el -10 hasta < id actual, luego, si el numero es menor o igual a 0 entonces el empleado no tendra supervisor (null)
            if supervisor_id <= 0:
                supervisor_id = "null"
        print('INSERT INTO PERSONALES VALUES ({}, "{}", "{}", "{}", {}, {});'.format(
            id, nombre, apellido, identificador, departamento_id, supervisor_id))
def data_muchos(alumnos):
    alumnos += 1
    for id in range(1, alumnos):
        matricula = fake.random_int(min=1000, max=5000)
        nombre = fake.first_name()
        apellido = fake.last_name()
        localidad = fake.city()
        fecha_nacimiento = fake.date_between_dates(date_start=datetime(
            1992, 12, 30), date_end=datetime(2000, 7, 12))
        print('INSERT INTO alumnos VALUES({}, "{}", "{}", "{}", "{}", "{}");'.format(
            id, matricula, nombre, apellido, localidad, fecha_nacimiento))

    cursos = ["MATEMATICA", "COMUNICACION",
              "INFORMATICA", "PSICOLOGIA", "FILOSOFIA"]
    id_curso = 1
    for curso in cursos:
        fecha_inicio = fake.date_between_dates(date_start=datetime(
            2021, 3, 1), date_end=datetime(2021, 12, 10))
        fecha_fin = fake.date_between_dates(
            date_start=fecha_inicio, date_end=datetime(2021, 12, 10))
        print('INSERT INTO cursos VALUES ({},"{}","{}","{}");'.format(
            id_curso, curso, fecha_inicio, fecha_fin))
        id_curso += 1

    registro_alumno_curso = []
    for ciclo in range(1, alumnos*2):
        alumno = fake.random_int(min=1, max=alumnos-1)
        curso = fake.random_int(min=1, max=len(cursos))
        if [alumno, curso] in registro_alumno_curso:
            ciclo -= 1
        else:
            registro_alumno_curso.append([alumno, curso])
            print('INSERT INTO alumnos_cursos VALUES ({},{});'.format(alumno, curso))


data_muchos(100)