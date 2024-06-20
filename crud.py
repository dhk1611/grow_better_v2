from sqlalchemy.orm import Session
# from models import Plant, Comments
import schemas, models
import uuid


def create_plant(db: Session, plant: schemas.PlantCreate, id: int):
    db_plant = models.Plant(**plant.dict(), id=id)
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant

# def create_comment(db: Session, comment: schemas.CommentCreate, given_comment: schemas.PlantCreate):
#     db_comment = models.Comments(**comment.dict())
#     db_plant = models.Plant(**score.dict())
#     given_comment = given_comment + 1
#     db.add(db_comment)
#     db.add(db_plant)
#     db.commit()
#     db.refresh(db_comment)
#     db.refresh(db_plant)
#     return db_comment, db_plant
def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comments(**comment.dict())
    db.add(db_comment)

    db.commit()
    db.refresh(db_comment)

    return db_comment

def get_all_plants(db: Session):
    return db.query(models.Plant).all()

def get_plant_status(db: Session, plant_name: str):
    return db.query(models.Plant).filter(models.Plant.name==plant_name).first()
    
def delete_plant(db: Session, id: int):
    obj = db.query(models.Plant).filter(id=id).first()
    db.delete(obj)
    db.commit()


def get_plant_by_status(db: Session, status: str):
    return db.query(models.Plant).filter(models.Plant.status == status).first()

def get_comment(db: Session, name: str):
    return db.query(models.Comments).filter(models.Comments.name == name).first()
# def update_grow_stage(db: Session ):