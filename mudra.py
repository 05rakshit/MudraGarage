from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('index.html')

@app.route("/Tools")
def tools_page():
    pass


@app.route("/Products")
def products_page():
    pass

@app.route("/login")
def login_page():
    pass

@app.route("/register")
def register_page():
    pass