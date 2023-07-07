import re
from copy import deepcopy
from sqlalchemy.sql import func
from cms.extensions import db


class Model:
    @db.declared_attr
    def __tablename__(cls):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    id_ = db.Column("id", db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    @classmethod
    def create(cls, data):
        instance = cls(**data)
        db.session.add(instance)

    def update(self, data):
        db.session.query(self.__class__).filter(id_=self.id_).update(data)

    @classmethod
    def update_by_id(cls, id_, data):
        safe_data = deepcopy(data)
        safe_data.pop("id", None)
        db.session.query(cls).filter(id_=id_).update(data)

    @classmethod
    def get(cls, id_):
        db.session.query(cls).get(id_)
