from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database.database import Base


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), index=True)
    balance = Column(Integer, default=300)
    behavior_type = Column(String(20), index=True)

    properties = relationship("Property", back_populates="owner")


class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cost = Column(Integer, nullable=False)
    rent = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey("players.id"), nullable=True)

    owner = relationship("Player", back_populates="properties")
