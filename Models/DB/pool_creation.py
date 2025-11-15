from sqlalchemy import create_engine
class Engine:
    def __init__(self):
        self._engine = create_engine(f"mysql+pymysql://root:root@localhost:3306/local_caponmada")