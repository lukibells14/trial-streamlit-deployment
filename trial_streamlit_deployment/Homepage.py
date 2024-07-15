import streamlit as st
import mysql.connector

# Connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="192.168.10.142",
        user="Lenard",
        password="Hondafd14",
        database="Iguzzini"
    )

# Function to fetch data from database
def fetch_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM product LIMIT 20")
    data = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return data

# Main function to run the app
def main():
    st.title('Product Viewer')

    # Fetch data from the database
    data = fetch_data()

    # Display the data
    if data:
        st.write('## Products')
        for row in data:
            st.write(f"**Product Name:** {row[1]}")
            st.write(f"**Price:** ${row[2]}")
            st.write('---')
    else:
        st.warning('No products found.')

if __name__ == '__main__':
    main()
