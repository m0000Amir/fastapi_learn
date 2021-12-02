from typing import List


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.blog_post import required_functionality

from schemas import ArticleBase, ArticleDisplay
from db.database import SessionLocal, get_db
from db import db_article


router = APIRouter(
    prefix = "/article",
    tags = ["article"]
)

# Create article
@router.post("/", response_model=ArticleBase)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


# Get specific article
@router.get("/{id}", response_model=ArticleDisplay)
def get_article(id: int, db:  Session = Depends(get_db)):
    return db_article.get_article(db, id)