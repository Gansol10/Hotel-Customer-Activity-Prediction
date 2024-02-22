import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px 
from PIL import Image 

# Set page config
st.set_page_config(
    page_title= 'Hotel_Reservation_EDA',
    layout= 'wide',
    initial_sidebar_state= 'expanded'
)

# Create Function for EDA
def run():
    #Create title
    st.title('Hotel Reservation Visitors')

    # Create Sub Header atau Sub Judul
    st.subheader('EDA untuk Analisis Dataset ')

    # Add Image
    st.image('https://www.hotellinksolutions.com/images/blog/avt.jpg', caption= 'Hotel Reservation')

    # Create a Description
    st.write('Page Made by Allen')


    # Magic Syntax
    '''
    Pada page kali ini, penulis akan melakukan eksplorasi sederhana,
    Dataset yang digunakan adalah Credit Card Default.
    Dataset ini berasal dari Big Query Google

    '''

    # Create Straight Line
    st.markdown('---')

    # Show Dataframe
    df = pd.read_csv('hotel_reservations.csv')
    st.dataframe(df)

    # Booking Status
    st.write('### Plot Booking Status Customer')
    fig= plt.figure(figsize=(20,5))
    sns.countplot(x='booking_status', data=df)
    st.pyplot(fig)
    st.write('From information above we can take an information that visitors that not canceled their booking is bigger than canceled their booking `67.2%` to `32.8%`.')

    st.write('### Plot Room Type Customer')
    fig= plt.figure(figsize=(20,5))
    sns.countplot(x='room_type_reserved', data=df)
    st.pyplot(fig)
    st.write('From the information above `Room type 1` is the highest room type reserved by booking status and then the second popular is `Room type 4`')

    st.write('### Plot Market Segment')
    fig= plt.figure(figsize=(20,5))
    sns.countplot(x='market_segment_type', data=df)
    st.pyplot(fig)
    st.write('Market segment of booking status majority from online')

    st.write('### Plot Type of Meal Plan')
    fig= plt.figure(figsize=(20,5))
    sns.countplot(x='type_of_meal_plan', data=df)
    st.pyplot(fig)
    st.write('Visitors that not canceled and canceled in how they chose meal plan, the meal plan 1 is occupied the first place')

    st.write('### Plot Arrival Year')
    fig= plt.figure(figsize=(20,5))
    sns.countplot(x='arrival_year', data=df)
    st.pyplot(fig)
  
    st.write('### Plot Arrival Month')
    fig= plt.figure(figsize=(20,5))
    sns.countplot(x='arrival_month', data=df)
    st.pyplot(fig)
    st.write('The Conclusion Based on Arrival Year and Arrival Month is visitors activity in reservation hotel, crowded in October 2018')

    
if __name__ == '__main__':
    run()