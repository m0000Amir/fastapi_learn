"""
ORM functionality

"""

from pydantic.networks import import_email_validator
from sqlalchemy.orm.session import Session
from router.blog_post import required_functionality


from schemas import UserBase, UserDisplay
from db.models import DbUser
from db.hash import Hash


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    # Create element in database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

    
# read all elements
def get_all_users(db: Session):
    return db.query(DbUser).all()


# read only one user
def get_user(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()


# update user
def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'


# delete user
def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return "ok"