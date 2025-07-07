import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""

def log_queries(func):
   @functools.wraps(func)
   def wrapper(*args, **kwargs):
      args_repr = [repr(a) for a in args]
      kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
      ##print(args_repr)
      print(kwargs_repr)
      func(*args, **kwargs)
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

