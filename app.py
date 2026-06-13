import streamlit as st
import tensorflow as tf
import numpy as np
import time
import warnings
from tensorflow.keras.utils import img_to_array, load_img
from src.disease_information import plant_disease_dict, model_mapping_dict

warnings.filterwarnings("ignore")

def display_plant_disease_dictrmation(result, plant_type):
    if result == 'Healthy':
        st.success("*Your plant is Healthy*")
        description = plant_disease_dict[result]['Description']
        symptoms = plant_disease_dict[result]['Symptoms']
        treatment = plant_disease_dict[result]['Treatment']
        time.sleep(3)
        st.balloons()
    else:
        st.error("*Your plant has {} disease*".format(result))
        description = plant_disease_dict[plant_type][result]['Description']
        symptoms = plant_disease_dict[plant_type][result]['Symptoms']
        treatment = plant_disease_dict[plant_type][result]['Treatment']
        time.sleep(3)

    st.sidebar.write("## *Description*")
    st.sidebar.write(description)
    st.write('## *Symptoms:*')
    st.write(symptoms)
    st.write('## *Treatment:*')
    st.write(treatment)

def select_model(plant_type):
    model_mapping = model_mapping_dict
    model_path = "models/" + model_mapping[plant_type]['model_path']
    classes = model_mapping[plant_type]['classes']
    return classes, model_path

def predict_disease(uploaded_image, plant_type):
    classes, model_path = select_model(plant_type)
    
    # Model load fix: compile=False se deserialization error ruk jayega
    model = tf.keras.models.load_model(model_path, compile=False)
    
    # Import fix: load_img aur img_to_array ab tensorflow.keras.utils se aayenge
    loaded_image = load_img(uploaded_image, target_size=(256, 256))
    image_arr = img_to_array(loaded_image)
    image = np.expand_dims(image_arr, axis=0)
    
    pred = model.predict(image)
    result = classes[np.argmax(pred[0])]
    display_plant_disease_dictrmation(result, plant_type)

st.title('*PlantGuard: Intelligent Plant Disease Detection* 🌱')

plant_type = st.selectbox('*Select Plant Type*', options=[
    'Apple', 'Cherry', 'Corn', 'Grape', 'Peach', 'Pepper', 'Potato', 'Strawberry', 'Tomato'])

uploaded_image = st.file_uploader('*Upload an image*', ['jpeg', 'png', 'jpg'])
st.sidebar.write("## *Selected Plant Type:*", plant_type)

if uploaded_image is not None:
    st.sidebar.image(uploaded_image)
    if st.button('Predict Disease'):
        with st.spinner('Processing the image...'):
            predict_disease(uploaded_image, plant_type)