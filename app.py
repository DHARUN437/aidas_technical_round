import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_excel('sales_data.xlsx')


st.title("Conversional Insights Assistant")

query = st.text_input("Ask a question about sales data:")

if query:
    if "what are the top selling products" in query.lower():
        st.image(r"assets\output.png")
    
    elif "who is the most returned customer" in query.lower():
       st.image(r'assets\image.png')
    
    elif "what is the average order value" in query.lower():
        avg_order_value = df["Total Price"].mean()
        
        st.write("### Average Order Value")
        st.write(avg_order_value)
    
    elif "what are the most profitable products" in query.lower():
        
        st.write("### Top 5 Most Profitable Products are :")
        st.image(r"assets\profit.png")
    
    elif "who is the most frequent customer" in query.lower():
                
        st.write("### The most Frequent Customers are :")
        st.image(r'assets\customers.png')
       
    
    else:
        st.write("Sorry, I couldn't understand your question")
