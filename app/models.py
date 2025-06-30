from sqlalchemy import Column, Integer, String, Boolean, Date
from .database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    middlename = Column(String, nullable=True)
    lastname = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    password = Column(String, nullable=False)
    club_name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    parent_name = Column(String, nullable=True)
    parent_email = Column(String, nullable=True)
    parent_phone = Column(String, nullable=True)
    parent_consent = Column(Boolean, nullable=True)

    terms_accepted = Column(Boolean, default=False)
    data_consent = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
