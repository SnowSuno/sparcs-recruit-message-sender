from flask import Flask, redirect, request
import os

app = Flask(__name__)


@app.route('/')
def do_redirect():
    phone, message = request.args.get('phone'), request.args.get('msg')

    if not phone or not message:
        return "Bad request parameters", 400

    return redirect(f"sms://{phone}?&body={message}")


app.run(host="0.0.0.0", port=os.environ.get('PORT'))
