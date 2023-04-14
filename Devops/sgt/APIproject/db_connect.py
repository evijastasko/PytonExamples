import mysql.connector

def create_connection():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='sgt2023',
            database ='aws_instances'
        )