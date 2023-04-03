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
        user_id = 123
        surname = "Berzina"

        update_query = """
UPDATE
    User_information
SET
    surname = %s
WHERE
   name = "%s";
""" % (
            user_id,
            surname
        )
        with connection.cursor() as cursor:
            cursor.execute(update_query)
            connection.commit()
except Error as e:
    print(e)