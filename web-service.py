# flask for web app.
import flask as fl
from flask import request, jsonify
# numpy for numerical arrays.
import numpy as np
# tensorflow nerural network
import tensorflow as tf
# keras API
from tensorflow import keras 

# Create a new web app.
app = fl.Flask(__name__)

# function to load wind turbine prediction model
def load_keras_model():
	# load in pre-trained model
	return keras.models.load_model('powermodel.h5')

# load prediction model
model = load_keras_model()

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add api route.
@app.route('/api', methods=["POST"])
def getPower():
	input = request.form['speed'] 
	num = float(input)
	prediction = model.predict([num])
	result = prediction[0][0].tolist()
	return {"value": result}
