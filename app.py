from flask import Flask, render_template
from flaskext.mysql import MySQL

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

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
