import streamlit as st
import pandas as pd
import requests

def main():
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
  st.text(fruityvice_response.json())

  #take the json version of response and normalize it
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  #output it the screen as a table
  st.dataframe(fruityvice_normalized)

if __name__ == "__main__":
    main()
