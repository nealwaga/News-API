from flask import Flask

app=Flask(__name__)

@app.route("/")
def intro():
    #home.html
    return "<h1>This is my deployed application</h1>"


if __name__=="__main__":    
    app.run(debug=True)