from flask import Flask,redirect,url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    Pass=""
    if request.method == "POST":
        Title = request.form["Heading"]
        Contents = request.form["material"]
        print(Title)
        print(Contents)
        if Contents == "Pass":
            Pass=1
        else:
            Pass=2
        return render_template("index.html", result=Pass)
    else:
        Pass=""
        return render_template("index.html",result=Pass)
    

if __name__ == "__main__":
    app.run(debug=True)