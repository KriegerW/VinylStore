from flask import render_template, url_for, flash, redirect
from shop import app, db
from shop.models import User, Record, Cart
from shop.forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    records = Record.query.all()
    return render_template('home.html', records=records)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(str(generate_password_hash('x516xx')), 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route("/product/<title>")
def product(title):
    records = Record.query.filter_by(name=title).one()
    return render_template('details.html', title=title, records=records)


@app.route("/cart")
@app.route("/cart/<item_id>")
def cart(item_id=0):
    if not item_id == 0:
        new_item = Cart.query.filter_by(item_id=item_id).first()
        if not new_item:
            new_item = Cart(item_id=item_id)
            db.session.add(new_item)
            db.session.commit()
    items = Cart.query.all()
    records = []
    for item in items:
        records.append(db.session.query(Record).get(item.item_id))
    return render_template('cart.html', title='Cart', records=records)
