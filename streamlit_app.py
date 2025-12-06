import streamlit as st
import pandas as pd
import random
st.title("🎬 Recomendador de Películas por Emoción")
def cargar_datos():
    return pd.read_excel("pensamiento (2).xlsx")
peliculas = cargar_datos()
emociones = peliculas["EMOCIÓN"].unique().tolist()
emocion = st.selectbox("¿Cómo te sientes hoy?", emociones)
key_lista = f"recs_{emocion}"
if key_lista not in st.session_state:
    lista = peliculas[peliculas["EMOCIÓN"] == emocion]["PELÍCULAS"].tolist()
    random.shuffle(lista)
    st.session_state[key_lista] = lista.copy()
st.subheader(f"🎞️ Recomendaciones para: {emocion}")
lista_restante = st.session_state[key_lista]
if len(lista_restante) == 0:
    st.info("Ya no hay más recomendaciones para esta emoción ❤️")
else:
    mostrar = lista_restante[:3]
    for peli in mostrar:
        st.write("•", peli)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Quiero más recomendaciones"):
            st.session_state[key_lista] = lista_restante[3:]
    with col2:
        if st.button("No quiero más"):
            st.success("🍿 Me alegra que hayas encontrado tu película ideal ✨")
            st.session_state[key_lista] = []
