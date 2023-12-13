from models import TODOCreate, TODOUpdate
from db_models import create_session, TodoRow
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session


class TodoDomain():
    def get_db_connection(self)->tuple[Engine, Session]:
        return create_session("")

    def create_todo(self, todo: TODOCreate) -> TODOUpdate:
        try:
            db: tuple[Engine, Session] = self.get_db_connection()
            todo_row = TodoRow(text=todo.text, is_completed=False)
            # saving todo
            db[1].add_all([todo_row])
            db[1].commit()
            return TODOUpdate(id=todo_row.id, text=todo_row.text, completed=todo_row.is_completed)
        except:
            db[1].rollback()
            db[1].close()
            raise
        
            
    
    def update_todo(self, todo: TODOUpdate) -> TODOUpdate:
        db: tuple[Engine, Session] = self.get_db_connection()
        todo_row = TodoRow(text=todo.text, is_completed=False)
        # saving todo
        db[1].add_all([todo_row])
        db[1].commit()
        return TODOUpdate(id=todo_row.id, text=todo_row.text, completed=todo_row.is_completed)