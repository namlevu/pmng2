import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from productmng import db


class Photo(db.DynamicDocument):
    url = db.StringField()


class User(db.DynamicDocument):
    username = db.StringField(required=True)
    photo = db.EmbeddedDocumentField('Photo')
    fullname = db.StringField()
    email = db.StringField(required=True)
    password_hash = db.StringField()
    disabled = db.BooleanField(default=False, required=True)
    current_session = db.StringField()
    logined_at = db.DateTimeField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Cost(db.DynamicDocument):
    amount = db.IntField()
    reason = db.StringField()
    created_by = db.ReferenceField('User')
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

class TrackingStatus(db.DynamicDocument):
    index = db.IntField()
    name = db.StringField()

class Product(db.DynamicDocument):
    name = db.StringField()
    category = db.StringField()
    brand = db.StringField()
    photos = db.ListField(db.EmbeddedDocumentField('Photo'))
    costs = db.ListField(db.EmbeddedDocumentField('Cost'))
    sale_price = db.IntField()
    created_by = db.ReferenceField('User')
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    updated_by = db.ReferenceField('User')
    updated_at = db.DateTimeField()
    status = db.EmbeddedDocumentField('TrackingStatus')
    history = db.StringField()
    note = db.StringField()
    sold = db.BooleanField()
    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }

    def change_status(self, to_status):
        self.status = to_status
