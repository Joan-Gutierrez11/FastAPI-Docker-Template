from src.config import db
from typing import Generator, Annotated

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from fastapi import Depends

engine = create_engine(db.url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DeclarativeBaseModel = declarative_base()

def get_db_session() -> Generator[Session, None, None]:
    """
    Create session for database
    """
    global session

    db_conn = session()
    try:
        yield db_conn
    finally:
        db_conn.close()
        

SessionDependency = Annotated[Session, Depends(get_db_session)]
