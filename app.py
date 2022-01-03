from flask import Flask,render_template,request,session,redirect,url_for
import math

app = Flask(__name__)
app.config["SECRET_KEY"] = "St1232468"

@app.route("/")
def hello_world():
    return render_template("app.html")

@app.route("/home")
def home():
    return render_template("app.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        email_reg = session.get("email","email is not registered")
        password_reg = session.get("password","email is not registered")
        if email == email_reg:
            if password == password_reg:
                message = "Logged in SUCCESFULLY !!!"
                session["authenticated"]=True

            else:
                message = "Please check with your password"
        else:
            message = "Your email id is not registered"
    return render_template("login.html",message = message)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    message = "You are logged Out successfully"
    session.clear()
    return render_template("app.html",message = message) 
    
@app.route('/reverse', methods=['POST','GET'])
def reverse():
    reverse = ""
    if request.method == 'POST':
        str1=request.form.get('string')
        for i in str1 :
            reverse = i+reverse
        
    return render_template('reverse.html',result=reverse)

@app.route('/largest', methods = ['POST','GET'])
def largest():
    greatest = 0
    if request.method == 'POST':
        num1=int(request.form.get('number1'))
        num2=int(request.form.get('number2'))
        num3=int(request.form.get('number3'))
        if num1 > num2 and num1 > num3 :
            greatest = str(num1)+" is the greatest among the 3"
        elif num2 > num1 and num2 > num3 :  
            greatest = str(num2)+" is the greatest among the 3"
        elif num3 > num1 and num3 > num2 :  
            greatest = str(num3)+" is the greatest among the 3"
    return render_template('largest.html',result=greatest)

@app.route('/uppercase' , methods=['POST','GET'])
def uppercase():
    answer = ""
    if request.method == "POST":
        string = request.form.get("string",type=str)
        
        if string.isalpha():
            if string.islower():
                answer = string.upper() 
            else:
                answer = "Given input is not in lowercase"
        else:
            answer = "Given input is not a letter/ word"
    return render_template('uppercase.html' ,result=answer)

@app.route('/leapyear' , methods = ['POST','GET'])
def leapyear():
    answer = ""
    if request.method == 'POST':
        Year = request.form.get("year",type=int)
        if Year % 4 == 0 :
            if Year % 100 == 0 : 
                if Year%400 == 0 :
                    answer =  str(Year)+"is a Leap year"
                else : 
                    answer =  str(Year)+"is not a Leap year"
            else :
                answer =  str(Year)+"is a Leap year"
        else :
            answer = str(Year)+", It is not a Leap year"
    return render_template ('leapyear.html',result=answer)

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""
    if request.method == "POST":
        name = request.form.get ("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmpassword = request.form.get("confirmpassword")
        address = request.form.get("address")
        
        if confirmpassword == password :
            session["email"]=email
            session["password"]=password
            #session = {'email':email,'pssword':password}
            message = "Hey "+name+", registration successful !!!"+ "with the email id "+email
            return render_template("login.html",message=message)   
        else:
            message = "Sorry !!! password did not match with the confirmation password"
            return render_template("register.html",message = message)
            
    return render_template("register.html",message=message)            

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == "POST" :
        time = request.form.getlist("callTime")
        print(time)
    return render_template("checkbox.html")

@app.route('/radiob', methods=['GET', 'POST'])
def radiob():
    if request.method == "POST" :
        call = request.form.get("callTime")
        print(call)
    return render_template("radiobutton.html")

def quiz(user_choice,correct_answer):
        choice = request.form.get(user_choice)
        score = session.get("score",0)  
        message=''  
        if choice == correct_answer:
            score = score+10
            message= "Your answer is correct"
        else :
            message= "That wasn't the right answer"
        session['score']=score
        print(score)
        return [message,score]
def attempted():
    attempted_questions = session.get("attempted_questions", [])
    if "q1" in attempted_questions :
        error = "THE QUESTION IS ALREADY ATTEMPTED !"
        return render_template("error.html", error = error)
    attempted_questions.append("q1")
    session["attempted_questions"] = attempted_questions

@app.route('/attempted_questions/<token>') 
def attempted_questions(token):
    attempted_questions = session.get("attempted_questions", [])
    if token in attempted_questions :
        error = "THE QUESTION IS ALREADY ATTEMPTED !"
        return render_template("error.html", error = error)
    attempted_questions.append(token)
    session["attempted_questions"] = attempted_questions


@app.route('/quiz1', methods=['GET', 'POST'])
def quiz1():
    message = ""
    if not session.get("authenticated"):
        message = "Please login to access Quiz Page"
        return render_template("login.html",message = message)
    elif request.method == ("POST"):
        attempted_questions("q1")
        message = quiz ("country","Indonesia")
    return render_template("quiz1.html", result = message)

@app.route('/quiz2', methods=['GET', 'POST'])
def quiz2():
    message = ""
    if request.method == ("POST"):
        attempted_questions("q2")
        message = quiz ("area","Russia")
    return render_template("quiz2.html", result = message)

@app.route('/quiz3', methods=['GET', 'POST'])
def quiz3():
    message = ""
    if request.method == ("POST"):
        attempted_questions("q3")
        message = quiz ("least","VaticanCity")
    return render_template("quiz3.html", result = message)
        

@app.route('/quiz4', methods=['GET', 'POST'])
def quiz4():
    message = ""
    if request.method == ("POST"):
        attempted_questions("q4")
        message=quiz('leastarea','VaticanCity')
    return render_template("quiz4.html", result = message)
        
    

@app.route('/quiz5', methods=['GET', 'POST'])
def quiz5():
    message = ""
    if request.method == ("POST"):
        attempted_questions("q5")
        message=quiz('smallestc','Australia')
    return render_template("quiz5.html", result = message)

@app.route('/quiz6', methods=['GET', 'POST'])
def quiz6():
    message = ""
    if request.method == ("POST"):
        attempted_questions("q6")
        message=quiz('find','4')
    return render_template("quiz6.html", result = message)

@app.route('/quiz7', methods=['GET', 'POST'])
def quiz7():
    message = ""
    if request.method == ("POST"):
        attempted_questions("q7")
        message = quiz("covid-19","as it started in the year 2019")
    return render_template("quiz7.html", result = message)
        
    

@app.route('/quiz8', methods=['GET', 'POST'])
def quiz8():
    message = ""
    if request.method == ("POST"):
        attempted_questions("q8")
        message = quiz("virus","Omicron")
    return render_template("quiz8.html", result = message)

@app.route('/quiz9', methods=['GET', 'POST'])
def quiz9():
    message = ""
    if request.method == ("POST"):
        attempted_questions("q9")
        message = quiz("bank","HDFC Bank")
    return render_template("quiz9.html", result = message)

@app.route('/quiz10', methods=['GET', 'POST'])
def quiz10():
    message = ""
    if request.method == ("POST"):
        attempted_questions("q10")
        message = quiz("pm","Kuwait")
    return render_template("quiz10.html", result = message)

@app.route('/ty', methods=['GET', 'POST'])
def ty():
    session.clear()
    return render_template("ty.html")

@app.route('/calculator', methods = ['POST','GET'])
def calculator():
    message = 0

    if request.method == 'POST':
        num1= int(request.form.get("number1"))

        num2= int(request.form.get("number2"))
        operator = request.form.get("operator")
        if operator == "+":
            message = num1+num2
        elif operator == "-":
            message = num1-num2
        elif operator == "x":
            message = num1*num2
        elif operator == "÷":
            if num2 != 0:
                message = num1/num2
            else:
                message = "∞, infinite"
        elif operator == "remainder":
            if num2 != 0:
                message = num1/num2
            else:
                message = "∞, infinity"
        elif operator == "power":
            #message = num1**num2
            message = math.pow(num1,num2)
        elif operator == "root":
            #message = num1**1/num2
            message = math.pow(num1,1/num2)
            
    return render_template("calculator.html",result = message)

           

    
if __name__=="__main__":
    app.run(debug=True)

