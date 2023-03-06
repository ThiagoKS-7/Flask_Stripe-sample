from flask import Flask, redirect
from decouple import config
import stripe
stripe.api_key = f"{config('STRIPE_API_KEY')}"

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

@app.route('/')
def hello_world():
    return redirect('/create-checkout-session')

@app.route('/create-checkout-session', methods=['POST', 'GET'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': f"{config('PRICE_ID')}",
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url= f"{config('HOST_NAME')}/success.html",
            cancel_url=f"{config('HOST_NAME')}/cancel.html",
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)