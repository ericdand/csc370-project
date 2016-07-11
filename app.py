from flask import Flask,request, render_template
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
mysql.init_app(app)

@app.route('/', methods=['GET'])
def signin_form():
	return render_template('loginpage.html')
	
@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	cursor=mysql.connect().cursor()
	cursor.execute("SELECT * from Accounts where username='"+ username +"'AND password='"+ password+"';" )
	data = cursor.fetchone()
	if data is None:
		return render_template('loginpage.html', message='Incorrect username or password', username=username)
	else:
		return render_template('index.html', username=username)
	

if __name__ == '__main__':
    app.run()
