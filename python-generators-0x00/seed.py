import mysql.connector
import csv
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

def db_connection():
    """Connect to MySQL server"""
    try:
        return mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            auth_plugin='mysql_native_password'
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def create_database(connection):
    """Create ALX_prodev database if not exists"""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

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

def create_table(connection):
    """Create user_data table if not exists"""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(10,2) NOT NULL,
                INDEX (user_id)
            )
        """)
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

def insert_data(connection, filename):
    """Insert data from CSV file"""
    try:
        cursor = connection.cursor()
        
        # Check if table is empty
        cursor.execute("SELECT COUNT(*) FROM user_data")
        if cursor.fetchone()[0] > 0:
            print("Data already exists in table")
            return
            
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (str(uuid.uuid4()), row['name'], row['email'], float(row['age'])))
        
        connection.commit()
        cursor.close()
        print("Data inserted successfully")
    except (mysql.connector.Error, FileNotFoundError) as err:
        print(f"Error inserting data: {err}")