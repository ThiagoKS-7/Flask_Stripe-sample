# Accept a Payment with Stripe Checkout

Stripe Checkout is the fastest way to get started with payments. Included are some basic build and run scripts you can use to start up the application.

## Running the sample

1. Build the server

~~~
pip3 install -r requirements.txt
~~~

2. Run the server

~~~
gunicorn run server:app
~~~

3. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)