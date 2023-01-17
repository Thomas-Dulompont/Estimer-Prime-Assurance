import streamlit as st
import pickle
import pandas as pd

pickle_in = open('model/model.pkl', 'rb')
model = pickle.load(pickle_in)

st.title("Hello world")

def calculer_charge(infos:list):
    infos = pd.DataFrame([infos],columns=["age","sex","bmi","children","smoker","region"])
    predict = model.predict(infos)
    return round(predict[0], 2)


age = st.number_input("Age du client :", min_value=18)

sex = st.selectbox("Genre du client :",['Femme', 'Homme'])
if sex == "Femme":
    sex = "female"
elif sex == "Homme":
    sex = "female"

bmi = st.radio("Connaissez-vous l'IMC du client ?", ['Oui', 'Non'])
imc = 20
if bmi == "Oui":
    imc = st.number_input("IMC du client :", min_value=0.0)
    imc = round(imc, 1)

if bmi == "Non":
    taille = st.number_input("Taille du client en cm :", min_value=0)
    poid = st.number_input("Poid du client en kg:", min_value=0.0)
    if taille != 0 and poid != 0:
        imc = round((poid / ((taille/10)**2))*100, 1)

if imc > 50:
    imc = 50

enfants = st.number_input("Nombre d'enfants du client :", min_value=0)
if enfants > 5:
    enfants = 5

fumeur = st.radio("Le client est fumeur :", ['Oui', 'Non'])
if fumeur == "Oui":
    fumeur = "yes"
elif fumeur == "Non":
    fumeur = "no"

region = st.selectbox("Region du client :", ['southwest', 'southeast', 'northwest', 'northeast'])

if st.button('Calculer'):
    st.write(calculer_charge([age, sex, imc, enfants, fumeur, region]))