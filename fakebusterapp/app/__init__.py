from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
import random
#from sklearn.externals import joblib
import re
import pickle as pk


app = Flask(__name__)
Bootstrap(app)

def clean_str(string):
    string = re.sub(r"\n", "", string)
    string = re.sub(r"\r", "", string)
    #string = re.sub(r"[0-9]", "digit", string)
    string = re.sub(r"\'", "", string)
    string = re.sub(r"\"", "", string)
    return string.strip()



#Write a function to handle the button press from
@app.route("/predict",methods=['POST'])
def predict():
    #result = ['This is fake','This is real story']
    #result = random.choice(result)
    if request.method == 'POST':
        text = request.form['comment']
		# data = [text]
		# vect = cv.transform(data).toarray()
		# my_prediction = clf.predict(vect)
        clean_input = clean_str(text)
        #model = joblib.load('fakebustermodel.pkl')
        result = model.predict([clean_input])[0]
    return render_template("index.html",result=result,usertext=text)

@app.route("/")
def index():
    return render_template("index.html")

model = pk.load(open('./models/fakebustermodel.pkl', 'rb'))
# if __name__ == "__main__":
#     app.run(debug=True)
