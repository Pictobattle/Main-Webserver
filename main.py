from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	return "yo!"

if __name__ == "__main__":
	app.secret_key = 'Ymsf,sfatwBU!Iwruh,bus'
	app.debug = True
	app.run(
		host='0.0.0.0',
		port=80
		)
