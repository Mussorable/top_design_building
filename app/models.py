from datetime import datetime, timezone
from typing import Optional, List
from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so


class User(db.Model):
    __tablename__ = 'users'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    full_name: so.Mapped[str] = so.mapped_column(sa.String(80))
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True)
    phone_number: so.Mapped[str] = so.mapped_column(sa.String(20), index=True, nullable=True)
    admin: so.Mapped[int] = so.mapped_column(sa.Integer(), default=0, index=True)

    messages: so.Mapped[List['Message']] = so.relationship('Message', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.full_name} | Administrator: {self.admin}>'


class ContactEmail(db.Model):
    __tablename__ = 'contact_emails'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True)

    messages: so.Mapped[List['Message']] = so.relationship('Message', backref='contact_email', lazy=True)

    def __repr__(self):
        return f'<Contact Email {self.email}>'


class Message(db.Model):
    __tablename__ = 'messages'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    text_message: so.Mapped[str] = so.mapped_column(sa.String(450))
    timestamp: so.Mapped[datetime] = so.mapped_column(sa.DateTime, default=datetime.now(timezone.utc))

    user_id: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer, sa.ForeignKey('users.id'), nullable=True)
    contact_email_id: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer, sa.ForeignKey('contact_emails.id'),
                                                                  nullable=True)

    def __repr__(self):
        return f'<Message {self.id} | User ID: {self.user_id} | Contact Email ID: {self.contact_email_id}>'
