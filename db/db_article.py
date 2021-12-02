from pydantic.networks import import_email_validator
from sqlalchemy.orm.session import Session
from router.blog_post import required_functionality


from schemas import ArticleBase, UserBase, UserDisplay
from db.models import DbArticle, DbUser
from db.hash import Hash


def create_article(db: Session, request: ArticleBase):
    new_article = DbArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
    

def get_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    # Handle errors
    return article
