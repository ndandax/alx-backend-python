from sqlalchemy import select, exists, create_engine, Column, String, Numeric
from sqlalchemy.orm import DeclarativeBase, sessionmaker

import csv
import uuid

Base = DeclarativeBase()

DB_HOST = 'localhost'
DB_NAME = 'ALX_prodev'
DB_USER = 'ndandax'

def UserData(Base):
    __tablename__ = 'user_data'
    user_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    age = Column(Numeric, nullable=True)

def connect_db():
    return create_engine(f"mysql+mysqlconnector://{DB_USER}")


def create_database(connection):
    with connection.connect() as conn:
        conn.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")


""" def create_database(connection):
    with connection.connect() as conn:
        conn.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print("✅ Database created or already exists.") """

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    return create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

def create_table(connection):
    """Create user_data table if it does not exist."""
    Base.metadata.create_all(connection)
    print("✅ Table created or already exists.")

def insert_data(connection, data):
    """Insert data if email does not already exist."""
    Session = sessionmaker(bind=connection)
    session = Session()
    try:
        for name, email, age in data:
            exists_query = session.query(exists().where(UserData.email == email)).scalar()
            if exists_query:
                print(f"⏩ Skipping existing email: {email}")
                continue

            user = UserData(name=name, email=email, age=age)
            session.add(user)
        session.commit()
        print("✅ Data inserted.")
    finally:
        session.close()

# --------------------
# CSV Reader
# --------------------

def read_csv(file_path):
    """Read CSV and return data as list of tuples."""
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append((row['name'], row['email'], row['age']))
    return data

# --------------------
# Generator: Stream DB Rows One-by-One
# --------------------

def stream_users(connection):
    """Generator that yields users one-by-one from the DB."""
    Session = sessionmaker(bind=connection)
    session = Session()
    try:
        query = session.query(UserData)
        for user in query:
            yield user
    finally:
        session.close()

# --------------------
# Run the Full Process
# --------------------

if __name__ == "__main__":
    server_conn = connect_db()
    create_database(server_conn)

    db_conn = connect_to_prodev()
    create_table(db_conn)

    sample_data = read_csv("user_data.csv")
    insert_data(db_conn, sample_data)

    print("\n🎯 Streaming data from DB:")
    for user in stream_users(db_conn):
        print(f"- {user.name} ({user.email}), Age: {user.age}")

