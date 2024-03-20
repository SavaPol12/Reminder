from sqlalchemy import JSON, Column, Integer
from database.config import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    words = Column(JSON)

    def __repr__(self):
        return f'{self.id} {self.tg_id}'
