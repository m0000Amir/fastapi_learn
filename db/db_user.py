"""
ORM functionality

"""

from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm.session import Session
# from starlette import status



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
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article with id {id} not found")
    return user


def get_user_by_username(db: Session, username: str):

    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with username {username} not found")
    return user


# update user
def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article with id {id} not found")
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
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Article with id {id} not found")
    db.delete(user)
    db.commit()
    return "ok"