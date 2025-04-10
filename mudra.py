from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('index.html')

@app.route("/Tools")
def tools_page():
    return render_template('tools.html')


@app.route("/Products")
def products_page():
    return render_template('products.html')

@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/register")
def register_page():
    return render_template('register.html')