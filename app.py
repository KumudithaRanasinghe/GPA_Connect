from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from werkzeug.security import generate_password_hash, check_password_hash #generate password to hash type to save database. sequre option
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

@app.route('/signup', methods=['GET', 'POST']) # for signup the user
def signup():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['r_password']

        if password==repeat_password:

            connection.connect()

            read_q = "SELECT COUNT(*) FROM user where u_name= '"+username+"'" #check if username available on database then redirect to login

            cursor = connection.cursor()
            cursor.execute(read_q)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            if rows[0][0] > 0: #check the data availability.. this query return 0 or 1. if username awailable count as 1. 
                
                return redirect(url_for('login')) #redirect to login page
            else:
                username = request.form['username']
                password = request.form['password']

                hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8) #generate hashed password to save on database

                query = "INSERT INTO user (u_name, u_password) VALUES (%s, %s)" #insert registration data to user table.
                values = (username, hashed_password)

                try:
                    connection.connect()
                    cursor = connection.cursor()
                    cursor.execute(query, values)
                    connection.commit()
                    return redirect(url_for('home')) # home page means the after load page signup. login page recomended to login to user again
                                                        # try exp used for handle if have error on this process
                
                except Exception as e:
                    return f"Error: {str(e)}"
        else:
            return render_template('signup.html', error='password not matching')
    

    return render_template('signup.html')   




@app.route('/login', methods=['GET', 'POST'])# this function for handle the login page. check userdetails to login.
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        read_q = "SELECT u_name FROM user where u_name= '"+username+"';" # check if have username on database user table

        connection.connect()
        cursor = connection.cursor()
        cursor.execute(read_q)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()

        if rows[0][0]==username: #if username similar to user entered username.. then,

            read_q = "SELECT u_password FROM user WHERE u_name = '"+username+"';" #..check the password

            connection.connect()
            cursor = connection.cursor()
            cursor.execute(read_q)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            if check_password_hash(rows[0][0], password): # convert hash password to regular type and check similarity.
            #session['user_id'] = user.id
            #flash('Login successful', 'success')
                return render_template('home.html')
            else:
                return render_template('login.html', error='Username or Password is wrong')
        else:
            return render_template('login.html', error='Username or Password is wrong')

    return render_template('login.html')


@app.route('/logout') # logout user
def logout():
    #session.pop('user_id', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

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
