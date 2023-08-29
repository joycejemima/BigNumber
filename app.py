import streamlit as st

def main():
    st.header("Find the Largest Number")
    
    st.write("Enter three numbers:")
    num1 = st.number_input("Number 1", value=0)
    num2 = st.number_input("Number 2", value=0)
    num3 = st.number_input("Number 3", value=0)
    
    largest = max(num1, num2, num3)
    st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
