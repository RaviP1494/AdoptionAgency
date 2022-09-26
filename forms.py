from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddTemplateForm(FlaskForm):
    """Template Form"""

    name = StringField("Name")
    weight = FloatField("Weight")