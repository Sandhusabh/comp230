from flask import render_template, Flask, request, redirect, flash, url_for
from flaskapp import app
from flaskapp.forms import AddressForm

@app.route("/", methods=['GET', 'POST'])
def index():
    form = AddressForm()
    if form.validate_on_submit():
        flash(f'Account created for !', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', form = form)

@app.route("/order", methods=['GET', 'POST'])
def order():
    return render_template('order.html', title='Home')

@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = price
    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)

@app.route('/task', methods=['POST'])
def task():
    if request.method == 'POST':
        try:
            global price
            price = request.form['price']
        finally:
            return render_template('order.html',key = stripe_keys['publishable_key'], price=price)
