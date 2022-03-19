from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return '<h1>I want to Deploy Flask to Circle CI !!</h1>'

@app.route('/here')
def here():
    return '<h1>I Am Here at Circle CI !!</h1>'

@app.route('/there')
def here():
    return '<h1>I Am There at Circle CI !!</h1>'

if __name__=="__main__":
    app.run()
