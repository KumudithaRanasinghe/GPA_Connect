from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash #generate password to hash type to save database. sequre option
from logic import Logic
import mysql.connector
import re
from flask_session import Session
import google.generativeai as genai

from IPython.display import Markdown

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

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    connection.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM degree ORDER BY d_id")
    value = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("testindex.html", data=value)
    

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

        cursor.execute("SELECT d_id,d_name FROM degree WHERE d_id=%s",(degree_id,))
        degree = cursor.fetchall()
        
        return render_template("/testcalgpa.html",degree=degree, modules=modules, grades=grades)
    
    except Exception as e:
        # Log the exception or handle it appropriately
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and connection in a finally block
        cursor.close()
        connection.close()

@app.route('/credit', methods=['GET', 'POST']) # handle ajax
def credit():

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
        name = request.form['name']
        username = request.form['username']
        student_id = request.form['student_id']
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['r_password']

        if password==repeat_password:

            connection.connect()

            # read_q = """ "SELECT COUNT(*) FROM user where u_name= "'+username+'" """ #check if username available on database then redirect to login
            read_q = "SELECT COUNT(*) FROM user WHERE u_name = %s"
            

            cursor = connection.cursor()
            # cursor.execute(read_q)
            cursor.execute(read_q, (username,))
            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            if rows[0][0] > 0: #check the data availability.. this query return 0 or 1. if username awailable count as 1. 
                
                # return redirect(url_for('signin')) #redirect to login page
                return render_template('signup.html', error='* Signup unsuccessful. Username already in use')
            else:

                connection.connect()

                read_q = "SELECT COUNT(u_id) FROM user where u_id= '"+student_id+"'"

                cursor = connection.cursor()
                cursor.execute(read_q)
                rows = cursor.fetchall()
                cursor.close()
                connection.close()

                if rows[0][0] > 0:
                
                
                    return render_template('signup.html', error='* Signup unsuccessful. Wrong student id')
                else:
                
                    hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8) #generate hashed password to save on database

                    query = "INSERT INTO user (u_id, u_name, name, email, gpa, d_id, user_type, u_password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" #insert registration data to user table.
                    values = (student_id, username, name, email, 0, 0, "student", hashed_password)

                    try:
                        connection.connect()
                        cursor = connection.cursor()
                        cursor.execute(query, values)
                        connection.commit()
                        # return redirect(url_for('signin')) # home page means the after load page signup. login page recomended to login to user again
                        #                                     # try exp used for handle if have error on this process
                        return render_template('signup.html', error='* Signup successfully')
                    
                    except Exception as e:
                        return f"Error: {str(e)}"
        else:
            return render_template('signup.html', error='* Password not matching')

    return render_template('signup.html')   



@app.route('/signin', methods=['GET', 'POST'])# this function for handle the login page. check userdetails to signin.
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        read_q = "SELECT COUNT(u_name) FROM user where u_name= '"+username+"';" # check if have username on database user table

        connection.connect()
        cursor = connection.cursor()
        cursor.execute(read_q)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()

        if rows[0][0]==1: #if username similar to user entered username.. then,

            read_q = "SELECT u_password FROM user WHERE u_name = '"+username+"';" #..check the password

            connection.connect()
            cursor = connection.cursor()
            cursor.execute(read_q)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()

            if check_password_hash(rows[0][0], password): # convert hash password to regular type and check similarity.
                session['username'] = username;
                connection.connect()
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM degree ORDER BY d_id")
                value = cursor.fetchall()
                cursor.close()
                connection.close()
                return render_template("testindex.html", data=value)
            else:
                return render_template('signin.html', error='* Username or Password is wrong')
        else:
            return render_template('signin.html', error='* User not found. please register or check username')

    return render_template('signin.html')


@app.route('/signout') # logout user
def signout():
    session.pop('username', None)
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

#job explore page
@app.route("/jobs", methods=['GET'])
def jobs():
    try:
        if request.method == 'GET':

            degree_id = request.args.get('id')
            gpa = request.args.get('gpa')

            try:
                connection.connect()
                cursor = connection.cursor()
      
                cursor.execute("SELECT d_name FROM degree WHERE d_id=%s",(degree_id,))
                degree_name = cursor.fetchall()

            except Exception as e:
       
                print(f"An error occurred: {e}")
            finally:
       
                cursor.close()
                connection.close()

            prompt = f"I have a GPA of {gpa} in degree {degree_name}. need structured details about the potential job opportunities with this GPA? Return html and should only include <div> and <br> tags with classes 'main-description, title, industry, salary, job-description'. include about gpa value and digree program to main-description. explain job by job in detail. minimum 250 words needed. do not use <h1>, <h2>, <h3> tags"
            
            # print("Generate route accessed")
            # print(request.get_json())

            GOOGLE_API_KEY='AIzaSyCg_2OOxs6GSIm1cjDkNmgZbkdIzJC4NNg'

            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel('gemini-pro')

            response = model.generate_content(prompt)
               
            return render_template('jobs.html', resp=response.text)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    app.run(debug=True)
