from flask import Flask,render_template,request
import pickle
import numpy as np


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/form')
def formpage():
    return render_template('form.html')

@app.route('/predict',methods=['POST'])
def predict():
    N = request.form['N']
    print(N)
    P = request.form['P']
    K = request.form['K']
    T = request.form['T']
    H = request.form['H']
    P = request.form['P']
    R = request.form['R']

    Soil_composition_list = np.array([N,P,K,T,H,P,R]).reshape(1,7)
    print(Soil_composition_list)
    loaded_model = pickle.load(open('Crop_recommendation.sav', 'rb'))
    result = loaded_model.predict(Soil_composition_list)
    print(result)

    return render_template('prediction.html',result = result)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)