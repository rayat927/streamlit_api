import pickle
import pandas as pd
import sklearn
import streamlit as st

model = pickle.load(open('RF.pkl', 'rb'))

# predict = model.predict([[1, 39, 0, 0, 0, 0, 195, 106, 70, 26.97, 80, 77]])

# print(predict)

cols = ['']

def main(): 
    st.title("Hypertension Risk Prediction")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Hypertension Risk Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    sex = st.text_input('Sex', '0')
    age = st.text_input('Age', '0')
    currentSmoker = st.text_input('Current Smoker', '0')
    cigsPerDay = st.text_input('Cigs per day', '0')
    BPMeds = st.text_input('BPMeds', '0')
    diabetes = st.text_input('diabetes', '0')
    totChol = st.text_input('totChol', '0')
    sysBP = st.text_input('sysBP', '0')
    diaBP = st.text_input('diaBP', '0')
    BMI = st.text_input('BMI', '0')
    heartRate = st.text_input('heartRate', '0')
    glucose = st.text_input('glucose', '0')

    if st.button("Predict"):      
        prediction = model.predict([[int(sex), int(age), int(currentSmoker), 
                                     float(cigsPerDay), float(BPMeds), int(diabetes),
                                     float(totChol), float(sysBP), 
                                     float(diaBP), float(BMI),float(heartRate), float(glucose)]])

        output = int(prediction[0])
        if output == 1:
            text = 'High risk'
        else:
            text = 'Low risk'
        st.success('Output is {}'.format(text))


if __name__=='__main__':
    main()