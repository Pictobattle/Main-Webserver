from flask import Flask, send_from_directory, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

#-------------Beond here are only occasionly to never changed urls--------------
@app.route('/favicon.ico')
def favicon():
	return redirect(url_for('static', filename='favicon.ico'))

if __name__ == "__main__":
	app.secret_key = 'Ymsf,sfatwBU!Iwruh,bus'
	app.debug = True
	app.run(
		host='0.0.0.0',
		port=4500
		)