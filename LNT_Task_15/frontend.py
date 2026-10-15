
import pickle
import numpy as np
import pandas as pd
from tensorflow import keras, float16
import requests
from PIL import Image
import streamlit as st
import cv2
import os

url = os.getenv(
    "API_URL",
    "http://localhost:8501"
)

try:
    @st.cache_resource
    def load_model():
        with open('model_deep.pkl', 'rb') as f:
            model = pickle.load(f)
except Exception as e:
    print("Error loading model")

def main():
    try:
        #model=load_model()
        st.title('CIFAR-10 Prediction')
        st.write('Predict the image shown')
        image = st.file_uploader("Choose a file")
        try:
            image =  Image.open(image).convert("RGB")
            if st.button('Predict!'):
                max_size = (51, 73)
                image.thumbnail(max_size)
                # creating thumbnail
                image.save('thumb.png')
                new_img = np.asarray(image,dtype=np.float32) / 255.0
                new_img = 255 - new_img
                new_img = np.expand_dims(new_img,axis=0)
                try:
                    response = requests.post(f"{url}/predict",json=new_img.tolist())
                    #prediction = response.json()
                    predicted_class = int(np.argmax(response))
                    labels=[
                        "airplane","automobile","bird","cat","deer",
                        "dog","frog","horse","ship","truck"
                    ]
                    label = labels[predicted_class]
                    st.success(f'Estimated category: {label}')
                except requests.exceptions.RequestException as e:
                    st.error("Could not send request",e)
        except requests.exceptions.RequestException as e:
            st.error("Please upload image",e)
    except Exception as e:
        print("Unexpected error",e)

if __name__ == '__main__':
    main()

