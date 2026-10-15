
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from tensorflow import keras, float16
from PIL import Image
import cv2
app = Flask(__name__)

with open('model_deep.pkl','rb') as f:
    model = pickle.load(f)
@app.route('/')
def home():
    return "Fashion data prediction app working!"

@app.route('/predict',methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error":"No data provided"}),400
        new_img = np.asarray(data, dtype=np.float32) / 255.0
        if new_img.size != 32 * 32:
            return jsonify({
                "error": f"Expected 1024 pixels, got {data.size}"
            }), 400
        new_img = np.expand_dims(new_img, axis=0)
        #data = data / 255.0
        prediction = model.predict(new_img)[0]
        predicted_class = int(np.argmax(prediction))
        return jsonify({"prediction": predicted_class})
    except Exception as e:
        return jsonify({"error":str(e)}),400

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8501)


