from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/post/record')
def recordPost():
	username=str(request.form.get("username"))
	#password=
	return redirect('/')

#---------------------------------Static stuff:---------------------------------
"""@app.route('/favicon.ico')
def favicon():
	return redirect(url_for('static', filename='favicon.ico'))"""

if __name__ == "__main__":
	app.secret_key = 'Ymsf,sfatwBU!Iwruh,bus'
	app.debug = True
	app.run(
'''		host='0.0.0.0',
		port=4000
		ssl_context=('/var/www/SSL/server.crt', '/var/www/SSL/server.key')'''
		)
