from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from logic import Logic
import mysql.connector
import re

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

@app.route('/credit', methods=['GET', 'POST']) # handle ajax
def fetch():

    if request.method == 'POST':
        m_id = request.form['m_id']

        connection.connect() 
        read_q = "SELECT m_credits FROM module WHERE m_id= '"+m_id+"'"

        cursor = connection.cursor()
        cursor.execute(read_q)
        credit = cursor.fetchall()
        cursor.close()
        connection.close()

    return credit

@app.route('/setGpa', methods=['GET', 'POST']) # set GPA
def setGpa():

    list_credit = [] #credit hours
    list_gpv = [] # grade point value list

    if request.method == 'POST':
        selection = request.form['selection']
        credit = request.form['credit']

        a = re.findall(r'\d+', selection)
        b = re.findall(r'\d+', credit)

    selection_int_list = list(map(float, a))
    list_credit = list(map(float, b))

    connection.connect() 

    for i in range(1, len(selection_int_list)+1, 2):
 
        read_q = "SELECT g_point FROM grade WHERE g_id= '"+str(selection_int_list[i])+"'"

        cursor = connection.cursor()
        cursor.execute(read_q)
        fetches = cursor.fetchall()
        list_gpv.append(float(fetches[0][0]))
        cursor.close()

    connection.close()
    
    my_instance = Logic(list_credit,list_gpv)

    return str(my_instance.getGPA())


#about us page       
@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

#faq page
@app.route('/faq')
def faq():
    return render_template("faq.html")
    

if __name__ == '__main__':
    app.run(debug=True)
