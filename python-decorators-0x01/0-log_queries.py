import sqlite3
import functools
from datetime import datetime

#### decorator to log SQL queries

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query from the function arguments
        # Check if 'query' is passed as a keyword argument
        if 'query' in kwargs:
            query = kwargs['query']
        # Check if 'query' is the first positional argument
        elif args and len(args) > 0:
            query = args[0]  # Assumes query is the first argument
        else:
            query = "No query found"
        
        # Log the SQL query with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Executing SQL query: {query}")
        
        # Execute the original function
        return func(*args, **kwargs)
    
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
