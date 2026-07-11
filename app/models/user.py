from app.database.base import Base

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
         Integer,
         primary_key = True,
         index = True
    )

    name: Mapped[str] = mapped_column(String)

    email: Mapped[str] = mapped_column(
        String,
        unique = True,
        index = True
    )

    password: Mapped[str] = mapped_column(String) 

