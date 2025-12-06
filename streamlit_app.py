import streamlit as st
import pandas as pd
import random
st.set_page_config(page_title="Recomendador de Películas", layout="centered")
st.title("🎬 Recomendador de Películas según tu emoción")
peliculas_df = pd.read_excel('pensamiento (2).xlsx')
emociones = [
    "Alegría", "Tristeza", "Enojo", "Miedo", "Justicia",
    "Nostálgia", "Romance", "Intriga", "Ternura"
]
emocion = st.selectbox("¿Cómo te sientes hoy?", emociones)
if "listas" not in st.session_state:
    st.session_state.listas = {}
if "progreso" not in st.session_state:
    st.session_state.progreso = {}
if "mostrar" not in st.session_state:
    st.session_state.mostrar = False
if emocion not in st.session_state.listas:
    lista_raw = peliculas_df[peliculas_df["EMOCIÓN"] == emocion]["PELÍCULAS"].tolist()
    shuffled = lista_raw.copy()
    random.shuffle(shuffled)
    st.session_state.listas[emocion] = shuffled
    st.session_state.progreso[emocion] = 0  
st.subheader(f"Películas para cuando sientes: {emocion}")
if st.button("Mostrar recomendaciones", key=f"mostrar_{emocion}"):
    st.session_state.mostrar = True
if st.session_state.mostrar:
    lista = st.session_state.listas.get(emocion, [])
    inicio = st.session_state.progreso.get(emocion, 0)
    fin = inicio + 3
    subset = lista[inicio:fin]
    if subset:
        st.write("### 🍿 Tus recomendaciones:")
        for peli in subset:
            st.write("•", peli)
        st.write("**¿Quieres más recomendaciones?**")
        col1, col2 = st.columns([1, 1])
        with col1:
            mas = st.button("Sí, quiero más 🍿", key=f"mas_{emocion}")
        with col2:
            no_mas = st.button("No, ya estoy feliz ❤️", key=f"no_{emocion}")
        if mas:
            st.session_state.progreso[emocion] = fin
            st.experimental_rerun()
        if no_mas:
            st.success("¡Me alegra que hayas encontrado tu película ideal! ✨")
            st.session_state.mostrar = False

    else:
        st.warning("❤️ Ya no hay más recomendaciones para esta emoción.")
