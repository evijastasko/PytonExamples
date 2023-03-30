from mysql.connector import connect, Error
from decouple import config

try:
    configValue = {
        "host": "localhost",
        "user": config("username"),
        "password": config("password"),
        "database": "system_audit"
    }
    with connect(**configValue) as connection:
        with connection.cursor() as cursor:
            select_audit_query = "SELECT * FROM User_information"
            with connection.cursor() as cursor:
                cursor.execute(select_audit_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)

except Error as e:
    print(e)

