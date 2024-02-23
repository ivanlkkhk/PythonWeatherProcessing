#################################################################
# Description: Project - Part 2 - Database
# Author: Kwok Keung Lai
# Date: Oct 15, 2023
# Usage: This module used to manage database connection,
#        and cursor. which allow other function to use it by
#        context management.
#################################################################
"""This module used to manage database connection,
        and cursor. which allow other function to use it by
        context management."""
import sqlite3

class DBCM:
    """ Class for manage database connection and cursor, allow
        use it by context management."""
    def __init__(self, db_name):
        """ Consturctor for initialize the database name."""
        self.db_name = db_name

    def __enter__(self):
        """
        Enter the context manager, establishing a connection and returning a cursor.
        Returns:
            A cursor for executing database operations.
        """
        self.db_conn = sqlite3.connect(self.db_name)
        self.db_cursor = self.db_conn.cursor()
        return self.db_cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context manager, committing changes and closing the connection.
        Args:
            exc_type: Type of exception (if any).
            exc_val: Exception value (if any).
            exc_tb: Exception traceback (if any).
        """
        if exc_type is not None:
            print(f"An error occurred: {exc_type}: {exc_val}")
        try:
            self.db_conn.commit()
        except Exception as commit_error:
            print(f"Error while committing changes: {commit_error}")
        self.db_cursor.close()
        self.db_conn.close()
