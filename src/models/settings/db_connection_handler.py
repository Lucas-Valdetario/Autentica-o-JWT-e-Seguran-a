import sqlite3
from sqlite3 import Connection

class __DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> Connection:
        self.__conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        
    def get_connection(self) -> Connection:
        if self.__conn is None:
            self.connect()
        return self.__conn

db_connection_handler = __DbConnectionHandler()