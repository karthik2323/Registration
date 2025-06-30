from pydantic import BaseModel, EmailStr, validator, root_validator
from datetime import date
import re

class PlayerBase(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    dob: date
    email: EmailStr
    phone: str | None = None
    password: str
    confirm_password: str
    club_name: str
    country: str
    parent_name: str | None = None
    parent_email: EmailStr | None = None
    parent_phone: str | None = None
    parent_consent: bool | None = None
    terms_accepted: bool
    data_consent: bool

    @validator("firstname", "middlename", "lastname")
    def validate_names(cls, v, field):
        if not re.match("^[A-Za-z '-]+$", v):
            raise ValueError(f"{field.name.replace('_', ' ').capitalize()} contains invalid characters")
        return v

    @validator("dob")
    def validate_dob_not_future(cls, v):
        if v > date.today():
            raise ValueError("Date of birth cannot be in the future")
        return v

    @validator("password")
    def validate_password_strength(cls, v):
        if len(v) < 8 or not re.search(r"[A-Z]", v) or not re.search(r"[a-z]", v) \
           or not re.search(r"\d", v) or not re.search(r"[^\w\s]", v):
            raise ValueError("Password must be at least 8 characters long and include upper, lower, number, and symbol")
        return v

    @root_validator
    def validate_password_match_and_consents(cls, values):
        pw = values.get("password")
        cpw = values.get("confirm_password")
        if pw != cpw:
            raise ValueError("Passwords do not match")
        if not values.get("terms_accepted"):
            raise ValueError("Terms must be accepted")
        if not values.get("data_consent"):
            raise ValueError("Data consent must be accepted")
        return values

    @root_validator
    def validate_under_13_parent_info(cls, values):
        dob = values.get("dob")
        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 13:
                missing_fields = []
                if not values.get("parent_name"):
                    missing_fields.append("parent_name")
                if not values.get("parent_email"):
                    missing_fields.append("parent_email")
                if not values.get("parent_phone"):
                    missing_fields.append("parent_phone")
                if values.get("parent_consent") is not True:
                    missing_fields.append("parent_consent")

                if missing_fields:
                    raise ValueError(
                        f"Under 13: {', '.join(missing_fields)} {'is' if len(missing_fields) == 1 else 'are'} mandatory"
                    )
        return values


class PlayerCreate(PlayerBase):
    pass


class PlayerResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
