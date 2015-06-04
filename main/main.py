from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/postPicture')
def postPicture():
	return render_template('postPicture.html')

@app.route('/postPicture/record')
def recordPost():
	username=str(request.form.get("username"))
	password=str(request.form.get("password"))
	description=str(request.form.get("description"))
	battle=str(request.form.get("battleSelector"))

	return "Yo waddup " + str([username, password, description, battle])

#---------------------------------Static stuff:---------------------------------

#--------------------------HTTP Error Pages:------------------------------------
@app.errorhandler(404)
def page_not_found(e):
	return render_template('errorPages/404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('errorPages/50x.html'), 500


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
