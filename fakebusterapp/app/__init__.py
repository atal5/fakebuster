from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
import random


app = Flask(__name__)
Bootstrap(app)

#Write a function to handle the button press from
@app.route("/predict",methods=['POST'])
def predict():
    result = ['This is fake','This is real story']
    result = random.choice(result)
    if request.method == 'POST':
        text = request.form['comment']
		# data = [text]
		# vect = cv.transform(data).toarray()
		# my_prediction = clf.predict(vect)
    return render_template("index.html",result=result,usertext=text)

@app.route("/")
def index():
    return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)
