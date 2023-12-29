from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_gpa_connect',
    'raise_on_warnings': True
}

# Create a connection and cursor
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

app = Flask(__name__)
#landing page
@app.route('/')
def index():
    connection.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM degree ORDER BY d_id")
    value = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("index.html", data=value)
    

#gpa calculation page

@app.route('/calgpa', methods=['GET', 'POST'])
def testcal_gpa():
    try:
        connection.connect()
        cursor = connection.cursor()
        degree_id = request.form['degree']
        
        # Execute the first query
        cursor.execute("SELECT * FROM module JOIN degree_module ON module.m_id = degree_module.m_id WHERE degree_module.d_id = %s", (degree_id,))
        modules = cursor.fetchall()

        # Execute the second query
        cursor.execute("SELECT * FROM grade")
        grades = cursor.fetchall()
        

        return render_template("/testcalgpa.html", modules=modules, grades=grades)
    except Exception as e:
        # Log the exception or handle it appropriately
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and connection in a finally block
        cursor.close()
        connection.close()

#about us page       
@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

#faq page
@app.route('/faq')
def faq():
    return render_template("faq.html")
    