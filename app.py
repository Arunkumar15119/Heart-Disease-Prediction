import pickle
import pandas as pd
import streamlit as st

# Load the dataset
df = pd.read_csv("Cleaned_df.csv")


with open("Log_reg_model.pkl","rb") as file:
    model = pickle.load(file)


st.header("🏥Heart Disease Diagnostic Assistance")

#page setup
st.set_page_config(page_icon="🫀",page_title="Heart Disease Predictor")


with st.sidebar:
    st.title("Heart Disease Predictor")
    st.image("Heart.png")


#user input

col1,col2 = st.columns(2)

with col1:
    age = st.number_input("Age: ",min_value=1,max_value=100)

    gender = st.radio("Gender: ",options=["Male","Female"],horizontal=True)
    gender = 1 if gender=="Male" else 0

    d = {"typical angina":0,"atypical angina":1,"non-anginal pain":2,"asymptomatic":3}
    chest_pain = st.selectbox("chest pain type: ",options=d)
    chest_pain = d[chest_pain] # to get numeric val

    resting_bp = st.number_input("Resting BP: ",min_value=80,max_value=250,step=5)
    cholestrol = st.number_input("Cholestrol: ",min_value=80,max_value=600,step=5)

    fbs = st.radio("Fasting Blood sugar: ",options=["Yes","No"],horizontal=True)
    fbs = 1 if fbs=="Yes" else 0    

    d = {"Normal":0,"ST-T wave abnormality":1," left ventricular hypertrophy":2}
    restecg = st.selectbox("Rest ECG: ",options=d)
    restecg = d[restecg]


with col2:
    max = st.number_input("Max Heart rate: ",min_value=60,max_value=260,step=10)

    exang = st.radio("Exer induced angina: ",options=["Yes","No"],horizontal=True)
    exang = 1 if exang=="Yes" else 0

    oldpeak = st.number_input("Oldpeak: ",min_value=0.0,max_value=7.0,step=0.5)


    d = {"upsloping":0,"flat":1,"downsloping":2}
    slope = st.selectbox("Slope: ",options=d)
    slope = d[slope]

    num_major_vessels = st.selectbox("Num of major vessels: ",options=[0,1,2,3,4])


    d = {"normal":1,"fixed defect":2,"reversable defect":3}
    thal = st.selectbox("Thal: ",options=d)
    thal = d[thal]


c1,c2,c3 = st.columns([1.5,1,1])
if c2.button("Predict"):
    data = [[age,gender,chest_pain,resting_bp,cholestrol,fbs,restecg,max,exang,oldpeak,slope,num_major_vessels,thal]]
    pred = model.predict(data)[0]
    if pred==0:
        st.subheader("Low risk of Heart disease")
    else:

        st.subheader("High risk of Heart disease")
