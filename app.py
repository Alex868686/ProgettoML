
import numpy as np
import streamlit as st
import pandas as pd
from numpy.random import rand

st.title("Rock Ginafri!!!????!")

st.video("gian.modificato.mp4")

def DDD(l1:float,l2:float):
    a = (l1*l2)/2
    return a 

def main():
    st.text("Gianfr level power")
    # slider
    num1 = st.slider('Please voti gianfranco', 0, 100, 25)
    num2 = st.slider('Please inserisci reddito leotta', 0, 100000, 35)
    r = DDD(num1,num1)

    st.write("Il livello di potenza di Leotta è pari a:",r)


if __name__ == "__main__":
    main()

st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">sei vecchio? Suonaaa !!</p>', unsafe_allow_html=True)

if st.button("Pigia se suoni!!!"):
    st.write("Fai bene vez!")
else:
    st.write("...")

if st.checkbox('marca se suoni rock'):
    st.write('Rockkk!!!!!!')
else:
    st.write("waiting...")
