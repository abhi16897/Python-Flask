from sqlalchemy import create_engine,Column, Integer,String,event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.event.api import listens_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
engine=create_engine('sqlite:///Company.db',echo=True)

Session=sessionmaker(bind=engine)
session=Session()

Base=declarative_base() 

class Student(Base):
   __tablename__='student'
   sd_id=Column(Integer,primary_key=True,autoincrement=True)
   name=Column(String(50))
   age=Column(Integer)
   grade=Column(String(50))

class Log_Table(Base):
   __tablename__='logtable'
   id=Column(Integer,primary_key=True,autoincrement=True)
   student_id=Column(Integer,ForeignKey(Student.sd_id))
   updated_for=Column(String(50))
   action=Column(String(20))

Base.metadata.create_all(engine)



@event.listens_for(Student,"after_insert")
def log_after_insert(mapper,connection,target):
   log1=Log_Table(student_id=target.sd_id,updated_for="Chala Chusam",action="Inserted")
   session.add(log1)

student1=Student(name="Abhishek",age=27,grade="Fifth")
session.add(student1)
session.commit()

students=session.query(Student).order_by(Student.name)
for s in students:
   print(f"Student Name is :{s.name}")

students=session.query(Log_Table).all()
for s in students:
   print(f"Sudent Id is {s.student_id} Updated for {s.updated_for}  and action is  {s.action}")

