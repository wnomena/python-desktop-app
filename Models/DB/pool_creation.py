from sqlalchemy import Engine, create_engine
import os

class Sqlite_Engine:
    engine:Engine = None
    def __init__(self):
        print(os.path.abspath("."))
        self.engine = create_engine("sqlite:///index.db")

