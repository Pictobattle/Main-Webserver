from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

localTest=True

sqlDuplicateErrorCode = 1062

sqlHost="localhost"
sqlPass="picto1Battle"
sqlUser="pictoext"
sqlDb="pictobattle"
if localTest:
	sqlHost="lucieng.ddns.net"

db = MySQLdb.connect(
	host=sqlHost,
    user=sqlUser,
	passwd=sqlPass,
	db=sqlDb
	)

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/user/signUp', methods=['GET','POST'])
def signUp():

	if request.method == 'GET':
		return render_template('userSignUp.html')
	else:
		global db # getting global db varible

		email=request.form.get("email")
		email=MySQLdb.escape_string(email)
		password=request.form.get("password")
		password=MySQLdb.escape_string(password)

		cur = db.cursor() # creating SQL cursor

		try:
			cur.execute('INSERT INTO logins (email,password) VALUES ("' + email + '","' + password + '");')
		except MySQLdb.IntegrityError, message:
			errorcode = message[0]
			if errorcode == sqlDuplicateErrorCode:
				return "a dupe"
			else:
				raise # unexpected error, reraise

		cur.execute("SELECT * FROM logins")

		tableVals=[]
		for ii in cur.fetchall():
			tableVals.append(ii)
		return str(tableVals)

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
