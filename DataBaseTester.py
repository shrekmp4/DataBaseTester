from faker import Faker
import random
import sqlite3

fake = Faker()

def create_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'address': fake.address(),
            'birthdate': fake.date_of_birth().strftime('%Y-%m-%d'),
            'company': fake.company(),
        }
        data.append(record)
    return data

def create_database(data):
    conn = sqlite3.connect('test_database.db')
    cursor = conn.cursor()

    # Crear una tabla llamada 'users'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            birthdate DATE,
            company TEXT
        )
    ''')

    # Insertar datos en la tabla 'users'
    for record in data:
        cursor.execute('''
            INSERT INTO users (name, email, phone, address, birthdate, company)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (record['name'], record['email'], record['phone'], record['address'], record['birthdate'], record['company']))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Crear 100 registros de datos aleatorios
    fake_data = create_fake_data(100)

    # Crear la base de datos con los datos generados
    create_database(fake_data)

    print("Base de datos 'test_database.db' creada con éxito.")
