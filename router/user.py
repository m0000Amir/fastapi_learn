from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.blog_post import required_functionality

from schemas import UserBase, UserDisplay
from db.database import get_db
from db.models  import DbUser
from db import db_user


router = APIRouter(
    prefix = "/user",
    tags = ["user"]
)


@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)
