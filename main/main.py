from flask import Flask, render_template, redirect, url_for, request, jsonify, session

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')


@app.route('/postPicture', methods=['POST','GET'])
def postPicture():
	if request.method == 'POST':
		username=request.form.get("username")
		password=request.form.get("password")
		description=str(request.form.get("description"))
		battle=str(request.form.get("battleSelector"))

		if username != None or password != None:
			#this most likely means it is from app
			username = str(username)
			password = str(password)
		#else:

		return "Yo waddup " + str([username, password, description, battle])
	elif request.method == 'GET':
		return render_template('postPicture.html')

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
	app.secret_key = 'RC0ZT6kkTQUSHt6hf0GFHhgddWaew3ApGRZnzcPPtClT4zhKiD6OWhlW4t2Z0X2'
	app.debug = True
	app.run(
		host='127.0.0.1',
		port=4000
		)
