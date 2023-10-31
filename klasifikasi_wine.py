import pickle
import streamlit as st

model = pickle.load(open('klasifikasi_wine_quality.sav', 'rb'))

st.title('Klasifikasi Wine Quality')

Id = st.number_input('ID')
fixed_acidity = st.number_input('fixed acidity')
volatile_acidty = st.number_input('volatile acidity')
citric_acid = st.number_input('citric acid')
residual_sugar = st.number_input('residual sugar')
chlorides = st.number_input('chlorides')
free_sulfur_dioxide = st.number_input('free sulfur dioxide')
total_sulfur_dioxide = st.number_input('total sulfur dioxide')
pH = st.number_input('pH')
sulphates = st.number_input('sulphates')
alcohol = st.slider('alcohol', 1, 10)
quality = st.slider('water', 1, 10)

predict = ''

if st.button('Submit'):
    predict = model.predict(
        [[Id, fixed_acidity, volatile_acidty, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, pH, sulphates, alcohol, quality]]
    )
    st.write('Klasifikasi Wine Quality:', predict[0])
