from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session

"""
table todo
    - id int pk
    - text str
    - is_completed BOOLEAN
"""

def create_session(connectionStr: str)->tuple[Engine, Session]:
    engine: Engine = create_engine(
        connectionStr,
        echo= True
    )
    Session = sessionmaker(bind=engine)
    db: Session = Session()
    return (engine, db) 

def create_tables(engine: Engine):
    Base.metadata.create_all(bind=engine)


class Base(DeclarativeBase):
    pass


class TodoRow(Base):
    __tablename__ = 'todo'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text:Mapped[str] = mapped_column(nullable=False)
    is_completed:Mapped[bool] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"<Todo {self.id}>"