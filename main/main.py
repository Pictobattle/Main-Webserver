from flask import Flask, render_template, request
import httplib, urllib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')
@app.route('/user/signUp', methods=['GET','POST'])
def signUp():
    if request.method == 'GET':
        return render_template('userSignUp.html')
    else:
        params = urllib.urlencode({'email': request.form.get("email"), 'password': request.form.get("password")})
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        conn = httplib.HTTPConnection("localhost:8081")
        conn.request("POST", "/user/signUp", params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return str (data)
        return "check with api server here then report"

if __name__ == "__main__":
	app.secret_key = 'RC0ZT6kkTQUSHt6hf0GFHhgddWaew3ApGRZnzcPPtClT4zhKiD6OWhlW4t2Z0X2'
	app.debug = True
	app.run(
		host='127.0.0.1',
		port=8080
		)
