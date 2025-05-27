import streamlit as st

st.title("Selamat Datang")
st.write(
    "Macam-macam Hewan Berdasarkan Makanannya:"
)
st.image("IMG_0815.jpeg", width=200)
st.write("1. Hewan Karnivora adalah hewan yang memakan daging hewan lainnya. Contoh hewan karnivora adalah singa, harimau, buaya, dan lainnya")
st.image("IMG_0816.jpeg", width=200)
st.write("2. Hewan Herbivora adalah hewan yang memakan tumbuhan seperti daun dan biji. Contoh hewan herbivora adalah domba, sapi, dan lainnya")
st.image("IMG_0817.jpeg", width=200)
st.write("3. Hewan Omnivora adalah hewan yang memakan daging dan tumbuhan. Contoh hewan omnivora adalah burung gagak, babi, dan lainnya")

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
    
