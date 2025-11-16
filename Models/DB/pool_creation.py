from sqlalchemy import create_engine
class Mysql_Engine:
    def __init__(self):
        self._engine = create_engine("mysql+pymysql://root:root@localhost:3306/local_caponmada")

class Sqlite_Engine:
    def __init__(self):
        self.engine = create_engine("sqlite3://")