# from flask import Flask
# ### WSGI Application 
# app = Flask(__name__)

# @app.route('/')
# def welcome():
#     return "Hello from Flask, Just don't break me!! AARRAA AARRA"

# @app.route('/members')
# def Members():
#     return "Welcome to the AARRAA ARRAA page"




# if __name__ == "__main__":
#     app.run(debug=True)

### Episode 2

"""
    Building Url Dynamically 
    Variable Rules and URL Building
"""

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def Welcome():
    return "Flask Welcomes you!!"

'''
We are building the URL Dynamically using variable rules.

'''
@app.route('/Success/<int:score>')     
def Success(score):
    return "<html><body><h1></h1>The Result is Passed</body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is " + str(score)
    

@app.route('/Results/<int:marks>')
def Results(marks):
    result = ""
    if marks<30:
        result =  'fail'
    else :
        result = 'Success'

    return redirect(url_for(result, score= marks))

if __name__ == "__main__":
    app.run(debug= True)