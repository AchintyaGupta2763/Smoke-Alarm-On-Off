import streamlit as st
import pickle as pkl
import sklearn
import numpy as np

model = pkl.load(open('model.pkl', 'rb'))
df1 = pkl.load(open('df1.pkl', 'rb'))

st.title('SMOKE ALARM ON/OFF')

UTC = st.number_input('UTC VALUE')
st.text('The average value of UTC is 1654792000')

Temperature = st.number_input('TEMPERATURE VALUE')
st.text('The average value of temperature is 15°C')

Humidity = st.number_input('HUMIDITY VALUE')
st.text('The average value of humidity is 48.53')

TVOC = st.number_input('TVOC VALUE')
st.text('The average value of TVOC 1942.05')

eCO2 = st.number_input('eCO2 VALUE')
st.text('The average value of eCO2 is 670.02')

Raw_H2 = st.number_input('RAW H2 VALUE')
st.text('The average value of RAW H2 is 12942.45')

Raw_Ethanol = st.number_input('RAW ETHANOL VALUE')
st.text('The average value of RAW ETHANOL is 19754.25')

Pressure = st.number_input('PRESSURE VALUE')
st.text('The average value of pressure is 938.62')

PM1_0 = st.number_input('PM1.0 VALUE')
st.text('The average value of PM1.0 is 100.59')

PM2_5 = st.number_input('PM2.5 VALUE')
st.text('The average value of PM2.5 is 184.46')

NC0_5 = st.number_input('NC0.5 VALUE')
st.text('The average value of NC0.5 is 491.46')

NC1_0 = st.number_input('NC1.0 VALUE')
st.text('The average value of NC1.0 is 203.58')

NC2_5 = st.number_input('NC2.5 VALUE')
st.text('The average value of NC2.5 is 80.049')

CNT = st.number_input('CNT VALUE')
st.text('The average value of CNT is 10511.38')

if st.button('ALARM CONDITION'):
    query = np.array([UTC, Temperature, Humidity, TVOC, eCO2, Raw_H2, Raw_Ethanol, Pressure, PM1_0, PM2_5, NC0_5, NC1_0,
                      NC2_5, CNT])
    query = query.reshape(1, 14)
    ans = model.predict(query)
    if ans == 1:
        st.title('ON')
    if ans == 0:
        st.title('OFF')
