
import streamlit as st
import pandas as pd

st.title("Rock Output!!!????!")

st.image("https://raw.githubusercontent.com/Frenz86/IFTS23/main/streamlit/bb.png", caption="foto brutta brutta", width=250, clamp=True)

def DDD(l1:float,l2:float):
    a = (l1*l2)/2
    return a 

def main():
    st.text("Quanti anni hai?")
    # slider
    num1 = st.slider('Please inserisci eta effettiva', 0, 100, 25)
    num2 = st.slider('Please inserisci reddito medio', 0, 100, 35)
    r = DDD(num1,num1)

    st.write("Tra 1 anno di python avrai tot anni:",r)


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