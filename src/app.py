import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials
DB_USER = os.getenv('DB_USER', 'ejemplo').strip()
DB_PASS = os.getenv('DB_PASSWORD', 'ejemplo').strip()
DB_HOST = os.getenv('DB_HOST', 'localhost').strip()
DB_NAME = os.getenv('DB_NAME', 'ejemplo').strip()
DB_PORT = os.getenv('DB_PORT', '5432').strip()

# Create engine
CONN_STRING = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(CONN_STRING, isolation_level="AUTOCOMMIT")

# Execute SQL files
def run_sql_file(file_path):
    with open(file_path, 'r') as f:
        sql = f.read()
    with engine.begin() as conn:
        conn.execute(text(sql))

# Main workflow
try:
    # Setup database schema
    run_sql_file("src/sql/drop.sql")
    run_sql_file("src/sql/create.sql")
    run_sql_file("src/sql/insert.sql")
    
    # Display results
    publishers = pd.read_sql("SELECT * FROM publishers", engine)
    print(publishers)
    print(f"\nSuccess! Displayed {len(publishers)} publishers")

except Exception as e:
    print(f"Error: {e}")