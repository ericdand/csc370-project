from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from user import SaidditUser
from post import SaidditPost

mysql = MySQL()
app = Flask(__name__)
# TODO(ericdand): Use a user other than root.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'Saiddit'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# TODO(ericdand): Uncomment the line below once
# you have the database actually set up.
# mysql.init_app(app)

app.secret_key = '\x88j\xd7\x1f&\xc6\x87(X\xa0\xc9\xc4\x96\xffL\xbe\xc8K\xa5JM\xdc\xae+'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return SaidditUser(user_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

def get_top_posts_for_subsaiddits(subsaiddits):
    top_posts = []
    for ss in subsaiddits:
        # Get top posts from ss.
        # TODO(edand): These are test values for now.
        top_posts.append(
                SaidditPost("top post from {0}".format(ss),
                    "text", "author", "sometime"))
    return top_posts

default_subsaiddits = [
        "Cats n stuff",
        "Meta-Saiddit",
        "The Weather Subsaiddit",
        ]

@app.route('/')
def index():
    top_posts = []
    if current_user.is_authenticated:
        top_posts = get_top_posts_for_subsaiddits(current_user.subscriptions)
    else:
        top_posts = get_top_posts_for_subsaiddits(default_subsaiddits)
    return render_template('index.html', top_posts=top_posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # TODO(edand): Authenticate here.
        # Just assume we put in OK credentials for now.
        authenticated = True

        # cursor = mysql.connect().cursor()
        # cursor.execute("SELECT * from Accounts where username='"+ username +"'AND password='"+ password+"';" )
        # data = cursor.fetchone()
        # if data is not None:
        #     authenticated = True

        if authenticated:
            login_user(SaidditUser(username))
            return redirect(url_for('index'))
        else:
            error = 'Could not authenticate. Wrong password?'

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run()
