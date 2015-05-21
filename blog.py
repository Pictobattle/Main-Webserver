from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	return "<h1>Looking for Picto Battle Blog</h1>Uhmmm... how do I say this... <br> <strong>I need to get someone to make it...!</strong>"

if __name__ == "__main__":
	app.secret_key = 'Ymsf,sfatwBU!Iwruh,bus'
	app.debug = True
	app.run(
		host='0.0.0.0',
		port=6000
		)
