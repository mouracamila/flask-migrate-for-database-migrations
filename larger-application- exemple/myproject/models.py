#MODELS.PY
# set up db inside the __init__.py under myproject folder
from myproject import db

class Cat(db.Model):

    __tablename__ = 'cats'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='cat',userlis=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Cat name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Cat name is {self.name} and no owner yet!"

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Interger,primary_key=True)
    name = db.Column(db.Text)

    cat_id = db.Column(db.Integer,db.ForeignKey('cats.id'))

    def __init__(self,name,cat_id):
        self.name = name
        self.cat_id = cat_id
