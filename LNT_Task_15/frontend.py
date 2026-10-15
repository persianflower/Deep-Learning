
import pickle
import numpy as np
import pandas as pd
from tensorflow import keras, float16
import requests
from PIL import Image
import streamlit as st
import cv2

url = "http://0.0.0.0:8501/predict"

try:
    @st.cache_resource
    def load_model():
        with open('model_deep.pkl', 'rb') as f:
            model = pickle.load(f)
except Exception as e:
    print("Error loading model")

def main():
    try:
        model=load_model()
        st.title('CIFAR-10 Prediction')
        st.write('Predict the image shown')
        image = st.file_uploader("Choose a file")
        try:
            image =  Image.open(image)
            if st.button('Predict!'):
                max_size = (51, 73)
                image.thumbnail(max_size)
                # creating thumbnail
                image.save('thumb.png')
                new_img = np.array(image)
                new_img = cv2.resize(new_img, (32, 32))
                new_img = np.dot(new_img[..., :3], [0.2989, 0.5870, 0.1140])
                new_img = 255 - new_img
                data = np.array(new_img, dtype=np.float32)
                data = data.reshape(1, 32, 32, 3)
                #data = data / 255.0
                # Perform prediction
                try:
                    response = requests.post(url,json=new_img.tolist())
                    #prediction = response.json()
                    predicted_class = int(np.argmax(response))
                    labels=[
                        "1","2","3","4","5","6","7","8","9","10"
                    ]
                    label = labels[predicted_class]
                    st.success(f'Estimated category: {label}')
                except requests.RequestException.response as e:
                    st.error("Could not send request",e)
        except requests.RequestException.response as e:
            st.error("Please upload image",e)
    except Exception as e:
        print("Unexpected error",e)

if __name__ == '__main__':
    main()

