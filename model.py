from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()





class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    topic = Column(String)
    user_id = Column(Integer)

    def __str__(self):
        return "name: " + self.name + " topic: " + self.topic + " user_id: " + str(self.user_id)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    email = Column(String(255), unique=True)
    password_hash = Column(String(255))  
    erea = Column(String)
    art = Column(String)



    def __str__(self):
        return "name: " + self.name + " email: " + self.email + " pass: " + self.password_hash

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)






engine = create_engine('sqlite:///webdata.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()