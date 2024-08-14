from faker import Faker


def data_fake():
    # Crear una instancia de Faker con localización para México
    fake = Faker('es_MX')

    # Generar un nombre completo falso
    first_name = fake.first_name()
    second_name = fake.first_name()
    firs_last_name = fake.last_name()
    second_last_name = fake.last_name()

    # Generar una fecha de nacimiento falsa
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)

    # Generar un CURP falso
    curp = fake.curp()

    # Generar un RFC falso
    rfc = fake.rfc()
    # Generar un identificacion falsa
    cedula = fake.ssn()



    return rfc, cedula, first_name,second_name, firs_last_name, second_last_name, birthday, curp