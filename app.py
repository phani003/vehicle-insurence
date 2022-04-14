
import pandas as pd
import streamlit as st
import pickle
import numpy as np
import sklearn 



pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('data.pkl','rb'))


st.title(' vehicle insurence ')


st.title('person details')

gender=st.selectbox('Gender',df['Gender'].unique())
age=st.number_input('AGE')
region=st.selectbox('Region code',df['Region_Code'].unique())
dl=st.selectbox('Driving licence',['yes','no'])

st.title('vehicle information')

pi=st.selectbox('Previously insurene',['yes','no'])
va=st.number_input("enter age of vehicle")
vd=st.selectbox('vehicle damage',df['Vehicle_Damage'].unique())

st.title("plocy informatin")

ap=st.number_input('Annual premium')
psc=st.selectbox('Policy Sales Channel',df['Policy_Sales_Channel'].unique())
vn=st.selectbox('ENter vintage',df['Vintage'].unique())


if st.button('Predict'):

    if dl=='yes':
        d=1
    elif dl=='no':
        d=0  
    if pi=='yes':
        p=1
    elif pi=='no':
        p=0   
    query=np.array([gender,age,d,region,p,va,vd,ap,psc,vn])
    query=query.reshape(1,10)

    ped=pipe.predict(query)
    
    if ped==1:
        st.title('custamer interested')

    elif ped==0:
        st.title('custamer not interested')
   










