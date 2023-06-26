import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

def main():
  st.title('menu menu menuuuuuu')
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

  #create the repeatable code block (called a function)
  def get_fruityvice_data(this_fruit_choice):
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized= pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
    
  #new section to display fruityvice api response
  st.header('fruityvice fruit advice')
  try:
    fruit_choice =st.text_input('what fruit would you like information about?')
    if not fruit_choice:
      st.error('please select a fruit to get information.')
    else:
      back_from_function = get_fruityvice_data(fruit_choice)
      st.dataframe(back_from_function)
      
  except URLError as e:
    st.error()
    
  st.header('the fruit load list contains:')
  #snowflake-reladed functions
  def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
      my_cur.execute('select * from fruit_load_list')
      return my_cur.fetchall()

  #add a button to load the fruit
  if st.button('get fruit load list'):
    my_cnx =snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows= get_fruit_load_list()
    st.dataframe(my_data_rows)
  
 
  st.write('thanks for adding', add_my_fruit)
  #this will not work correctly, but just go with it for now
  my_cur.execute("insert into fruit_load_list_values (´from streamlit')")
  
  
if __name__ == "__main__":
    main()
