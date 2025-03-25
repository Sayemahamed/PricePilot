from sqlmodel import Field, SQLModel, Relationship, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import pytz


class User(SQLModel, table=True):
    email: str = Field(sa_column=Column(pg.VARCHAR, primary_key=True, nullable=False))
    name: str = Field(sa_column=Column(pg.VARCHAR, nullable=False))
    hashed_password: str = Field(sa_column=Column(pg.VARCHAR, nullable=False))

    # Relationships
    trackings: list["Tracking"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete"})


class Product(SQLModel, table=True):
    url: str = Field(sa_column=Column(pg.VARCHAR, primary_key=True, nullable=False))
    name: str = Field(sa_column=Column(pg.VARCHAR, nullable=False))
    price: float = Field(sa_column=Column(pg.FLOAT, nullable=False))

    # Relationships
    trackings: list["Tracking"] = Relationship(back_populates="product", sa_relationship_kwargs={"cascade": "all, delete"})
    prices: list["Price"] = Relationship(back_populates="product", sa_relationship_kwargs={"cascade": "all, delete"})


class Tracking(SQLModel, table=True):
    email: str = Field(foreign_key="user.email", primary_key=True, nullable=False)
    url: str = Field(foreign_key="product.url", primary_key=True, nullable=False)
    time: datetime = Field(default_factory=lambda: datetime.now(pytz.utc), sa_column=Column(pg.TIMESTAMP, nullable=False))

    # Relationships
    user: User = Relationship(back_populates="trackings")
    product: Product = Relationship(back_populates="trackings")


class Price(SQLModel, table=True):
    url: str = Field(foreign_key="product.url", primary_key=True, nullable=False)
    time: datetime = Field(default_factory=lambda: datetime.now(pytz.utc), sa_column=Column(pg.TIMESTAMP, nullable=False))
    price: float = Field(sa_column=Column(pg.FLOAT, nullable=False))

    # Relationships
    product: Product = Relationship(back_populates="prices")
