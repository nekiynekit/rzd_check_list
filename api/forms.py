from tokenize import String
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FieldList
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search_request = StringField('Название смены: ', validators=[DataRequired()])
    submit = SubmitField('Найти чек-лист для смены')

class CheckListForm(FlaskForm):
    name = StringField('Название: ', validators=[DataRequired()])
    items = FieldList(StringField())
    submit = SubmitField('Создать чек-лист')
    