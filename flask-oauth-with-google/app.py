import os
#os.environ['AOUTHLIB_INSECURE_TRANSPORT'] = 1
#os.environ['OAUTHLIB_RELEX_TOKEN_SCOPE'] = 1

## Loggin system
import logging
logging.basicConfig(level=logging.DEBUG)

#########
from flask import Flask,redirect,url_for,render_template
from flask_dance.contrib.google import make_google_blueprint,google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

blueprint = make_google_blueprint(
    client_id='824848467259-fluj67834hk5ndlbecpbpepbaeuojl44.apps.googleusercontent.com',
    client_secret='6s0t58w0QyD5z3fyjbD7JZgA',
    offline=True,
    scope=[
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/userinfo.email'
        #'profile', 'email'
    ]
)

app.register_blueprint(blueprint,url_prefix='/login')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    # RETURN ERROR INTERNAL SERVER ERROR IF NOT LOGGED IN!!
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html',email=email)


@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))

    return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
    #app.run()
