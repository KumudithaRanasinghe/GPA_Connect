from flask import Flask, render_template
from logic import Logic

#Create a Flask Interface
app = Flask(__name__)

#Create a route decorator

@app.route('/')

def index():

    print("GPA Value is : ",getGPA())
    return "<h1>Hello Flask</h1>"


#___________________________
def getGPA():

    list_credit = [4.0, 4.0, 4.0, 4.0, 4.0] #credit value of each 5 subjects set to order
    list_gpv = [4.0, 2.3, 2.7, 2.7, 3.7] #grade point value of each 5 subjects et to order A+=4.0, C+=2.3...

    my_instance = Logic(list_credit,list_gpv)
    
    return my_instance.getGPA()



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