import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="centered"
)

model = joblib.load('loan_lr_train.pkl')

st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #edf2f7;
}

/* Main Title */
h1 {
    color: #0d6efd;
    text-align: center;
    font-weight: bold;
    font-size: 42px;
}

/* Subtitle */
h3 {
    color: #0d6efd;
    text-align: center;
    font-weight: 600;
    margin-bottom: 30px;
}

/* Input Labels */
label {
    font-weight: 600 !important;
    color: #333333 !important;
}

/* Rounded Input Boxes */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    border-radius: 10px;
}

/* Predict Button */
div.stButton > button {
    background-color: #0d6efd;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
    transition: all 0.3s ease;
}

/* Predict Button Hover */
div.stButton > button:hover {
    background-color: #0b5ed7;
    color: white;
    transform: scale(1.02);
}

</style>

<h1>🏦 Loan Approval Prediction</h1>

<h3>Fill in the applicant details below</h3>

""", unsafe_allow_html=True)

#Gender
g=st.selectbox("Gender",["Male","Female"])
g_map={"Male":1,"Female":0}
g=g_map[g]

#Married
m=st.selectbox("Married",["Yes","No"])
m_map={"No":0,"Yes":1}
m=m_map[m]

#Dependents
d=st.selectbox("No. of dependents:",["0","1","2",'3+'])
d_map={"0":0,"1":1,"2":2,"3+":3}
d=d_map[d]

#Education
e=st.selectbox("Education Level:",["Graduate","Not Graduate"])
e_map={"Graduate":0,"Not Graduate":1}
e=e_map[e]

#Self_employed
se=st.radio("Self Employed",["Yes","No"])
se_map={"Yes":1,"No":0}
se=se_map[se]

#Applicant_income
ai=st.number_input("Applicant Income:",min_value=0.00,max_value=100000.00,format="%.2f")

#Coapplicantincome
cai=st.number_input("Coapplicant Income:",min_value=0.00,max_value=50000.00,format="%.2f")

#Loan_amount
la=st.number_input("Loan Amount:",min_value=9.0,max_value=1000.0,format="%.2f")

#Loan_amount_term
lat=st.number_input("Loan Amount Term:",min_value=12.0,max_value=480.0,format="%.2f")

#Credit_history
ch = st.selectbox("Credit History", ["Good", "Bad"])
ch_map = {"Good": 1, "Bad": 0}
ch = ch_map[ch]

#Property_area
pa=st.selectbox("Property area",["Rural","Urban","Semiurban"])
pa_map={"Rural":0,"Urban":2,"Semiurban":1}
pa=pa_map[pa]


if st.button("Predict"):
   info = [[g,m,d,e,se,ai,cai,la,lat,ch,pa]]

   pred = int(model.predict(info)[0])

   if pred == 1:
       
       st.success("✅ Predicted Loan Status: Loan Approved.")
       
   else:
        
        st.error("❌ Predicted Loan Status: Loan Rejected.")
