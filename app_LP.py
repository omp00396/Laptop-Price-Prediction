import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("C:\\Users\\hp\\Downloads\\LP.pkl",'rb'))
df = pd.read_csv("C:\\Users\\hp\\Desktop\\Laptop_Price\\laptop_price.csv", encoding='latin-1')


# Define the user input interface
st.title("Laptop Price Prediction")
st.write("Enter the Laptop details below:")


unique_values1 = df["Company"].unique().tolist()
company = st.selectbox("Select Company Name : ", unique_values1)

unique_values2 = df["TypeName"].unique().tolist()
type_name = st.selectbox("Select TypeName Name : ", unique_values2)

inches = st.number_input("Inches : ", value=0)
ram = st.number_input("Ram : ", value=0)

unique_values3 = df["OpSys"].unique().tolist()
op_sys = st.selectbox("Select OpSys Name : ", unique_values3)

weight = st.number_input("Weight : ", value=0)

# query = np.array([company,type_name,inches,ram,op_sys,weight])
# query = query.reshape(1, 6)
# prediction = str(int(np.exp(model.predict(query)[0])))
# st.title("The predicted price of this configuration is " + prediction)

# Display the prediction to the user
if st.button("Estimate Price", key='predict'):
    # Make the prediction
    # prediction = model.predict(pd.DataFrame([[company,type_name,inches,ram,op_sys,weight]],columns=['Company'	,'TypeName',	'Inches',	'Ram',	'OpSys',	'Weight']))
    prediction = model.predict(pd.DataFrame([[company, type_name, inches, ram, op_sys, weight]], columns=['Company', 'TypeName', 'Inches', 'Ram', 'OpSys', 'Weight']))

    output = round(prediction[0],2)
    if output<0:
        st.warning("Not able to predict laptop price on this features !!")
    else:
        st.success("The predicted price of this configuration is " + prediction)

# Company	TypeName	Inches	Ram	OpSys	Weight	Price_euros
# 0	Apple	Ultrabook	13.3	8	macOS	1.37	1339.69 """"
# st.write(model.predict(pd.DataFrame([['Apple','Ultrabook',13.3,8,	'macOS',1.37]],columns=['Company','TypeName','Inches','Ram','OpSys','Weight'])))

# print(model.predict(pd.DataFrame([['HP','Ultrabook',13.3,64,'macOS',1.37]],columns=['Company','TypeName','Inches','Ram','OpSys','Weight'])))
