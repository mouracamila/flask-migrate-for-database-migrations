#myproject/owners/views.py
from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprints = Blueprint('owners',__name__, template_folder = 'templates/owners')

@owners_blueprints.route('/add',methods=['GET','POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data
        cat_id = form.cat_id.data
        # add new owner to database
        new_owner = Owner(name,cat_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_cat'))

    return render_template('add.html',form=form)
