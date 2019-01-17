# cats --> views.py
from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.cats.forms import AddForm,DelForm
from myproject.models import Cat

cats_blueprint = Blueprint('cats',__name__,template_folder='templates/cats')

@cats_blueprint.route('/add', methods=["GET","POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # add new cat to database
        new_cat = Cat(name)
        db.session.add(new_cat)
        db.session.commit()

        return redirect(url_for('cats.list'))

    return render_template('add.html',form=form)

@cats_blueprint.route('/list')
def list():
    cats = Cat.query.all()
    return render_template('list.html', cats=cats)

@cats_blueprint.route('/delete', methods=["GET","POST"])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        cat = Cat.query.get(id)
        db.session.delete(cat)
        db.session.commit()

        return redirect(url_for("cats.list"))

    return render_template('delete.html',form=form)
