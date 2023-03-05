from flask import Flask, redirect, request
import os

app = Flask(__name__)


@app.route('/')
def do_redirect():
    phone, body = request.args.get('phone'), request.args.get('body')

    return redirect(f"sms://{phone}?&body={body}")


app.run(host="0.0.0.0", port=os.environ.get('PORT'))
