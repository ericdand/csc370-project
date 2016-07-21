from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from hashlib import sha256

from user import SaidditUser
from post import SaidditPost

mysql = MySQL()
app = Flask(__name__)
# TODO(ericdand): Use a user other than root.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'Saiddit'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

app.secret_key = '\x88j\xd7\x1f&\xc6\x87(X\xa0\xc9\xc4\x96\xffL\xbe\xc8K\xa5JM\xdc\xae+'
login_manager = LoginManager()
login_manager.init_app(app)

def build_saiddituser_for_username(username):
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("SELECT subsaiddit from Subscribers WHERE username = '{0}';".format(username))
    result = cur.fetchall()
    subscriptions = [e[0] for e in result]
    cur.close()
    conn.close()
    return SaidditUser(username, subscriptions)

@login_manager.user_loader
def load_user(user_id):
    return build_saiddituser_for_username(user_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

def get_top_posts_for_subsaiddits(subsaiddits):
    top_posts = []
    conn = mysql.connect()
    for ss in subsaiddits:
        cur = conn.cursor()
        cur.execute("SELECT title, text, author, created, url FROM Posts WHERE subsaiddit = '{0}' ORDER BY created DESC LIMIT 10;".format(ss))
        result = cur.fetchall()
        for post in result:
            top_posts.append(SaidditPost(*post))
        cur.close()
    conn.close()
    return top_posts

def get_default_subsaiddits():
    defaults = []
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("SELECT title FROM Subsaiddits WHERE default_or_not_default = 'default';")
    result = [e[0] for e in cur.fetchall()]
    cur.close()
    conn.close()
    return result

@app.route('/')
def index():
    top_posts = []
    if current_user.is_authenticated:
        top_posts = get_top_posts_for_subsaiddits(current_user.subscriptions)
    else:
        top_posts = get_top_posts_for_subsaiddits(get_default_subsaiddits())
    return render_template('index.html', top_posts=top_posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = sha256(request.form['password']).hexdigest()
        subscriptions = []

        # TODO(edand): Authenticate here.
        # Just assume we put in OK credentials for now.
        authenticated = True

        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT username from Accounts where username='{0}' AND password='{1}';".format(username, password))
        data = cur.fetchone()
        cur.close()
        conn.close()
        if data is not None:
            login_user(build_saiddituser_for_username(*data))
            return redirect(url_for('index'))
        else:
            error = 'Could not authenticate. Wrong password?'

    return render_template('login.html', error=error)

def store_post(title, text, author, subsaiddit):
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Posts (title, text, author, subsaiddit) VALUES ('{0}', '{1}', '{2}', '{3}');".format(title, text, author, subsaiddit))
    cur.close()
    conn.commit()
    conn.close()

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        # TODO(edand): Show an error message telling the user to log in
        # if they aren't authenticated instead of just silently failing
        # to store their post.
        if current_user.is_authenticated:
            title = request.form['title']
            text = request.form['text']
            author = current_user.id
            subsaiddit = request.form['subsaiddit']
            store_post(title, text, author, subsaiddit)
        return redirect(url_for('index'))
    else:
        if current_user.is_authenticated:
            subsaiddits = current_user.subscriptions
        else:
            subsaiddits = get_default_subsaiddits()
        return render_template('post.html', user_subsaiddits=subsaiddits)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
