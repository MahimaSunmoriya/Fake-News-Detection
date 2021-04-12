from flask import Flask,redirect,url_for, render_template, request
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
app = Flask(__name__)

Pkl_Filename = "Pickle_RL_Model.pkl"  
with open(Pkl_Filename, 'rb') as file:  
    Pickled_LR_Model = pickle.load(file)

Pickled_LR_Model
vectorizer = pickle.load(open("vectorizer.pickle", 'rb'))
@app.route("/", methods=["POST", "GET"])
def index():
	Pass=""
	if request.method == "POST":
		Title = request.form["Heading"]
		Contents = request.form["material"]
		print(Title)
		print(Contents)
		# f = open("demofile.txt", "r")
		# text = 
		tfidf_test_one=vectorizer.transform([Contents])
		new_predit=Pickled_LR_Model.predict(tfidf_test_one)

		print(new_predit)
		if new_predit[0] == 'REAL':
		    Pass=1
		else:
		    Pass=2
		return render_template("index.html", result=Pass)
	else:
		Pass=""
	return render_template("index.html",result=Pass)
    

if __name__ == "__main__":
    app.run(debug=True)