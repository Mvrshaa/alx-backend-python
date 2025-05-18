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

def stream_users_in_batches(batch_size):
    """Generator that streams users in batches"""
    connection = connect_to_prodev()
    if not connection:
        return
    
    offset = 0
    while True:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        batch = cursor.fetchall()
        cursor.close()
        
        if not batch:
            connection.close()
            break
            
        yield batch
        offset += batch_size

def batch_processing(batch_size):
    """Process batches to filter users over 25"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)