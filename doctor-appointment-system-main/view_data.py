import sqlite3
from tabulate import tabulate

db_path = 'instance/clinic.db'

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("=" * 80)
    print("DATABASE TABLES")
    print("=" * 80)
    
    for table in tables:
        table_name = table[0]
        print(f"\n\n📋 TABLE: {table_name}")
        print("-" * 80)
        
        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [col[1] for col in cursor.fetchall()]
        
        # Get all rows
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        if rows:
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            print(f"Total rows: {len(rows)}")
        else:
            print("(No data)")
    
    conn.close()
    print("\n" + "=" * 80)
    
except Exception as e:
    print(f"Error: {e}")
