from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello Welcome to my Website'

@app.route('/success/<int:score>')
def success(score):
    return 'The person is pass by:'+str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return 'The person is fail by:'+str(score)

@app.route("/results/<int:marks>")
def results(marks):
    result = ''
    if marks <45:
        result='fail'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    app.run(debug=True)