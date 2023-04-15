import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():

    """Show portfolio of stocks"""
   # db.execute("SELECT )
    display_shares = db.execute ("SELECT stocks.name_stock, stocks.price, stocks.number, users.cash FROM stocks JOIN users ON stocks.person_id = users.id WHERE person_id = (?) GROUP BY name_stock", session["user_id"])
    return render_template("index.html", display_shares = display_shares)
    #return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol2= request.form.get("symbol")
        dict_stock= lookup(symbol2)
        shares = int(request.form.get("shares"))

        if not symbol2 or dict_stock == None:
            return apology("that is not a good symbol mate")

        elif not shares or shares <=0:
            return apology("that's not a right number")


        #id = db.execute ("SELECT id FROM users WHERE hash = (?)", hash)
        cash = db.execute ("SELECT cash FROM users WHERE id = (?)", session["user_id"])
        if shares * dict_stock["price"] > cash[0]["cash"]:
            return apology("Sorry mate, you have not got enough cash")
        else:
            stocks= db.execute ("INSERT INTO stocks (name_stock, price, number, person_id) VALUES (?, ?, ?, ?)", dict_stock["name"], dict_stock["price"], shares, session["user_id"])
            remainder = cash[0]["cash"] - (shares * dict_stock["price"])
            update= db.execute("UPDATE users SET cash = (?) WHERE id =(?)", remainder, session["user_id"])
            bought = "bought"
            symbol_= lookup(symbol2)
            hist_stocks= db.execute ("INSERT INTO history (symbol, name, price, number, person_id, status) VALUES (?, ?, ?, ?, ?, ?)", symbol_["symbol"],dict_stock["name"], dict_stock["price"], shares, session["user_id"], bought)


            return redirect("/")
    else:
        return render_template("stocks.html")

    #return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    hist_table = db.execute("SELECT * FROM history WHERE person_id = (?)", session["user_id"])
    return render_template("history.html", hist_table= hist_table)
    #return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol or lookup(symbol) == None:
            return apology("You need to put a valid symbol")

        quote = lookup(symbol)
        return render_template ("quoted.html", quote=quote)
    else:
        return render_template("quote.html")

    #return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    users = []
    if "user" not in session:
        session["user"] = []

    if request.method == "POST":
        username = request.form.get("username")
        if not username or username in users:
            return apology("must provide valid username")

        password= request.form.get("password")
        if not password:
            return apology("must provide a password")
        redirect("/register")

        confirmation = request.form.get("confirmation")
        if confirmation == password:
            list = [username,password]
            session["user"].extend(list)
            users.append(username)
            hash = generate_password_hash (password)
            user = db.execute ("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return redirect("/login")


        else:
            return apology("passwords do not match")
    else:
        return render_template("register.html")




@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        to_sell= request.form.get("to_sell")
        stock_name = db.execute("SELECT DISTINCT name_stock FROM stocks WHERE person_id = (?)", session["user_id"])

        if not to_sell:
                return apology("You didn't put a stock")
        for symbol in stock_name:
            if to_sell not in symbol["name_stock"]:
                return apology("There is no such stock you own, mate!")

        total_shares = db.execute("SELECT SUM(number) FROM stocks WHERE person_id = (?)", session["user_id"])
        n_shares = request.form.get("n_shares")
        if not n_shares or int(n_shares) < 0 or int(n_shares) > total_shares[0]["SUM(number)"]:
            return apology ("invalid number of shares")
        else:
            symbol = db.execute("SELECT DISTINCT symbol FROM history WHERE name = (?)",to_sell)
            dict_sell= lookup(symbol[0]["symbol"])
            sold = "sold"
            current_cash = db.execute ("SELECT cash FROM users WHERE id = (?)", session["user_id"])
            sell_shares = db.execute("INSERT INTO history (symbol, name, number, price, status, person_id) VALUES (?, ?, ?, ?, ?, ?)", to_sell ,dict_sell["name"] ,n_shares, dict_sell["price"],sold, session["user_id"])
            updated_cash =  current_cash[0]["cash"] + int(n_shares) * dict_sell["price"]
            update_cash = db.execute ("UPDATE users SET cash = (?) WHERE id = (?)",updated_cash, session["user_id"])
            return redirect("/")
    else:
        stock_name = db.execute("SELECT DISTINCT name_stock FROM stocks WHERE person_id = (?)", session["user_id"])
        return render_template("sell.html", symbols2 = stock_name)

    """Sell shares of stock"""
    #return apology("TODO")
