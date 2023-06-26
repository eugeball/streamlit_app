import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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
  

  #take the json version of response and normalize it
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  #output it the screen as a table
  st.dataframe(fruityvice_normalized)

  #new section to display fruityvice api response
  st.header('fruityvice fruit advice')
  try:
    fruit_choice =st.text_input('what fruit would you like information about?')
    if not fruit_choice:
      st.error('please select a fruit to get information.')
    else:
      fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized=pd.json_normalized(fruityvice_response.json())
      st.dataframe(fruityvice_normalized)

  except URLError as e:
    st.error()
    
  
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_cur = my_cnx.cursor()
  my_cur.execute("SELECT * from fruit_load_list")
  my_data_row = my_cur.fetchall()
  st.header("the fruit load list contains:")
  st.dataframe(my_data_row)

  st.write('thanks for adding', add_my_fruit)
  #this will not work correctly, but just go with it for now
  my_cur.execute("insert into fruit_load_list_values (´from streamlit')")
  
  
if __name__ == "__main__":
    main()
