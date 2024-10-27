from sqlalchemy.orm import Session
from app.models import models


class PropertyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_properties(self):
        return self.db.query(models.Property).all()

    def get_property_by_id(self, property_id: int):
        return self.db.query(models.Property).filter(models.Property.id == property_id).first()

    def update_owner(self, property_id: int, new_owner_id: int):
        property = self.get_property_by_id(property_id)
        if property:
            property.owner_id = new_owner_id
            self.db.commit()
            self.db.refresh(property)
        return property

    def create_property(self, cost: int, rent: int):
        new_property = models.Property(cost=cost, rent=rent)
        self.db.add(new_property)
        self.db.commit()
        self.db.refresh(new_property)
        return new_property
