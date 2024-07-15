import streamlit as st
from utils.database import get_connection

def main():
    st.title("Product Viewer")

    # Test database connection
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Product")
        products = cursor.fetchall()
        conn.close()

        st.success("Connected to the database successfully!")
        st.write("Products:")
        for product in products:
            st.write(product)
    except Exception as e:
        st.error(f"Failed to connect to the database: {e}")

if __name__ == "__main__":
    main()
