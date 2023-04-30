from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("glowna.html")

@app.route("/me")
def me():
    return render_template("strona.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("strona2.html")
    elif request.method == 'POST':
        print("Wiadomość wysłana")
        print(request.form)
        return redirect("/contact")
   
