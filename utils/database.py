import os
import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
    host='mysql-container2',  # or 127.0.0.1
    user='root',
    password='tnsh76',
    database='gpt3_project'
)

def insert_data(user_input, gpt3_response, sentiment):
    connection = None
    cursor = None
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        query = "INSERT INTO interactions (user_input, gpt_response, sentiment) VALUES (%s, %s, %s)"
        values = (user_input, gpt3_response, sentiment)
        cursor.execute(query, values)
        connection.commit()
    except Exception as e:
        print(f"Error inserting data into the database: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
