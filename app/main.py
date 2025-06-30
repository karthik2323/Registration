from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.database import engine, get_db
from passlib.context import CryptContext

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post("/v1/player/register", response_model=schemas.PlayerResponse)
def register_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    existing_player = db.query(models.Player).filter(models.Player.email == player.email).first()
    if existing_player:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(player.password)

    db_player = models.Player(
        firstname=player.firstname,
        middlename=player.middlename,
        lastname=player.lastname,
        dob=player.dob,
        email=player.email,
        phone=player.phone,
        club_name=player.club_name,
        country=player.country,
        parent_name=player.parent_name,
        parent_email=player.parent_email,
        parent_phone=player.parent_phone,
        parent_consent=player.parent_consent,
        terms_accepted=player.terms_accepted,
        data_consent=player.data_consent,
        password=hashed_password,
        is_active=True
    )
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player
