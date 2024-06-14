from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base, engine
import uuid

'''

DB Tables

'''
class Plant(Base):          #Plant라는 테이블 
    __tablename__="plants"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    score = Column(Integer)
    given_comment = Column(Integer)
    
    comment_relation= relationship("Comments", back_populates="plant_relation")

class Comments(Base):
    __tablename__="comments"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    comment = Column(String)
    plant_id = Column(Integer, ForeignKey(Plant.id))
    
    plant_relation= relationship("Plant", back_populates="comment_relation")
    
Base.metadata.create_all(bind=engine)
