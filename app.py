import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('sales_data.xlsx')


st.title("Conversional Insights Assistant")

query = st.text_input("Ask a question about sales data:")

if query:
    if "what are the top selling products" in query.lower():
        top_selling = df.groupby("Item ID")["Qty Ordered"].sum().nlargest(5)
        
        st.write("### The top 5 selling products are : ")
        st.bar_chart(top_selling)
        st.write(top_selling)
    
    
    elif "who is the most returned customer" in query.lower():
        top_returning_customers = df.groupby("Customer ID")["Qty Returned"].sum().nlargest(5)
        
        st.write("### Customers with Highest Returns")
        st.bar_chart(top_returning_customers)
        st.write(top_returning_customers)
    
    elif "what is the average order value" in query.lower():
        avg_order_value = df["Total Price"].mean()
        
        st.write("### Average Order Value")
        st.metric(label="Average Order Value (₹)", value=round(avg_order_value, 2))
    
    elif "what are the most profitable products" in query.lower():
        profitable_products = df.groupby("Item ID")["Total Price"].sum().nlargest(5)
        
        st.write("### Top 5 Most Profitable Products are :")
        st.bar_chart(profitable_products)
        st.write(profitable_products)
    
    elif "who is the most frequent customer" in query.lower():
        frequent_customers = df["Customer ID"].value_counts().nlargest(5)
        
        st.write("### The most Frequent Customers are :")
        st.bar_chart(frequent_customers)
        st.write(frequent_customers)
    
    
    else:
        st.write("Sorry, I couldn't understand your question. Try asking about top products, returns, order value, profits, or customers.")
