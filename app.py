from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World! My First Application</h1>"
@app.route("/pages")
def thanks():
    return render_template('thanks.html')
