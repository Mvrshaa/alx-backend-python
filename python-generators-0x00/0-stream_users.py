import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_prodev():
    """Connect to ALX_prodev database"""
    try:
        return mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database='ALX_prodev',
            auth_plugin='mysql_native_password'
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None

def stream_users():
    """Generator that streams users one by one"""
    connection = connect_to_prodev()
    if not connection:
        return
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
    
    cursor.close()
    connection.close()