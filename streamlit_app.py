import  streamlit
streamlit.title('my parents new healthy dinner')
streamlit.header('BREAKFAST MENU')
streamlit.text('idly')
streamlit.text('dosa with coconut chutny')
streamlit.text('chapathi with alu curry')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞avocado toast')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
