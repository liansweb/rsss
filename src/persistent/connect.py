from src.start import script
logger = script.logger

def connect(db_name):
    import sqlite3
    
    
    """
    Connect to the SQLite database with the given database name.

    Args:
    - db_name: The path/name of the database file.

    Returns:
    - A connection object to the SQLite database.

    Raises:
    - sqlite3.Error: If an error occurs while connecting to the database.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        logger.info(f"[*] Successfully connected to database {db_name} with sqlite version {sqlite3.sqlite_version}")
        return conn
    except sqlite3.Error as e:
        logger.error(f"[*] An error occurred: {e}")
        if conn:
            conn.close()
        raise  # Re-raise the exception to be handled by the caller

