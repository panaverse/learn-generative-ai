from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import OperationalError

import time
import os
from dotenv import load_dotenv, find_dotenv

_: bool = load_dotenv(find_dotenv())

DB_URL = os.environ.get("DB_URL")

if DB_URL is None:
    raise Exception("No DB_URL environment variable found")

# Enable connection pooling with pessimistic testing
engine = create_engine(DB_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency with retry mechanism for OperationalError
def get_db():
    attempt_count = 0
    max_attempts = 3
    retry_delay = 2  # seconds

    while attempt_count < max_attempts:
        db = SessionLocal()
        try:
            yield db
            break  # If successful, exit the loop
        except OperationalError as e:
            print(f"SSL connection error occurred: {e}, retrying...")
            attempt_count += 1
            time.sleep(retry_delay)
        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            break
        finally:
            db.close()

        if attempt_count == max_attempts:
            print("Failed to connect to the database after several attempts.")

