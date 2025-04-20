from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/Business Loan")
def tools_page():
    return render_template('bl.html')


@app.route("/Personal Loan")
def products_page():
    return render_template('pl.html')

@app.route("/Professional Loan")
def login_page():
    return render_template('prl.html')

@app.route("/Secure Loan")
def register_page():
    return render_template('sl.html')