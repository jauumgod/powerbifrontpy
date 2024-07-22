from app import *
from app import db


class User(db.Model):
    __tablename__ = 'tabUsers'
    idUser: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    permission: Mapped[str] = mapped_column(String(100), default=['default'])
    dataCreated: Mapped[str] = mapped_column(String(100))
    