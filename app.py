import sys
import mariadb

try:

    conn = mariadb. connect(
    user="marcus",
    password="12345" ,
    host="54.205.101.113",
    port=3306,
    database="Users"

    )
except mariadb. Error as e:
    print(f"Error connecting to MariaDB Platform:
    sys.exit(1)

# Get Cursor
cur = conn. cursor ()