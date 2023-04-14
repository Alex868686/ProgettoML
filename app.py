
import streamlit as st
import pandas as pd

st.title("Area Triang")

st.image("https://raw.githubusercontent.com/Frenz86/IFTS23/main/streamlit/bb.png", c)

def areatriangolo(l1:float,l2:float):
    a = (l1*l2)/2
    return a 

def main():
    st.text("Area triangoloooooo")
    # slider
    num1 = st.slider('Please inserisci base', 0, 100, 25)
    num2 = st.slider('Please inserisci altezza', 0, 100, 35)
    r = areatriangolo(num1,num1)

    st.write("l'area del triangolo è")



if __name__ == "__main__":
    main()