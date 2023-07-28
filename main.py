### Integrate HTML With Flask
### HTTP verb GET and POST

## Integrating with Jinja2 template
'''
{%...%} for statements
{{   }} expression to print output
{#   #} for commenting.
'''

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')
    

'''
We are building the URL Dynamically using variable rules.

'''
@app.route('/Success/<int:score>')     
def Success(score):
    res = ''
    if score>= 50:
        res = "PASS"
    else:
        res = 'FAIL'
    exp = {'score': score, 'res' : res }
    return render_template('results.html', result= exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is " + str(score)
    

@app.route('/Results/<int:score>')
def Results(score):
    res = ""
    if score<30:
        res =  'fail'
    else :
        res = 'Success'

    return redirect(url_for(res, score= score))

### Result checker html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score= 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float (request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
        res = ''
        if total_score > 50:
            res = 'Success'
        else:
            res = "fail"

        return redirect(url_for(res, score= total_score))
if __name__ == "__main__":
    app.run(debug= True)