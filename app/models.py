from typing import Optional
from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so


class User(db.Model):
    __tablename__ = 'users'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    full_name: so.Mapped[str] = so.mapped_column(sa.String(80))
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    phone_number: so.Mapped[str] = so.mapped_column(sa.String(20), index=True, nullable=True)

    text_message: so.Mapped[Optional[str]] = so.mapped_column(sa.String(450))

    admin: so.Mapped[int] = so.mapped_column(sa.Integer(), default=0, index=True)

    def __repr__(self):
        return f'<User {self.full_name} | Administrator: {self.admin}>'
