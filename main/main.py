from flask import Flask, render_template
import MySQLdb

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/signUp', methods=['GET','POST'])
def signUp():

	return "yo"

@app.route('/areWeOnline')
def thisIsStatic():
	return "we must be..."
#--------------------------HTTP Error Pages:------------------------------------
@app.errorhandler(404)
def page_not_found(e):
	return render_template('errorPages/404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('errorPages/50x.html'), 500


if __name__ == "__main__":
	app.secret_key = 'RC0ZT6kkTQUSHt6hf0GFHhgddWaew3ApGRZnzcPPtClT4zhKiD6OWhlW4t2Z0X2'
	app.debug = True
	app.run(
		host='127.0.0.1',
		port=4000
		)
