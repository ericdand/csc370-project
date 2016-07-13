from flask import Flask, render_template
from flaskext.mysql import MySQL
from flask_login import LoginManager, login_user

from user import SaidditUser

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

@app.route('/')
def main():
    # TODO(edand): This is just a demo user.
    login_user(SaidditUser('admin'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
