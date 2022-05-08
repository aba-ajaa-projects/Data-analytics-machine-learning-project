import pickle
import numpy as np
import pandas as pd
import streamlit as st
 
# loading the model
models_path = '../models/'
model_name = models_path + 'model3.pkl'
loaded_model = pickle.load(open(model_name, 'rb'))

# loading the scaler
scalers_path = '../scalers/'
scaler_name = scalers_path + 'scaler3.pkl'
loaded_scaler = pickle.load(open(scaler_name, 'rb'))

# Main page #
st.title("Will a client accept a credit card offer?")     

# Get input values - numeric variables

reward_desired = st.selectbox('What is the reward desired?', ('Air Miles','Cashback','Points')),

if 'Air Miles' in reward_desired:
    reward_desired = 0
elif 'Cashback' in reward_desired:
    reward_desired = 1
elif 'Points' in reward_desired:
    reward_desired = 2

mailer_type = st.selectbox('What is the mailer type?', ('Letter', 'Postcard'))

if 'Letter' in mailer_type:
    mailer_type = 0
elif 'Postcard' in mailer_type:
    mailer_type = 1

income_level = st.selectbox('What is the income level?', ('Low', 'Medium', 'High'))

if 'Low' in income_level:
    income_level = 0
elif 'Medium' in income_level:
    income_level = 1
elif 'High' in income_level:
    income_level = 2


open_accounts = st.slider('How many open accounts do you have?', 0, 10, 0)

overdraft_protection = st.selectbox('Have you overdraft protection?', ('Yes', 'No'))

if 'Yes' in overdraft_protection:
    overdraft_protection = 1
elif 'No' in overdraft_protection:
    overdraft_protection = 0



credit_rating = st.selectbox('What is the credit rating?' , ('Low', 'Medium', 'High'))

if 'Low' in credit_rating:
    credit_rating = 0
elif 'Medium' in credit_rating:
    credit_rating = 1
elif 'High' in credit_rating:
    credit_rating = 2



credit_cards_held = st.slider('How many credit cards held do you have?', 0, 10, 0)
homes_owded = st.number_input('How many homes do you owned?', min_value=0, max_value=1000, value=0)
household_size = st.number_input('How many people live in the household?', min_value=0, max_value=100, value=0)
owner_home = st.selectbox('Do you own the home?', ('Yes', 'No'))

if 'Yes' in owner_home:
    owner_home = 1
elif 'No' in owner_home:
    owner_home = 0


balanced_q1 = st.number_input('Enter average balanced Q1')
balanced_q2 = st.number_input('Enter average balanced Q2')
balanced_q3 = st.number_input('Enter average balanced Q3')
balanced_q4 = st.number_input('Enter average balanced Q4')



def Average(x):
    avg = sum(x) / len(x)
    return avg


if st.button("Average Balance"):
    Z = {balanced_q1, balanced_q2, balanced_q3, balanced_q4}
    Z_avg = Average(Z)
    st.success(Z_avg)


Z = {balanced_q1, balanced_q2, balanced_q3, balanced_q4}
Z_avg = Average(Z)


# when predict is clicked, make the prediction and store it
if st.button("Get Your Prediction"):
#encoding String variables

    X = pd.DataFrame({'Reward': [reward_desired],
                      'Mailer Type': [mailer_type],
                      'Income Level': [income_level],
                      'Bank Accounts Open': [open_accounts],
                      'Overdraft Protection': [overdraft_protection],
                      'Credit Rating': [credit_rating],
                      'Credit Cards Held': [credit_cards_held],
                      'Homes Owned': [homes_owded],
                      'Household Size': [household_size],
                      'Own Your Home': [owner_home],
                      'Average Balance': [Z_avg],
                      'Q1 Balance': [balanced_q1],
                      'Q2 Balance': [balanced_q2],
                      'Q3 Balance': [balanced_q3],
                      'Q4 Balance': [balanced_q4]})
    
    # Scaling data
    X_scaled = loaded_scaler.transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

    # Making predictions
    prediction = loaded_model.predict(X_scaled_df)

    # Displaying the prediction
    if (prediction == 0):
      st.success("The prediction of the model is: your client will not accept the offer.")
    else:
      st.success("The prediction of the model is: your client will accepted the offer.")