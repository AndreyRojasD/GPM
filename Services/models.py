from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, create_engine
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "../gpm.db")
ENGINE_NAME = "sqlite" # change this to engine name
engine = create_engine(f"{ENGINE_NAME}:///{FILE_PATH}")
Base = declarative_base()

Session = sessionmaker(engine)
session = Session()

def create_session():
    return sessionmaker(engine)()

def drop_all():
    Base.metadata.drop_all(engine)

def create_all():
    Base.metadata.create_all(engine)

def reset():
    drop_all()
    create_all()

def add(_object, session=session):
    session.add(_object)

def commit(session=session):
    session.commit()

def save(_object,session=session):
    session.add(_object)
    session.commit()

def save_many(*objects, session = session):
    session.add_all(objects)
    session.commit()

def get_all(_object,session=session):
    return session.query(_object).all()

def filter(condition,*fields_or_class,session=session):
    return session.query(*fields_or_class).filter(condition)

def query(*fields_or_class,session=session):
    return session.query(*fields_or_class)




# Create your models here
class Profile(Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String, unique=True)
    user_name = Column(String)
    email = Column(String)
    pull_rebase = Column(String)
    ssh_key_name = Column(String)
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, user_name: {self.user_name}, email: {self.email}, pull_rebase: {self.pull_rebase}, ssh_key_name: {self.ssh_key_name}"
    