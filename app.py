from flask import Flask, request, render_template, redirect, flash
from forms import AddTemplateForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "thisisthekey"

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """Snack add form; handle adding."""

    form = AddTemplateForm()

    if form.validate_on_submit():
        name = form.name.data
        weight = form.weight.data
        flash(f"Added {name} at {weight}")
        return redirect("/add")

    else:
        return render_template("/add.html", form=form)