# This is whre you can start you python file for your week1 web app
# Name: Create a server, webpage can be editted in Python; use template

'''http://flask.pocoo.org/docs/views/'''

import flask, flask.views
import os
import functools

app = flask.Flask(__name__)
app.secret_key = "bumiao"

# database
users = {'mt':'peace'}

class Main(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		if 'logout' in flask.request.form:
			flask.session.pop('username', None)
			return flask.redirect(flask.url_for('index'))
		required = ['username', 'passwd']
		for r in required:
			if r not in flask.request.form:
				flash("Error: {0} is required.".format(r))
				return flask.redirect(flask.url_for('index'))
		username = flask.request.form['username']
		passwd = flask.request.form['passwd']
		if username in users and users[username] == passwd:
			flask.session['username'] = username
		else:
			flask.flash("username doesn't exist or incorrect password")
		return flask.redirect(flask.url_for('index'))
# need to use Decorator to protect the entire 'Remote' view

def login_required(method):
	@functools.wraps(method)
	def wrapper(*args, **kwargs):
		if 'username' in flask.session:
			return method(*args, **kwargs)
		else:
			flask.flash("A login is required to see the page!")
			return flask.redirect(flask.url_for('index'))
	return wrapper


class Remote(flask.views.MethodView):
	@login_required
	def get(self):
		return flask.render_template('remote.html')

	@login_required
	def post(self):
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))

class music(flask.views.MethodView):
	@login_required
	def get(self):
		songs = os.listdir('static/music/')
		return flask.render_template('music.html', songs=songs)

app.add_url_rule('/', view_func=Main.as_view('index'), methods=['GET', 'POST'])

app.add_url_rule('/remote/', view_func=Remote.as_view('remote'), methods=['GET', 'POST'])

app.add_url_rule('/music/', view_func=music.as_view('music'), methods=['GET'])

app.debug = True
app.run()

