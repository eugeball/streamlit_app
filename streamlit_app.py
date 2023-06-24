''' import streamlit
import pandas as pd
streamlit.title('Euge es la mas linda ahr')


streamlit.header('🥑🍞Menú de desayuno')
streamlit.text('🥑🍞Omega 3 y avena con arándanos')
streamlit.text('🥑🍞Batido de col rizada, espinacas y rúcula')
streamlit.text('🥑🍞Huevo de gallinas camperas hervidas')


streamlit.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')

my_fruit_list= pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)

fruit_selected = streamlit.multiselect("Pick:", list(my_fruit_list.index)
fruit_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)

#nueva seccion de display fruityvice
import requests
fruityvice_response =requests.get ("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

'''

import streamlit as st
import pandas as pd
import requests

st.title('Euge es la mas linda ahr')
st.header('🥑🍞Menú de desayuno')
st.text('🥑🍞Omega 3 y avena con arándanos')
st.text('🥑🍞Batido de col rizada, espinacas y rúcula')
st.text('🥑🍞Huevo de gallinas camperas hervidas')

st.header('🍌🥭 Crea tu propio batido de frutas 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
st.dataframe(my_fruit_list)

fruit_selected = st.multiselect("Pick:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruit_selected]
st.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.json(fruityvice_response.json())



