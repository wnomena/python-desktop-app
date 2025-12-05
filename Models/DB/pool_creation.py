from sqlalchemy import Engine, create_engine
class Mysql_Engine:
    _engine:Engine = None
    def __init__(self):
        self._engine = create_engine("mysql+pymysql://root:root@localhost:3306/local_caponmada")

class Sqlite_Engine:
    engine:Engine = None
    def __init__(self):
        self.engine = create_engine("sqlite3://")