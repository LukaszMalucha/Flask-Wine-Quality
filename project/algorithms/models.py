from db import db


## Code Templates Main Repository

class CodeModel(db.Model):
    __tablename__ = 'CodeModel'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    file = db.Column(db.LargeBinary)

    def __init__(self, name, file):
        self.name = name
        self.file = file

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(type_of_algorithm=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()