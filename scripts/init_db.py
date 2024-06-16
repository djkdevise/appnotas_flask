import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS agenda_notas_medicas")
cursor.execute("USE agenda_notas_medicas")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fecha DATE NOT NULL,
        semana INT NOT NULL,
        dia VARCHAR(255) NOT NULL,
        nota TEXT NOT NULL
    )
""")

connection.commit()
cursor.close()
connection.close()
