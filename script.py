import mysql.connector
from mysql.connector import Error

def fetch_notes():
    try:
        # Establish connection to MySQL database
        connection = mysql.connector.connect
        (
            host="localhost",  
            user="someuser",  
            password="mysecretpassword",  
            database="notes_db"  
        )
        
        if connection.is_connected():
            print("Connected to the database.")

            cursor = connection.cursor()
            cursor.execute("SELECT * FROM notes;")
            records = cursor.fetchall()
            
       
            print("\nID\tContent\t\tCompleted")
            print("--------------------------------")
            for row in records:
                print(f"{row[0]}\t{row[1]}\t{row[2]}")
                
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("\nMySQL connection is closed.")
fetch_notes()
