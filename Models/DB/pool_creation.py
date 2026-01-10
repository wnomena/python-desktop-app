from sqlalchemy import Engine, create_engine
import os

class Sqlite_Engine:
    engine:Engine = None
    def __init__(self):
        print(os.path.abspath("."))
        self.engine = create_engine("sqlite:///index.db")


class Mysql_Engine(Sqlite_Engine):
    _engine:Engine = None
    def __init__(self,):
        self._engine = create_engine("mysql+pymysql://root:root@localhost:3306/local_caponmada")
