from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open('predict.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def predict():

	info = request.form.to_dict()
	cgpa = float(info['cgpa'])
	iq = int(info['iq'])
	profile_score = int(info['profile'])

	result = model.predict(np.array([cgpa, iq, profile_score]).reshape(1, 3))

	if result[0] == 1:
		res = 'Placed.'
	else:
		res = 'Better Luck Next Time, Bob.'

	return render_template('index.html', result=res)


if __name__ == '__main__':
	app.run(debug=False)