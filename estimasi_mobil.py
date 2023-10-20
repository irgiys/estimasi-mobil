import pickle
import streamlit as st

model = pickle.load(open("estimasi_mobil.sav", "rb"))
st.title("Estimasi harga mobil bekas")
year = st.number_input("Input tahun Mobil")
mileage = st.number_input("Input KM Mobil")
tax = st.number_input("Input pajak mobil")
mpg = st.number_input("Input konsumsi BBM Mobil")
engineSize = st.number_input("Input Engine size")

predict = ''

if st.button("Estimasi Harga"):
    predict = model.predict(
        [[year,mileage,tax,mpg,engineSize]]
    )
    st.write("Estimasi harga mobil bekas dalam Ponds : ", predict)
    st.write("Estimasi harga mobil bekas dalam Rupiah (Juta) : ", predict*19)