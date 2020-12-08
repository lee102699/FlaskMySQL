from flask import Flask, render_template, request
import mysql.connector


connection = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "9ol./;p0",
  database = "test",
  )


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        connection.commit()

        return 'success'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
