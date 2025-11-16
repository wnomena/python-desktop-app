from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


MYSQL_URL = "mysql+pymysql://root:root@localhost:3306/local_caponmada"

engine = create_engine(MYSQL_URL,echo=False)

session = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
