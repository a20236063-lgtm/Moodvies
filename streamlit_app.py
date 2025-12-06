import streamlit as st
import pandas as pd
import random
st.title("🎬 Recomendador de Películas según tu emoción")
peliculas = pd.read_excel('pensamiento (2).xlsx')
emociones = [
    "Alegría", "Tristeza", "Enojo", "Miedo", "Justicia",
    "Nostálgia", "Romance", "Intriga", "Ternura"
]
emocion = st.selectbox("¿Cómo te sientes hoy?", emociones)
if "emocion_anterior" not in st.session_state:
    st.session_state.emocion_anterior = None
if st.session_state.emocion_anterior != emocion:
    st.session_state.index = 0
    st.session_state.emocion_anterior = emocion
lista = peliculas[peliculas["EMOCIÓN"] == emocion]["PELÍCULAS"].tolist()
random.shuffle(lista)
st.subheader(f"Películas para cuando sientes: {emocion}")
if "index" not in st.session_state:
    st.session_state.index = 0
if st.button("Mostrar recomendaciones"):
    inicio = st.session_state.index
    fin = inicio + 3
    subset = lista[inicio:fin]
    if subset:
        for peli in subset:
            st.write("🍿", peli)
        st.session_state.index = fin
    else:
        st.success("❤️ ¡Ya no hay más recomendaciones para esta emoción!")

