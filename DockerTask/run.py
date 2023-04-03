import os
import time
import mysql.connector

def connect_to_mysql():
    start_time = time.time()
    timeout = 60

    while time.time() - start_time < timeout:
        try:
            connection = mysql.connector.connect(
                host="mysql",
                user="Evija",
                password="sgt2023",
                database="db"
            )
            print("Connected to MySQL")
            return connection
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
            time.sleep(5)

    raise Exception(f"Could not connect to MySQL within {timeout} seconds")

if name == "main":
    try:
        while True:
            with connect_to_mysql() as connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("SELECT VERSION()")
                    result = cursor.fetchone()
                    print(f"!!MySQL version!!: {result}")
                finally:
                    cursor.close()

            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping script")