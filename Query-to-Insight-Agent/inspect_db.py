
import sqlite3
import os

db_path = 'datatechcon.db'

if not os.path.exists(db_path):
    print(f"Database file '{db_path}' does not exist.")
else:
    print(f"Database file '{db_path}' found.")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        if not tables:
            print("No tables found in the database.")
        else:
            print("Tables found:")
            for table in tables:
                print(f"- {table[0]}")
                
                # Get columns for each table
                cursor.execute(f"PRAGMA table_info({table[0]})")
                columns = cursor.fetchall()
                for col in columns:
                    print(f"  - {col[1]} ({col[2]})")
                    
        conn.close()
    except Exception as e:
        print(f"Error reading database: {e}")
