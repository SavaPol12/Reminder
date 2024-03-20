from sqlalchemy.orm import Session
from database.models import User
from sqlalchemy.orm.attributes import flag_modified


def create_user(db: Session, tg_id: int):
    if not get_user(db, tg_id):
        user = User(tg_id=tg_id, words={})
        db.add(user)
        db.commit()
        return user


def get_users(db: Session):
    users = db.query(User).all()
    return users


def get_user(db: Session, tg_id: int):
    user = db.query(User).filter(User.tg_id == tg_id).first()
    return user


def update_users_words(db: Session, user: User, word: dict):
    old_words = user.words
    old_words.update(word)
    user.words = old_words
    flag_modified(user, "words")
    db.add(user)
    db.commit()
    return user.words


def get_user_words(db: Session, tg_id: int):
    return get_user(db, tg_id).words
