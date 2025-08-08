from sqlite3 import connect
from shared.models import OperationRecord

DB_NAME = 'python_math_api.db'
DB_FOLDER = '../data/sql'
DB_PATH = f"{DB_FOLDER}/{DB_NAME}"


def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    Returns a connection object.
    """
    conn = connect(DB_PATH)
    return conn


def setup_database():
    """
    Sets up the database with necessary tables.

    This function should be called once to initialize the database.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Create a table for storing results if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS api_calls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                operation TEXT NOT NULL,
                input_data TEXT NOT NULL,
                result TEXT NOT NULL
            )
        ''')
        # Duration of the operation can be added later if needed

        conn.commit()


def log_api_call(operation: OperationRecord):
    """
    Logs an API call to the database.

    :param operation: The operation performed (e.g., 'pow', 'factorial',
        'fibonacci').
    :param input_data: The input data used for the operation.
    :param result: The result of the operation.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO api_calls (operation, input_data, result)
            VALUES (?, ?, ?)
        ''', (operation.operation, operation.input_data, operation.result))

        conn.commit()
