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

def get_all_plants(db: Session):
        return db.query(models.Plant).all()
    
def delete_plant(db: Session, plant_name: str):
    obj = db.query(models.Plant).filter_by(plant_name=plant_name).first()
    db.delete(obj)
    db.commits()
