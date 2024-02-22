import pickle
import json
import pandas as pd 
import numpy as np
import streamlit as st

# Load All Files
with open('best_param.pkl', 'rb') as file_1:
 best_params = pickle.load(file_1)

with open('preprocessing_pipeline.pkl', 'rb') as file_2:
 preprocessing_pipeline= pickle.load(file_2)

def run ():
  with st.form(key ='PREDICT VISITORS FORM'): #Nulis nama sendiri menggunakan name= st.text_input('')
    Booking_ID= st.text_input('Booking_ID', 'Input ID Here')
    no_of_adults = st.number_input('Number of Adults')
    no_of_children= st.number_input('Number of Children')
    no_of_weekend_nights= st.number_input('Number of Weekend Nights', min_value=0, max_value=7)
    no_of_week_nights= st.number_input('Number of Week Nights', min_value=0, max_value=17)
    type_of_meal_plan= st.selectbox(
    'Choose your Meal Plan',
    ('Meal Plan 1', 'Not Selected', 'Meal Plan 2', 'Meal Plan 3'))
    required_car_parking_space= st.number_input('Required Car Parking Space')
    room_type_reserved=  st.selectbox(
    'Choose your Room Type',
    ('Room_Type 1', 'Room_Type 4', 'Room_Type 2', 'Room_Type 6',
       'Room_Type 5', 'Room_Type 7', 'Room_Type 3'))
    lead_time= st.number_input('The number of days between booking and arrival')
    arrival_year= st.number_input('The year of arrival')
    arrival_month= st.number_input('The month of arrival', min_value=1, max_value=12)
    arrival_date= st.number_input('The date of arrival', min_value=1, max_value=31)
    market_segment_type=  st.selectbox(
    'What Segment Type of Customer',
    ('Offline', 'Online', 'Corporate', 'Aviation', 'Complementary'))
    repeated_guest= st.number_input('Repeated Guest')
    no_of_previous_cancellations= st.number_input('The number of previous cancellations by the guest')
    no_of_previous_bookings_not_canceled= st.number_input('The number of previous bookings not canceled by the guest')
    avg_price_per_room= st.number_input('The average price per room')
    no_of_special_requests= st.number_input('The number of special requests made by the guest', min_value=0, max_value=5)
    submitted = st.form_submit_button('Predict')

  # Create New Data
  df_inf={
    'Booking_ID': Booking_ID, 
    'no_of_adults': no_of_adults, 
    'no_of_children': no_of_children, 
    'no_of_weekend_nights':no_of_weekend_nights,
    'no_of_week_nights':no_of_week_nights, 
    'type_of_meal_plan':type_of_meal_plan, 
    'required_car_parking_space': required_car_parking_space,
    'room_type_reserved':room_type_reserved, 
    'lead_time':lead_time, 
    'arrival_year': arrival_year, 
    'arrival_month':arrival_month,
    'arrival_date':arrival_date, 
    'market_segment_type':market_segment_type, 
    'repeated_guest':repeated_guest,
    'no_of_previous_cancellations':no_of_previous_cancellations, 
    'no_of_previous_bookings_not_canceled':no_of_previous_bookings_not_canceled,
    'avg_price_per_room':avg_price_per_room, 
    'no_of_special_requests':no_of_special_requests, 
        }
  df_inf = pd.DataFrame([df_inf])

  if submitted: 
    prediction = best_params.predict(df_inf)
    st.write('This Visitor Predicted:', round(prediction[0],2))
    # df_inf_best_params = df_inf[best_params]
    # df_inf_classifier= df_inf[preprocessing_pipeline]
    # df_inf_final = np.concatenate([preprocessing_pipeline], axis=1)
    # y_pred_inf = best_params.predict(df_inf_final) 
    # st.write(f'# Rating {best_params}:', int(y_pred_inf))


if best_params == '__main__':
  run()