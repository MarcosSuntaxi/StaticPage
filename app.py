from flask import Flask, render_template
import mariadb

app = Flask(__name__)

# Configuración de conexión a la base de datos
db_config = {
    'host': '54.205.101.113',
    'user': 'marcus',
    'password': '12345',
    'database': 'Users',
    'port': 3306
}

@app.route('/')
def home():
    try:
        # Conexión a la base de datos
        conn = mariadb.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT Name, LastName FROM Users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Renderiza la plantilla con los datos obtenidos
        return render_template('index.html', users=users)
    except mariadb.Error as e:
        return f"Error connecting to the database: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
