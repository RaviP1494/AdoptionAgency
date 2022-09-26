from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):
    """Pet Add Form"""

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(["dog", "cat", "porcupine"])])
    img_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Pet Edit Form"""

    img_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")