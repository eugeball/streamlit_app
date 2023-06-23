import streamlit
import pandas as pd
streamlit.title('Euge es la mas linda ahr')


streamlit.header('🥑🍞Menú de desayuno')
streamlit.text('🥑🍞Omega 3 y avena con arándanos')
streamlit.text('🥑🍞Batido de col rizada, espinacas y rúcula')
streamlit.text('🥑🍞Huevo de gallinas camperas hervidas')


streamlit.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')

my_fruit_list= pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("pick:", list(my_fruit_list.index),['Avocado','Strawberries']
