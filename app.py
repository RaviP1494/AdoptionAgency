from flask import Flask, request, render_template, redirect, flash
from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "thisisthekey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:drowssap@localhost:5432/adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('pets.html', pets = pets)

@app.route("/add", methods=["GET", "POST"])
def add():
    """Pet add form; handle adding."""

    form = AddPetForm()
        
    if form.validate_on_submit():

        p = Pet(name = form.name.data, species = form.species.data, img_url = form.img_url.data, age = form.age.data, notes = form.notes.data)
        db.session.add(p)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("/add.html", form = form)

@app.route("/pets/<int:pid>", methods=["GET", "POST"])
def pet_view(pid):
    """Show individual pet details, along with edit form and edit form handling"""
    
    pet = Pet.query.get(pid)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.img_url = form.img_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template('/pet.html', p = pet, form = form)