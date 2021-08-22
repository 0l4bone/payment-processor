#coding=utf-8
import sys
from sqlalchemy import create_engine, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import joinedload, subqueryload

password="123456"
username="root"
hostname="127.0.0.1"
port="3306"

engine = create_engine('mysql://{}:{}@{}:{}/test?charset=utf8'.format(username, password, hostname, port), echo=True)

session = Session(engine)

Base = declarative_base()

class Sql_test(Base):
    __tablename__ = 'sql_test'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255)),
    des = Column(String(255))

print(session.query(Sql_test).group_by(sys.argv[1]).all())