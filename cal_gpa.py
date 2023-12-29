from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash #generate password to hash type to save database. sequre option
from logic import Logic # GPA calculation function
import mysql.connector

app = Flask(__name__)
app.run(debug=True)
db_config = { #databsse configuration
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'db_gpa_connect',
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor() #create the connection and cursor object

@app.route('/')#index page for degree selection page
def index():
    
    read_q = "SELECT * FROM degree ORDER BY d_id" #select all degree from degree table
    conn.connect()
    cursor = conn.cursor()
    cursor.execute(read_q)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("base.html",degree_programs=rows)
  

@app.route('/module', methods=['GET', 'POST'])# for handle the modules select page
def module():

    degree_id = request.form['degree']

    conn.connect()
        
    read_q = "SELECT * FROM module JOIN degree_module ON module.m_id = degree_module.m_id WHERE degree_module.d_id = '"+degree_id+"'" #query for all modules related to that digree
    #read_q = "SELECT * FROM module WHERE m_id IN(SELECT m_id FROM degree_module WHERE d_id='"+degree_id+"')" same with inner query

    cursor = conn.cursor()
    cursor.execute(read_q)
    modules = cursor.fetchall()
    cursor.close()
    conn.close()


    conn.connect()
        
    read_q = "SELECT * FROM grade" #get all grade simbols add to dropdown list

    cursor = conn.cursor()
    cursor.execute(read_q)
    grades = cursor.fetchall()
    cursor.close()
    conn.close()
    print(modules)
    return render_template("module1.html",modules=modules, grades=grades) #pass the all modules and grades list to module page



@app.route('/fetch', methods=['GET', 'POST']) #this function create for tests. not important. this created to my module selection show on thath same page as text(for test ajax). used for test some ajax code 
def fetch():

    if request.method == 'POST':
        query = request.form['query']

    return query
    




@app.route('/signup', methods=['GET', 'POST']) # for signup the user. only used i username and password at this tyme for signup. repeat password check working. 
def signup():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['r_password']

        if password==repeat_password:

            conn.connect()

            read_q = "SELECT COUNT(*) FROM user where u_name= '"+username+"'" #1st check the username if username available on database redirect to login page to login. 

            cursor = conn.cursor()
            cursor.execute(read_q)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()

            if rows[0][0] > 0: #check the data availability.. this query return 0 or 1. if username awailable count as 1. 
                
                return redirect(url_for('login')) #redirect to login page
            else:
                username = request.form['username']
                password = request.form['password']

                hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8) #generate hashed password to save on database

                query = "INSERT INTO user (u_name, u_password) VALUES (%s, %s)" #insert registration data to user table.
                values = (username, hashed_password)

                try:
                    conn.connect()
                    cursor = conn.cursor()
                    cursor.execute(query, values)
                    conn.commit()
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

        conn.connect()
        cursor = conn.cursor()
        cursor.execute(read_q)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        if rows[0][0]==username: #if username similar to user entered username.. then,

            read_q = "SELECT u_password FROM user WHERE u_name = '"+username+"';" #..check the password

            conn.connect()
            cursor = conn.cursor()
            cursor.execute(read_q)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()

            if check_password_hash(rows[0][0], password): # database have the hashed password before. so we need convert thath password to regular type and check similarity.
            #session['user_id'] = user.id
            #flash('Login successful', 'success')
                return render_template('home.html')
            else:
                return render_template('login.html', error='Username or Password is wrong')
        else:
            return render_template('login.html', error='Username or Password is wrong')

    return render_template('login.html')


@app.route('/logout') # this function use to logout user. we need to remove session setup for that user. this function not completed.
def logout():
    #session.pop('user_id', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))



@app.route('/home') #home page function. 
def home():
    return render_template('home.html')

# IMPORTANT
#this all html template pages need to run this code. there have not these pages. 




#___________________________
def getGPA():

    list_credit = [4.0, 4.0, 4.0, 4.0, 4.0] #credit value of each 5 subjects
    list_gpv = [4.0, 2.3, 2.7, 2.7, 3.7] #grade point value of each 5 subjects

    my_instance = Logic(list_credit,list_gpv)
    
    return my_instance.getGPA()

if __name__ == '__main__':
    app.run(debug=True)

#_______________________________________________
# LETTER GRADE	GRADE POINTS	NUMERICAL GRADE
# A+	        4.0	            85–100
# A	            4.0	            75-84
# A-	        3.7	            70-74
# B+	        3.3	            63-69
# B	            3.0	            55-62
# B-	        2.7	            50-54
# C+	        2.3	            45-49
# C	            2.0	            40-44
# C-	        1.7	            35-39
# D+	        1.3	            30-34
# D	            1.0	            20-29
# F 	        0.0	            00-19          