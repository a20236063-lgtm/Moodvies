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
if "progreso" not in st.session_state:
    st.session_state.progreso = {}
if "mostrar" not in st.session_state:
    st.session_state.mostrar = False
if emocion not in st.session_state.progreso:
    st.session_state.progreso[emocion] = 0
    st.session_state.mostrar = False
lista = peliculas[peliculas["EMOCIÓN"] == emocion]["PELÍCULAS"].tolist()
random.shuffle(lista)
st.subheader(f"Películas para cuando sientes: {emocion}")
if st.button("Mostrar recomendaciones"):
    st.session_state.mostrar = True
if st.session_state.mostrar:
    inicio = st.session_state.progreso[emocion]
    fin = inicio + 3
    subset = lista[inicio:fin]
    if subset:
        st.write("### 🍿 Tus recomendaciones:")
        for peli in subset:
            st.write("•", peli)
        st.session_state.progreso[emocion] = fin
        col1, col2 = st.columns(2)
        with col1:
            mas = st.button("Sí")
        with col2:
            no_mas = st.button("No")
        if mas:
            st.session_state.mostrar = True  # volver a mostrar
        if no_mas:
            st.success("¡Me alegra que hayas encontrado tu película ideal! ✨")
            st.session_state.mostrar = False
    else:
        st.warning("❤️ Ya no hay más recomendaciones.")
        st.session_state.progreso[emocion] = 0
        st.session_state.mostrar = False
