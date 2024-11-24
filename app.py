from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Configuración de conexión a la base de datos
db_config = {
    'host': '<MARIADB_EC2_IP>',
    'user': '<marcus>',
    'password': '<12345>',
    'database': 'Users',
    'port': 3306
}

@app.route('/')
def home():
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT Name, LastName FROM Users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', users=users)
    except Exception as e:
        return f"Error connecting to the database: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
