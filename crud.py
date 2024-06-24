from sqlalchemy.orm import Session
# from models import Plant, Comments
import schemas, models
import uuid
from rate_comments import CommentRater

def create_plant(db: Session, plant: schemas.PlantCreate, id: int):
    db_plant = models.Plant(**plant.dict(), id=id)
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant


def create_comment(db: Session, comment: schemas.CommentCreate, scores: int):
    db_comment = models.Comments(**comment.dict())
    db.add(db_comment)
    plant = db.query(models.Plant).filter(models.Plant.name == comment.name).first()
    plant.score += scores
    # comment_rater = CommentRater(comment)
    # plant.score += comment_rater.create_score()   
    
    if plant.score == 100:
        result = "max"
    elif plant.score > 60 and plant.score <= 80:
        result = "Lv4"
    elif plant.score > 40 and plant.score <= 60:
        result = "Lv3"
    elif plant.score > 20 and plant.score <= 40:
        result = "Lv2"
    elif plant.score >= 1 and plant.score <= 20:
        result = "Lv1"    
    elif plant.score ==0:
        result = "Lv0"
    
    plant.status = result
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_all_plants(db: Session):
    return db.query(models.Plant).all()

def get_plant_status(db: Session, plant_name: str):
    return db.query(models.Plant).filter(models.Plant.name==plant_name).first()
    
def delete_plant(db: Session, id: int):
    obj = db.query(models.Plant).filter_by(id=id).first()
    db.delete(obj)
    db.commit()


def get_plant_by_status(db: Session, status: str):
    return db.query(models.Plant).filter(models.Plant.status == status).first()

def get_comment(db: Session, name: str):
    return db.query(models.Comments).filter(models.Comments.name == name).all()
# def update_grow_stage(db: Session ):