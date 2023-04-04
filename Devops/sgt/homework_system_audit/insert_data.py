from mysql.connector import connect, Error
from decouple import config

try:
    configValue = {
        "host": "127.0.0.1",
        "user": config("username"),
        "password": config("password"),
        "database": "system_audit",
        "port": "3306"
    }
    with connect(**configValue) as connection:
        insert_Audit_log = """
            INSERT INTO Audit_log
            (date,time)
            VALUES (%s, %s)
            """
        audit_log_data = [
            ("01.04.2023", "12:10"),
            ("02.04.2023", "13:10")
]
    with connection.cursor() as cursor:
        cursor.executemany(insert_Audit_log, audit_log_data)
        connection.commit()

except Error as e:
    print(e)