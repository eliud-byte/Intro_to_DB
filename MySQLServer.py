from db import DB_CONFIG
import mysql.connector

def create_database():
    """
    This function takes a name as argument and creates a database 
    of that name.
    
    :param db_name: This name of the database to be created.
    :type db_name: str
    """
    try:
        mydb = mysql.connector.connect(**DB_CONFIG)
        print("Database server connection successful!")
        #mydb = None
        # Create SQL query
        create_db_query = f"CREATE DATABASE IF NOT EXISTS alx_book_store"

        # Execute query
        with mydb.cursor() as cursor:
            cursor.execute(create_db_query)
            
            # Commit the query
            mydb.commit()
            print(f"\nDatabase 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"\nFailed to connect to MySQL server: {e}")

    except Exception as e:
        print(f"\n An unexpected error occurred: {e}")
    
    finally:
        # Close the database connection
        mydb.close()
        print("\nDatabase connection is closed.")

# Usage
if __name__ == "__main__":
    create_database()