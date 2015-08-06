from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

localTest=True

sqlDuplicateErrorCode = 1062

sqlHost="127.0.0.1"
sqlPass="pictobattle"
sqlDb="pictobattle"
if localTest:
	sqlPass="picto1Battle"
	sqlUser="pictoext"
	sqlHost="lucieng.ddns.net"

'''readDb = MySQLdb.connect(
	host="lucieng.ddns.net",
    user="pictoext",
	passwd="picto1Battle",
	db="pictobattle"
	)'''

readDb="hey"

def sqlServerConnect():
	global sqlHost
	global sqlUser
	global sqlPass
	global sqlDb
	return createConnect(sqlHost,sqlUser,sqlPass,sqlDb)

def createConnect(sqlHost,sqlUser,sqlPass,sqlDb):
	db = MySQLdb.connect(
		host=sqlHost,
	    user=sqlUser,
		passwd=sqlPass,
		db=sqlDb
		)
	return db

def checkSQlExistance(connection, colsAndValues, table):
	"""
	Params:
	connection - a "MySQLdb.connect"
	colsAndValues - {<columnName>:<columnCheckVal>}
	table - table name
	"""

	cursor = connection.cursor() # creating cursor
	executeString='SHOW COLUMNS FROM ' + table + ';'
	cursor.execute(executeString) # getting columns

	output=cursor.fetchall() # getting columns
	columnNumbers=[] # creating array to hold column numbers that are being checked
	#columnAmount=len(output)
	for columnName in colsAndValues: # cycling through inputted columns
		for ii in range(len(output)): # cycling through actual columns
			columnFound=False # setting default value for columnFound to False
			if output[ii][0] == columnName:
				# checking if inputted column is equal to one of the cycled actual columns
				columnNumbers.append(ii) # adding the number column to the array (in same order as colsAndValues)
				columnFound=True # setting that column was found so the exception doesnt throw
				break

		if not columnFound: # if column isn't found
			raise Exception('The column \'' + columnName + '\' doesn\'t exist')
			# raise exception that column hasn't found

	executeString='SELECT * FROM ' + table
	cursor.execute(executeString) # executing table read

	for ii in cursor.fetchall(): # cycling through table entries
		for jj in range(len(colsAndValues)): # cycling through colsAndValue indexes
			#return str(colsAndValues.keys()[0])
			print str(jj)
			columnName=colsAndValues.keys()[jj] # setting columnName to the keys of colsAndValues

			columnNumber=columnNumbers[jj]
			# setting columnNumber to the value in columnNumbers
			#(is synced with colsAndValues [not acutall synced, just has the entries in the same order])

			columnCheckVal=colsAndValues[columnName]
			columnVal=ii[columnNumber] # getting value from column using columnNumber
			print(columnCheckVal)
			print(columnVal)

			occurences=[]
			if columnVal == columnCheckVal: # checks if column value is equal to the one inputted
				occurences.append(True)
			else:
				occurences.append(False)

			#print colsAndValues.keys()[jj] + " is " + str(occurences[len(occurences)-1])


		if False in occurences:
			# checks one of the asked column didnt match the inputted and acutal value
			print "false!!"
			pass
		else:
			return str(True) # all of the columns matched the inputted and actual value

	return str(False) # none of the columns matched

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/user/signUp', methods=['GET','POST'])
def signUp():

	if request.method == 'GET':
		return render_template('userSignUp.html')
	else:
		db = sqlServerConnect() # creates a connection to the database

		email=request.form.get("email")
		email=MySQLdb.escape_string(email)
		password=request.form.get("password")
		password=MySQLdb.escape_string(password)

		#return checkSQlExistance(readDb, {"email":"poo"},"logins")
		#return test()


		cur = db.cursor() # creating SQL cursor

		table="logins"
		cur.execute('SHOW COLUMNS FROM ' + table + ';')
		return str(cur.fetchall())


		try:
			executeString=(
				#'IF NOT EXISTS(SELECT TOP 1 user_id FROM logins WHERE email = "' + email + '"); '
				'INSERT INTO logins (email,password) VALUES ("' + email + '","' + password + '");'
			)
			#cur.execute('INSERT INTO logins (email,password) VALUES ("' + email + '","' + password + '") ON DUPLICATE KEY UPDATE user_id = LAST_INSERT_ID(user_id);')
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
			print(ii[0])
			tableVals.append(ii)

		db.commit()
		db.close()
		return str(tableVals)

@app.route('/test')
def test():
	global readDb
	return checkSQlExistance(readDb, {"email":"dddddd"}, "logins")

@app.route('/cheese')
def cheese():
	return str(readDb)
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
	readDb=sqlServerConnect()
	app.secret_key = 'RC0ZT6kkTQUSHt6hf0GFHhgddWaew3ApGRZnzcPPtClT4zhKiD6OWhlW4t2Z0X2'
	app.debug = True
	app.run(
		host='127.0.0.1',
		port=4000
		)
