# adoption-site.py
import os
from forms import AddForm, DelForm
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

##########################
## SQL DATABASE SECTION ##
##########################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#############
### MODELS###
#############

class Cat(db.Model):

    __tablename__ = 'cats'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Cat name: {self.name}"

##################################
## VIEW FUNCTIONS -- HAVE FORMS ##
##################################

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods = ['GET','POST'])
def add_cat():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data

        new_cat = Cat(name)
        db.session.add(new_cat)
        db.session.commit()

        return redirect(url_for('list_cat'))

    return render_template('add.html',form=form)

@app.route('/list')
def list_cat():

    cats = Cat.query.all()
    return render_template('list.html',cats=cats)

@app.route('/delete',methods=['GET','POST'])
def del_cat():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        cat = Cat.query.get(id)
        db.session.delete(cat)
        db.session.commit()

        return redirect(url_for('list_cat'))
    return render_template('delete.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
