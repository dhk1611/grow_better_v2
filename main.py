from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
import models, crud, schemas
from rate_comments import CommentRater

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow CORS for all origins (for simplicity)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Plant Comment API"}


@app.post("/plants/")
def create_plant(
    id: int, plant: schemas.PlantCreate, db: Session = Depends(get_db)
): 
    return crud.create_plant(db=db, plant=plant, id=id)

@app.post("/plants/comment/")
def comment_on_plant(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    
    return crud.create_comment(db=db, comment=comment)



@app.get("/plants/all")
def get_all_plants(db: Session = Depends(get_db)):
    return crud.get_all_plants(db=db)
    

    
@app.get("/plants/status/{plant_name}")
def get_plants_status(plant_name: str, db: Session = Depends(get_db)):
    return crud.get_plant_status(plant_name = plant_name, db=db)


@app.delete("/plants/status/{plant_name}")
def delete_plants(
    id=id, db: Session = Depends(get_db)
    ):
    return crud.delete_plant(id=id, db=db)

@app.get("/plants/comments/{plant_name}")
def get_comments_by_plant(name: str, db: Session = Depends(get_db)):

    return crud.get_comment(name=name, db=db)


@app.get("/plants/growth_stage/{growth_stage}")
def get_plants_by_growth_stage(status: str, db: Session = Depends(get_db)):
    return crud.get_plant_by_status(status=status, db=db)

