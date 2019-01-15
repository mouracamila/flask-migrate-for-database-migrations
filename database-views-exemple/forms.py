# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Cat:')
    submit = SubmitField('Add Cat')

class DelForm(FlaskForm):

    id = IntegerField("Id Number of Cat to Remove: ")
    submit = SubmitField("Remove Cat")