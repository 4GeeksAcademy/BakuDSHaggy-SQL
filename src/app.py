import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1) Connect to the database with SQLAlchemy
# Create DB connection
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Connect to PostgreSQL
engine = create_engine(f"postgresql://{DB_USER} : {DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Execute SQL files
def run_sql_file(file_path):
    """Execute all SQL commands in a file"""
    with open(file_path, 'r') as f:
        sql = f.read()

    
    with engine.begin() as conn:
        for command in sql.split(';'):
            if command.strip():
                conn.execute(text(command))



try:
# 2) Create the tables
    run_sql_file("src/sql/create.sql")
    print("Tables have been created")
# 3) Insert data
    run_sql_file("src/sql/insert.sql")
    print("Data has been inserted")
# 4) Use Pandas to read and display a table
    publishers = pd.read_sql("SELECT * FROM publishers", engine)
    print("\n Publishers Table:")
    print(publishers)

except Exception as e:
    print(f"Error: {e}")
