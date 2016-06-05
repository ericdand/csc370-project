# Saiddit

Saiddit is a Reddit clone built as a project for UVic's CSC 370 (Database
Systems) course.

# Toolchain Setup

## On OS X

You'll need to first get `pip`, then use that to install `virtualenv`, `flask`,
and `flask-mysql`:

```
$ sudo easy_install pip
$ sudo -H pip install virtualenv
```

Now that we have `virtualenv` installed, navigate to the root of this project
(e.g. `~/Documents/GitHub/csc370-project/`) and do the following to install
Flask in a virtual environment (as recommended by the Flask docs):

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install flask
$ pip install flask-mysql
```

This will install `flask` and `flask-mysql` only within a virtual environment
in your `csc370-project` directory. When you're ready to stop working on the
project and go back to the real world, run the command:

```
$ deactivate
```

and `virtualenv` will tear down the virtual environment and go back to reality.
Remember to `source venv/bin/activate` again every time you want to work on the
project! Otherwise, python won't be able to find the `flask` package.

# Starting the Server

You can start the server by simply running:

```
$ python app.py
```

The server should then be accessible on your local machine on port 5000.
Navigate to `http://localhost:5000/` to see it with your own eyes. Press
`Ctrl-c` in your terminal to kill the server.

# Resources

The links below may help you to understand the project:

## Flask

* http://flask.pocoo.org/docs/0.11/quickstart/
* http://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
* http://flask.pocoo.org/snippets/54/

