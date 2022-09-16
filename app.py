import numpy as np
from flask import Flask,request,render_template,jsonify
import pickle
import math

app=Flask(__name__)
model = pickle.load(open('taxi.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_feautres =  [int(x) for x in request.form.values()]
    final_feautres = [np.array(int_feautres)]
    prediction = model.predict(final_feautres)
    output= round(prediction[0],2)
    return render_template('index.html',prediction_text="NUMBER OF WEEKLY RIDES SHOULD BE:{}".format(math.floor(output)))

if __name__ == '__main__':
    app.run(debug=True)